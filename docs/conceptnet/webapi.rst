
.. _webapi:

The ConceptNet Web API
======================

You can look up information in ConceptNet using a Web-based API. The API
follows the `Representational State Transfer`_ (REST) standard, using simple
HTTP requests to interact with the server. (A prominent example of a REST API
is the `Twitter API`_.)

.. _`Representational State Transfer`: http://en.wikipedia.org/wiki/Representational_State_Transfer
.. _`Twitter API`: http://apiwiki.twitter.com/Twitter-API-Documentation

The URLs listed below are relative to the base URL of http://openmind.media.mit.edu. As an
example, you can use the command line utility cURL to see the results of the
`/api/en/concept/duck` call::

  curl http://openmind.media.mit.edu/api/en/concept/duck/

By the way, the excellent `django-piston`_ library made it much easier to write
this API, its documentation, and its examples, all at the same time.

.. _`django-piston`: http://bitbucket.org/jespern/django-piston/wiki/Home

If you want to quickly get started using this Web API in Python, go to the next
section, `webapi-client`_.

Output formats
--------------

When the API returns an object, it will represent it as a structure of key-value
mappings. This structure will, by default, be represented in JSON format.

You can request the results in a different format by adding "query.format" to
the end of a URL:

- Adding `query.xml` will request the results in XML format.
- Adding `query.json` will request the results in their default JSON format.
- Adding `query.yaml` will request the results in YAML_ format.
  
.. _YAML: http://yaml.org

For example, adding "query.xml" will request the results in XML format.

The examples shown below all use YAML format, because it is fairly readable and
the most compact of all these formats.

REST requests
-------------



UserHandler
.......................................

.. function:: /api/user/{username}/

    
    **Checking users**: A GET request to this URL will confirm whether a user
    exists. If the user exists, this returns a data structure containing their
    username. If the user does not exist, it returns a 404 response.

    **Creating users**: A POST request to this URL will create a user that does
    not already exist. This takes two additional POST parameters:

    - `password`: The password the new user should have.
    - `email`: (Optional and not very important) The e-mail address to be
      associated with the user in the database.

    Do not use high-security passwords here. You're sending them over plain
    HTTP, so they are not encrypted.
    
    Implemented by: :class:`conceptnet.webapi.UserHandler`

    
    
    **Example:** `GET /api/user/verbosity/query.yaml <http://openmind.media.mit.edu/api/user/verbosity/query.yaml>`_ ::
    
        {username: verbosity}
    
    


LanguageHandler
.......................................

.. function:: /api/{lang}/

    
    A GET request to this URL will show basic information about a language --
    its ID and how many sentences (parsed or unparsed) exist in the database
    for that language.

    The sentence count is a cached value. It might become out of sync with the
    actual number of sentences, but it's not supposed to.
    
    Implemented by: :class:`conceptnet.webapi.LanguageHandler`

    
    
    **Example:** `GET /api/ja/query.yaml <http://openmind.media.mit.edu/api/ja/query.yaml>`_ ::
    
        {id: ja, sentence_count: 14540}
    
    


AssertionHandler
.......................................

.. function:: /api/{lang}/assertion/{id}/

    
    A GET request to this URL returns information about the Assertion with
    a particular ID.
    
    This ID will appear in URLs of other objects,
    such as RawAssertions, that refer to this Assertion.
    
    Implemented by: :class:`conceptnet.webapi.AssertionHandler`

    
    
    **Example:** `GET /api/en/assertion/25/query.yaml <http://openmind.media.mit.edu/api/en/assertion/25/query.yaml>`_ ::
    
        concept1:
          canonical_name: go to a concert
          language: {id: en}
          resource_uri: /api/en/concept/go%20concert/
          text: go concert
        concept2:
          canonical_name: hearing music
          language: {id: en}
          resource_uri: /api/en/concept/hear%20music/
          text: hear music
        frequency:
          language: {id: en}
          resource_uri: /api/en/frequency//
          text: ''
          value: 5
        language: {id: en}
        relation: {name: HasSubevent}
        resource_uri: /api/en/assertion/25/
        score: 9
    
    


AssertionToRawHandler
.......................................

.. function:: /api/{lang}/assertion/{id}/raw/

    
    A GET request to this URL will list the RawAssertions (natural language
    statements) associated with a given Assertion ID.
    
    Implemented by: :class:`conceptnet.webapi.AssertionToRawHandler`

    
    
    **Example:** `GET /api/en/assertion/31445/raw/query.yaml <http://openmind.media.mit.edu/api/en/assertion/31445/raw/query.yaml>`_ ::
    
        - assertion:
            concept1:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            concept2:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/assertion/31445/
            score: 21
          created: 2009-03-12 07:39:58.485641
          creator: {username: infovore}
          frame:
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            goodness: 2
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/frame/90/
            text: '{1} can be used to {2}'
          language: {id: en}
          resource_uri: /api/en/raw_assertion/223329/
          score: 16
          sentence:
            created_on: 2006-11-14 17:38:29.661909
            creator: {username: infovore}
            language: {id: en}
            score: 11
            text: A computer can be used to play games.
          surface1:
            concept:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            language: {id: en}
            residue: a 1
            resource_uri: /api/en/surface/A%20computer/
            text: A computer
          surface2:
            concept:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            language: {id: en}
            residue: 1 2s
            resource_uri: /api/en/surface/play%20games/
            text: play games
          updated: 2010-08-16 11:32:46.755767
        - assertion:
            concept1:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            concept2:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/assertion/31445/
            score: 21
          created: 2009-03-11 21:33:53.941539
          creator: {username: jradoff}
          frame:
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            goodness: 2
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/frame/90/
            text: '{1} can be used to {2}'
          language: {id: en}
          resource_uri: /api/en/raw_assertion/85931/
          score: 2
          sentence:
            created_on: 2006-11-14 16:06:57.129833
            creator: {username: jradoff}
            language: {id: en}
            score: 1
            text: Computers can be used to play games
          surface1:
            concept:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            language: {id: en}
            residue: 1s
            resource_uri: /api/en/surface/Computers/
            text: Computers
          surface2:
            concept:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            language: {id: en}
            residue: 1 2s
            resource_uri: /api/en/surface/play%20games/
            text: play games
          updated: 2010-04-21 21:52:27.157557
        - assertion:
            concept1:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            concept2:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/assertion/31445/
            score: 21
          created: 2009-03-11 18:43:07.429866
          creator: {username: Chriki}
          frame:
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            goodness: 2
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/frame/4/
            text: You can use {1} to {2}
          language: {id: en}
          resource_uri: /api/en/raw_assertion/33432/
          score: 2
          sentence:
            created_on: 2006-11-14 15:32:32.050252
            creator: {username: Chriki}
            language: {id: en}
            score: 1
            text: You can use a computer to play games.
          surface1:
            concept:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            language: {id: en}
            residue: a 1
            resource_uri: /api/en/surface/a%20computer/
            text: a computer
          surface2:
            concept:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            language: {id: en}
            residue: 1 2s
            resource_uri: /api/en/surface/play%20games/
            text: play games
          updated: 2010-04-21 23:17:28.934516
        - assertion:
            concept1:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            concept2:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/assertion/31445/
            score: 21
          created: 2009-03-12 02:44:06.656549
          creator: {username: Surgchen}
          frame:
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            goodness: 3
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/frame/7/
            text: '{1} is for {2}'
          language: {id: en}
          resource_uri: /api/en/raw_assertion/163934/
          score: 1
          sentence:
            created_on: 2006-11-14 16:53:44.325891
            creator: {username: Surgchen}
            language: {id: en}
            score: 1
            text: a computer is for playing games
          surface1:
            concept:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            language: {id: en}
            residue: a 1
            resource_uri: /api/en/surface/a%20computer/
            text: a computer
          surface2:
            concept:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            language: {id: en}
            residue: 1'ing 2s
            resource_uri: /api/en/surface/playing%20games/
            text: playing games
          updated: 2009-12-03 09:35:58.763571
        - assertion:
            concept1:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            concept2:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/assertion/31445/
            score: 21
          created: 2009-03-12 01:39:23.581455
          creator: {username: hanta007}
          frame:
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            goodness: 2
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/frame/8/
            text: '{1} is used for {2}'
          language: {id: en}
          resource_uri: /api/en/raw_assertion/149058/
          score: 1
          sentence:
            created_on: 2006-11-14 16:42:50.858692
            creator: {username: hanta007}
            language: {id: en}
            score: 1
            text: a computer is used for playing games
          surface1:
            concept:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            language: {id: en}
            residue: a 1
            resource_uri: /api/en/surface/a%20computer/
            text: a computer
          surface2:
            concept:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            language: {id: en}
            residue: 1'ing 2s
            resource_uri: /api/en/surface/playing%20games/
            text: playing games
          updated: 2009-12-03 05:46:13.115839
        - assertion:
            concept1:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            concept2:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/assertion/31445/
            score: 21
          created: 2010-02-16 19:42:42.007318
          creator: {username: puga}
          frame:
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            goodness: 3
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/frame/7/
            text: '{1} is for {2}'
          language: {id: en}
          resource_uri: /api/en/raw_assertion/1284488/
          score: 1
          sentence:
            created_on: 2010-02-16 19:42:44.207263
            creator: {username: puga}
            language: {id: en}
            score: 1
            text: computer is for play games
          surface1:
            concept:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            language: {id: en}
            residue: '1'
            resource_uri: /api/en/surface/computer/
            text: computer
          surface2:
            concept:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            language: {id: en}
            residue: 1 2s
            resource_uri: /api/en/surface/play%20games/
            text: play games
          updated: 2010-02-16 19:42:45.829579
        - assertion:
            concept1:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            concept2:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/assertion/31445/
            score: 21
          created: 2009-04-14 21:09:56.440264
          creator: {username: openmind}
          frame:
            frequency:
              language: {id: en}
              resource_uri: /api/en/frequency//
              text: ''
              value: 5
            goodness: 2
            language: {id: en}
            relation: {name: UsedFor}
            resource_uri: /api/en/frame/90/
            text: '{1} can be used to {2}'
          language: {id: en}
          resource_uri: /api/en/raw_assertion/544683/
          score: 1
          sentence:
            created_on: 2009-04-14 21:09:56.521981
            creator: {username: openmind}
            language: {id: en}
            score: 1
            text: computers can be used to play games
          surface1:
            concept:
              canonical_name: a computer
              language: {id: en}
              resource_uri: /api/en/concept/computer/
              text: computer
            language: {id: en}
            residue: 1s
            resource_uri: /api/en/surface/computers/
            text: computers
          surface2:
            concept:
              canonical_name: play a game
              language: {id: en}
              resource_uri: /api/en/concept/play%20game/
              text: play game
            language: {id: en}
            residue: 1 2s
            resource_uri: /api/en/surface/play%20games/
            text: play games
          updated: 2009-12-03 15:14:18.291844
    
    


AssertionFindHandler
.......................................

.. function:: /api/{lang}/assertionfind/{relation}/{text1}/{text2}/

    
    A GET request to this URL will return an Assertion
    given the text of its two concepts and its relation.

    - `relation` is the name of the relation.
    - `text1` is the text of the first concept.
    - `text2` is the text of the second concept.
    
    The concept text can actually be any surface form that normalizes to that
    concept.

    If such an assertion exists, it will be returned. If not, you will get a
    404 response. You can use this to find out whether the assertion exists or
    not.
    
    Implemented by: :class:`conceptnet.webapi.AssertionFindHandler`

    
    
    **Example:** `GET /api/en/assertionfind/IsA/dog/animal/query.yaml <http://openmind.media.mit.edu/api/en/assertionfind/IsA/dog/animal/query.yaml>`_ ::
    
        - concept1:
            canonical_name: a dog
            language: {id: en}
            resource_uri: /api/en/concept/dog/
            text: dog
          concept2:
            canonical_name: animals
            language: {id: en}
            resource_uri: /api/en/concept/animal/
            text: animal
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: IsA}
          resource_uri: /api/en/assertion/382591/
          score: 12
    
    


ConceptHandler
.......................................

.. function:: /api/{lang}/concept/{concept}/

    
    A GET request to this URL will look up a Concept in ConceptNet.
    
    It may not be especially useful to use this query directly, as most of
    the information it gives you back is the information you needed to look it
    up in the first place. However, you can use this to test for a concept's
    existence, and this URL is a base for more interesting queries on concepts.
    
    Implemented by: :class:`conceptnet.webapi.ConceptHandler`

    
    
    **Example:** `GET /api/en/concept/duck/query.yaml <http://openmind.media.mit.edu/api/en/concept/duck/query.yaml>`_ ::
    
        canonical_name: duck
        language: {id: en}
        resource_uri: /api/en/concept/duck/
        text: duck
    
    


ConceptAssertionHandler
.......................................

.. function:: /api/{lang}/concept/{concept}/assertions/limit:{limit}/

    
    A GET request to this URL will look up all the
    :class:`Assertions <conceptnet.models.Assertion>` that this
    Concept participates in with a score of at least 1.
    
    The results will be limited to the *n* highest-scoring assertions.
    By default, this limit is 20, but you can set it up to 100 by changing
    the *limit* in the URL.
    
    Implemented by: :class:`conceptnet.webapi.ConceptAssertionHandler`

    
    
    **Example:** `GET /api/en/concept/web%20foot/assertions/limit:5/query.yaml <http://openmind.media.mit.edu/api/en/concept/web%20foot/assertions/limit:5/query.yaml>`_ ::
    
        - concept1:
            canonical_name: duck
            language: {id: en}
            resource_uri: /api/en/concept/duck/
            text: duck
          concept2:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: HasA}
          resource_uri: /api/en/assertion/75224/
          score: 7
        - concept1:
            canonical_name: a waterfowl
            language: {id: en}
            resource_uri: /api/en/concept/waterfowl/
            text: waterfowl
          concept2:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: HasA}
          resource_uri: /api/en/assertion/76465/
          score: 1
        - concept1:
            canonical_name: duck
            language: {id: en}
            resource_uri: /api/en/concept/duck/
            text: duck
          concept2:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: IsA}
          resource_uri: /api/en/assertion/699417/
          score: 1
        - concept1:
            canonical_name: penquin
            language: {id: en}
            resource_uri: /api/en/concept/penquin/
            text: penquin
          concept2:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: HasA}
          resource_uri: /api/en/assertion/101343/
          score: 1
        - concept1:
            canonical_name: duck
            language: {id: en}
            resource_uri: /api/en/concept/duck/
            text: duck
          concept2:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: HasProperty}
          resource_uri: /api/en/assertion/641891/
          score: 1
    
    


ConceptFeatureHandler
.......................................

.. function:: /api/{lang}/concept/{concept}/features/

    
    A GET request to this URL will return a list of all existing
    :class:`Features <conceptnet.models.Features>` built on the given
    :class:`Concept <conceptnet.models.Concept>`.

    The features will be described in a short form: each feature will be a
    dictionary containing its *direction*, the *relation* involved, and the
    *resource_uri* for looking up more information about that feature. The
    concept will be omitted from each feature, because you already know it.
    
    Implemented by: :class:`conceptnet.webapi.ConceptFeatureHandler`

    
    
    **Example:** `GET /api/en/concept/moose/features/query.yaml <http://openmind.media.mit.edu/api/en/concept/moose/features/query.yaml>`_ ::
    
        - direction: left
          relation: {name: IsA}
          resource_uri: /api/en/leftfeature/IsA/moose/
        - direction: left
          relation: {name: AtLocation}
          resource_uri: /api/en/leftfeature/AtLocation/moose/
        - direction: left
          relation: {name: UsedFor}
          resource_uri: /api/en/leftfeature/UsedFor/moose/
        - direction: left
          relation: {name: ConceptuallyRelatedTo}
          resource_uri: /api/en/leftfeature/ConceptuallyRelatedTo/moose/
        - direction: left
          relation: {name: HasA}
          resource_uri: /api/en/leftfeature/HasA/moose/
        - direction: left
          relation: {name: HasProperty}
          resource_uri: /api/en/leftfeature/HasProperty/moose/
        - direction: left
          relation: {name: LocatedNear}
          resource_uri: /api/en/leftfeature/LocatedNear/moose/
        - direction: left
          relation: {name: SimilarSize}
          resource_uri: /api/en/leftfeature/SimilarSize/moose/
        - direction: right
          relation: {name: IsA}
          resource_uri: /api/en/rightfeature/IsA/moose/
        - direction: right
          relation: {name: AtLocation}
          resource_uri: /api/en/rightfeature/AtLocation/moose/
        - direction: right
          relation: {name: ConceptuallyRelatedTo}
          resource_uri: /api/en/rightfeature/ConceptuallyRelatedTo/moose/
        - direction: right
          relation: {name: PartOf}
          resource_uri: /api/en/rightfeature/PartOf/moose/
        - direction: right
          relation: {name: LocatedNear}
          resource_uri: /api/en/rightfeature/LocatedNear/moose/
    
    


ConceptSurfaceHandler
.......................................

.. function:: /api/{lang}/concept/{concept}/surfaceforms/limit:{limit}/

    
    A GET request to this URL will look up all the
    :class:`SurfaceForms <conceptnet.models.SurfaceForm>` that
    correspond to this Concept -- that is, the phrases of natural language
    that are considered to reduce to this Concept.
    
    The results will be limited to *n* surface forms.
    By default, this limit is 20, but you can set it up to 100 by adding
    `limit:n/` to the URI.
    
    Implemented by: :class:`conceptnet.webapi.ConceptSurfaceHandler`

    
    
    **Example:** `GET /api/en/concept/web%20foot/surfaceforms/limit:5/query.yaml <http://openmind.media.mit.edu/api/en/concept/web%20foot/surfaceforms/limit:5/query.yaml>`_ ::
    
        - concept:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          language: {id: en}
          residue: 1ed 2s
          resource_uri: /api/en/surface/webbed%20feet/
          text: webbed feet
        - concept:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          language: {id: en}
          residue: 1 2s
          resource_uri: /api/en/surface/web%20feet/
          text: web feet
        - concept:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          language: {id: en}
          residue: 1ed 2ed
          resource_uri: /api/en/surface/webbed%20footed/
          text: webbed footed
        - concept:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          language: {id: en}
          residue: have 1ed 2s
          resource_uri: /api/en/surface/have%20webbed%20feet/
          text: have webbed feet
    
    


FrameHandler
.......................................

.. function:: /api/{lang}/frame/{id}/

    
    A GET request to this URL will look up a sentence frame in a particular
    language, given its ID.
    
    This ID will appear in URLs of other objects,
    such as RawAssertions, that refer to this Frame.
    
    Implemented by: :class:`conceptnet.webapi.FrameHandler`

    
    
    **Example:** `GET /api/en/frame/7/query.yaml <http://openmind.media.mit.edu/api/en/frame/7/query.yaml>`_ ::
    
        frequency:
          language: {id: en}
          resource_uri: /api/en/frequency//
          text: ''
          value: 5
        goodness: 3
        language: {id: en}
        relation: {name: UsedFor}
        resource_uri: /api/en/frame/7/
        text: '{1} is for {2}'
    
    


RawAssertionByFrameHandler
.......................................

.. function:: /api/{lang}/frame/{id}/statements/limit:{limit}/

    
    **Getting assertions**: A GET request to this URL lists the RawAssertions
    that use a particular
    sentence frame, specified by its ID. As with other queries that return a
    list, this returns 20 results by default, but you can ask for up to 100
    by changing the value of *limit*.
    
    **Adding assertions**: A POST request to this URL submits new knowledge to
    Open Mind. The
    POST parameters `text1` and `text2` specify the text that fills the blanks.
    
    You must either have a logged-in cookie or send `username` and
    `password` as additional parameters.
    
    Other optional parameters:

    - `activity`: a string identifying what activity or application this
      request is coming from.
    - `vote`: either 1 or -1. This will vote for or against the assertion after
      you create it, something you often want to do.
    
    Implemented by: :class:`conceptnet.webapi.RawAssertionByFrameHandler`

    
    


FrequencyHandler
.......................................

.. function:: /api/{lang}/frequency/{text}/

    
    A GET request to this URL will look up a Frequency modifier by name in
    ConceptNet's natural language module. Each Frequency has a value from
    -10 to 10, so for example, you can use this to determine that
    the English modifier "sometimes" has a value of 4 in ConceptNet.
    
    Implemented by: :class:`conceptnet.webapi.FrequencyHandler`

    
    
    **Example:** `GET /api/en/frequency/sometimes/query.yaml <http://openmind.media.mit.edu/api/en/frequency/sometimes/query.yaml>`_ ::
    
        language: {id: en}
        resource_uri: /api/en/frequency/sometimes/
        text: sometimes
        value: 4
    
    


RawAssertionHandler
.......................................

.. function:: /api/{lang}/raw_assertion/{id}/

    
    A GET request to this URL returns information about the RawAssertion
    with a particular ID. This includes the Sentence and Assertion that it
    connects, if they exist.
    
    Implemented by: :class:`conceptnet.webapi.RawAssertionHandler`

    
    
    **Example:** `GET /api/en/raw_assertion/26/query.yaml <http://openmind.media.mit.edu/api/en/raw_assertion/26/query.yaml>`_ ::
    
        assertion:
          concept1:
            canonical_name: go to a concert
            language: {id: en}
            resource_uri: /api/en/concept/go%20concert/
            text: go concert
          concept2:
            canonical_name: hearing music
            language: {id: en}
            resource_uri: /api/en/concept/hear%20music/
            text: hear music
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: HasSubevent}
          resource_uri: /api/en/assertion/25/
          score: 9
        created: 2009-03-11 14:59:35.901858
        creator: {username: MrMcGibby}
        frame:
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          goodness: 2
          language: {id: en}
          relation: {name: HasSubevent}
          resource_uri: /api/en/frame/19/
          text: Something that might happen while {1} is {2}
        language: {id: en}
        resource_uri: /api/en/raw_assertion/26/
        score: 1
        sentence:
          created_on: 2006-11-14 15:32:37.087072
          creator: {username: MrMcGibby}
          language: {id: en}
          score: 1
          text: Something that might happen while going to a concert is hear music
        surface1:
          concept:
            canonical_name: go to a concert
            language: {id: en}
            resource_uri: /api/en/concept/go%20concert/
            text: go concert
          language: {id: en}
          residue: 1'ing to a 2
          resource_uri: /api/en/surface/going%20to%20a%20concert/
          text: going to a concert
        surface2:
          concept:
            canonical_name: hearing music
            language: {id: en}
            resource_uri: /api/en/concept/hear%20music/
            text: hear music
          language: {id: en}
          residue: 1 2
          resource_uri: /api/en/surface/hear%20music/
          text: hear music
        updated: 2009-12-03 05:09:18.677617
    
    


SurfaceFormHandler
.......................................

.. function:: /api/{lang}/surface/{text}/

    
    A GET request to this URL will look up a SurfaceForm in ConceptNet. The
    SurfaceForm must represent a phrase that someone has used at some point
    on ConceptNet.
    
    Implemented by: :class:`conceptnet.webapi.SurfaceFormHandler`

    
    
    **Example:** `GET /api/en/surface/have%20webbed%20feet/query.yaml <http://openmind.media.mit.edu/api/en/surface/have%20webbed%20feet/query.yaml>`_ ::
    
        concept:
          canonical_name: webbed feet
          language: {id: en}
          resource_uri: /api/en/concept/web%20foot/
          text: web foot
        language: {id: en}
        residue: have 1ed 2s
        resource_uri: /api/en/surface/have%20webbed%20feet/
        text: have webbed feet
    
    


FeatureQueryHandler
.......................................

.. function:: /api/{lang}/{dir}feature/{relation}/{concept}/limit:{limit}/

    
    A GET request to this URL will look up the
    :class:`Assertions <conceptnet.models.Assertion>` that contain a
    certain :class:`Feature <conceptnet.models.Feature>`.
    
    The parameter "{dir}feature" means that the URL should contain either
    `leftfeature/` or `rightfeature/`, depending on what form of feature
    you are looking for. See the :class:`Feature <conceptnet.models.Feature>`
    documentation for more explanation.
    
    As with other queries that return a
    list, this returns 20 results by default, but you may ask for up to 100
    by changing the value of *limit*.
    
    Implemented by: :class:`conceptnet.webapi.FeatureQueryHandler`

    
    
    **Example:** `GET /api/en/rightfeature/HasA/web%20foot/limit:5/query.yaml <http://openmind.media.mit.edu/api/en/rightfeature/HasA/web%20foot/limit:5/query.yaml>`_ ::
    
        - concept1:
            canonical_name: duck
            language: {id: en}
            resource_uri: /api/en/concept/duck/
            text: duck
          concept2:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: HasA}
          resource_uri: /api/en/assertion/75224/
          score: 7
        - concept1:
            canonical_name: a waterfowl
            language: {id: en}
            resource_uri: /api/en/concept/waterfowl/
            text: waterfowl
          concept2:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: HasA}
          resource_uri: /api/en/assertion/76465/
          score: 1
        - concept1:
            canonical_name: penquin
            language: {id: en}
            resource_uri: /api/en/concept/penquin/
            text: penquin
          concept2:
            canonical_name: webbed feet
            language: {id: en}
            resource_uri: /api/en/concept/web%20foot/
            text: web foot
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: HasA}
          resource_uri: /api/en/assertion/101343/
          score: 1
    
    


RatedObjectHandler
.......................................

.. function:: /api/{lang}/{type}/{id}/votes/

    
    A GET request to this URL will look up an object that can be voted on
    by users, and show how users have voted on it.
    
    The "type" parameter should either be 'assertion', 'raw_assertion', or
    'sentence', and the "id" should be an object's ID within that type.
    
    This request will return a structure containing the object itself, its
    type, and its list of votes.
    
    A POST request to this URL lets you vote on the object, by supplying
    the parameter `vote` with a value of 1 or -1. You must either have a
    logged-in cookie or send `username` and `password` as additional parameters.
    
    Other optional parameters:
    
    * `activity`: a string identifying what activity or application this
      request is coming from.
    
    Implemented by: :class:`conceptnet.webapi.RatedObjectHandler`

    
    
    **Example:** `GET /api/en/assertion/25/votes/query.yaml <http://openmind.media.mit.edu/api/en/assertion/25/votes/query.yaml>`_ ::
    
        assertion:
          concept1:
            canonical_name: go to a concert
            language: {id: en}
            resource_uri: /api/en/concept/go%20concert/
            text: go concert
          concept2:
            canonical_name: hearing music
            language: {id: en}
            resource_uri: /api/en/concept/hear%20music/
            text: hear music
          frequency:
            language: {id: en}
            resource_uri: /api/en/frequency//
            text: ''
            value: 5
          language: {id: en}
          relation: {name: HasSubevent}
          resource_uri: /api/en/assertion/25/
          score: 9
        type: assertion
        votes:
        - user: {username: PaoloM}
          vote: 1
        - user: {username: dab}
          vote: 1
        - user: {username: rspeer}
          vote: 1
        - user: {username: MrMcGibby}
          vote: 1
        - user: {username: manauser}
          vote: 1
        - user: {username: RogierBrussee}
          vote: 1
        - user: {username: dopefishdave}
          vote: 1
        - user: {username: glennlee}
          vote: 1
        - user: {username: skoerber}
          vote: 1
    
    
SimilarityHandler
.......................................

.. function:: /api/{lang}/similar_to/{termlist}/limit:{limit}/

    
    A GET request to this URL will take in a comma-separated list of concept
    names, and return a list of concepts that are the most similar.
    The concept names can have underscores that are translated
    to spaces, and @ signs that indicate a weight. For example:

        /api/en/similar_to/dog,cat,mouse@0.5,guinea_pig/limit:10
    
    The first argument is the language, and the second argument is the list
    of terms. The language must currently be 'en'.
    
    Implemented by: :class:`conceptnet.webapi.SimilarityHandler`

    
    
    **Example:** `GET /api/en/similar_to/dog,cat,mouse@0.5,guinea_pig/limit:10/query.yaml <http://openmind.media.mit.edu/api/en/similar_to/dog,cat,mouse@0.5,guinea_pig/limit:5/query.yaml>`_ ::
    
        - concept:
            canonical_name: a cat
            language: {id: en}
            resource_uri: /api/en/concept/cat/
            text: cat
          score: 3.4199635478331318
        - concept:
            canonical_name: a dog
            language: {id: en}
            resource_uri: /api/en/concept/dog/
            text: dog
          score: 3.381817053975718
        - concept:
            canonical_name: a tabby cat
            language: {id: en}
            resource_uri: /api/en/concept/tabby%20cat/
            text: tabby cat
          score: 3.3789687864846085
        - concept:
            canonical_name: a kitten
            language: {id: en}
            resource_uri: /api/en/concept/kitten/
            text: kitten
          score: 3.3779517430787402
        - concept:
            canonical_name: Guinea pigs
            language: {id: en}
            resource_uri: /api/en/concept/guinea%20pig/
            text: guinea pig
          score: 3.3541297786211377
