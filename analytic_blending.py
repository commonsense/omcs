from joblib import Memory
memory = Memory(cachedir='cache')

import divisi2
from csc_utils.ordered_set import OrderedSet
from luminoso2.assoc_space import SVDSpace
import numpy as np

K = 200

@memory.cache
def build_matrices():
    cnet = divisi2.network.conceptnet_matrix('en')
    isa_features = [feat for feat in cnet.col_labels if feat[1] == 'IsA']
    usedfor_features = [feat for feat in cnet.col_labels if feat[1] == 'UsedFor']
    joined_features = OrderedSet(isa_features+usedfor_features)

    cnet_entries = cnet.named_entries()
    isa_ent = [entry for entry in cnet_entries if entry[2][1] == 'IsA']
    usedfor_ent = [entry for entry in cnet_entries if entry[2][1] == 'UsedFor']
    row_labels = OrderedSet(row for val, row, col in (isa_ent + usedfor_ent))

    isa_mat = divisi2.sparse.SparseMatrix.from_named_lists(*(zip(*isa_ent)+[row_labels, joined_features]))
    usedfor_mat = divisi2.sparse.SparseMatrix.from_named_lists(*(zip(*usedfor_ent)+[row_labels, joined_features]))

    return dict(
        isa_mat = isa_mat,
        usedfor_mat = usedfor_mat)

@memory.cache
def make_isa_space():
    matrices = build_matrices()
    return SVDSpace.from_matrix(matrices['isa_mat'], K)

@memory.cache
def make_usedfor_space():
    matrices = build_matrices()
    return SVDSpace.from_matrix(matrices['usedfor_mat'], K)

@memory.cache
def make_summed_space():
    matrices = build_matrices()
    summed = matrices['isa_mat'] + matrices['usedfor_mat']
    return SVDSpace.from_matrix(summed, K)

@memory.cache
def make_merged_space():
    return make_isa_space().merged_with(make_usedfor_space())
    
def plot_singular_vector_alignment():
    u_dot_u = make_summed_space().u.T.dot(make_merged_space().u)

    from matplotlib import pyplot as plt
    plt.imshow(np.abs(u_dot_u))
    plt.show()

    return u_dot_u

def check_concept_angles():
    pairs = [
        ('dog', 'cat'),
        ('apple', 'banana'),
        ('umbrella', 'toaster'),
        ('table', 'europe')]

    sa = make_summed_space()
    ma = make_merged_space()
    for words in pairs:
        summed_vecs = [sa.u.row_named(word) for word in words]
        merged_vecs = [ma.u.row_named(word) for word in words]

        print '{}:{} summed: {:.4f} merged: {:.4f}'.format(
            words[0], words[1],
            summed_vecs[0].dot(summed_vecs[1]),
            merged_vecs[0].dot(merged_vecs[1]))

def check_nearby_concepts():
    N = 20
    seed = 0
    
    import random
    r = random.Random(seed)

    sa = make_summed_space()
    ma = make_merged_space()

    words = r.sample(sa.u.row_labels, N)
    summed_vecs = [sa.u.row_named(word) for word in words]
    merged_vecs = [ma.u.row_named(word) for word in words]

    def print_proximity_to(idx):
        summed_dots = [summed_vecs[idx].dot(vec) for vec in summed_vecs]
        sorted_summed_words = [word for _, word in sorted(zip(summed_dots, words))]

        merged_dots = [merged_vecs[idx].dot(vec) for vec in merged_vecs]
        sorted_merged_words = [word for _, word in sorted(zip(merged_dots, words))]

        print 'Proximity to {}:'.format(words[idx])
        print 'summed: ' + ', '.join(sorted_summed_words)
        print 'merged: ' + ', '.join(sorted_merged_words)

    print_proximity_to(0)
    print_proximity_to(1)

