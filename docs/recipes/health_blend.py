from csc.conceptnet4.models import *
from csc.conceptnet4.analogyspace import *
from csc.divisi.util import get_picklecached_thing
from csc.divisi.blend import Blend
from csc.divisi.export_svdview import write_packed

cnet = get_picklecached_thing('cnet.pickle.gz', lambda: conceptnet_2d_from_db('en'))

def make_blend(other):
    return Blend([cnet, other])

def run_cnet_blend(other, FILENAME='blend'):
    blend = get_picklecached_thing(FILENAME+'.pickle.gz',
        lambda: make_blend(other))
    svd = blend.svd()
    write_packed(svd.u, FILENAME, unstem=lambda x: x)
    return svd

def example():
    # In the context of this corpus of healthcare-related messages (not
    # publicly provided), what do people want?
    
    health = get_picklecached_thing('health.pickle.gz', None)
    svd = run_cnet_blend(health, 'health_blend')
    svd.summarize(10)

    # Make a labeled vector of similarities to the feature person\Desires.
    vec = predict_concepts(svd, ('left', 'Desires', 'person'))

    # Get the list of concepts in ConceptNet.
    concepts = cnet.label_list(0)

    # Look for concepts that *aren't* in ConceptNet and are ranked highly
    # in the vector of results.
    for item in vec.top_items(5000):
        
        # skip over stopwords
        contentful = False
        for word in item[0].split(' '):
            if not en.nl.is_stopword(word):
                contentful = True
                break

        if contentful and item[0] not in concepts:
            # found one. print it along with its score.
            print item[0], item[1]

if __name__ == '__main__': example()

