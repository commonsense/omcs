
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


.. function:: /api/{lang}/assertion/{id}/

    
    A GET request to this URL returns information about the Assertion with
    a particular ID.
    
    This ID will appear in URLs of other objects,
    such as RawAssertions, that refer to this Assertion.
    
    Implemented by: :class:`csc.webapi.AssertionHandler`

    
    
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
        score: 8
    
    

.. function:: /api/{lang}/concept/{concept}/

    
    A GET request to this URL will look up a Concept in ConceptNet.
    
    It may not be especially useful to use this query directly, as most of
    the information it gives you back is the information you needed to look it
    up in the first place. However, you can use this to test for a concept's
    existence, and this URL is a base for more interesting queries on concepts.
    
    Implemented by: :class:`csc.webapi.ConceptHandler`

    
    
    **Example:** `GET /api/en/concept/duck/query.yaml <http://openmind.media.mit.edu/api/en/concept/duck/query.yaml>`_ ::
    
        canonical_name: duck
        language: {id: en}
        resource_uri: /api/en/concept/duck/
        text: duck
    
    

.. function:: /api/{lang}/concept/{concept}/assertions/limit:{limit}/

    
    A GET request to this URL will look up all the
    :class:`Assertions <csc.conceptnet.models.Assertion>` that this
    Concept participates in with a score of at least 1.
    
    The results will be limited to the *n* highest-scoring assertions.
    By default, this limit is 20, but you can set it up to 100 by changing
    the *limit* in the URI.
    
    Implemented by: :class:`csc.webapi.ConceptAssertionHandler`

    
    
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
    
    

.. function:: /api/{lang}/concept/{concept}/features/

    
    A GET request to this URL will return a list of all existing
    :class:`Features <csc.conceptnet.models.Features>` built on the given
    :class:`Concept <csc.conceptnet.models.Concept>`.

    The features will be described in a short form: each feature will be a
    dictionary containing its *direction*, the *relation* involved, and the
    *resource_uri* for looking up more information about that feature. The
    concept will be omitted from each feature, because you already know it.
    
    Implemented by: :class:`csc.webapi.ConceptFeatureHandler`

    
    
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
    
    

.. function:: /api/{lang}/concept/{concept}/surfaceforms/limit:{limit}/

    
    A GET request to this URL will look up all the
    :class:`SurfaceForms <csc.conceptnet.models.SurfaceForm>` that
    correspond to this Concept -- that is, the phrases of natural language
    that are considered to reduce to this Concept.
    
    The results will be limited to *n* surface forms.
    By default, this limit is 20, but you can set it up to 100 by adding
    `limit:n/` to the URI.
    
    Implemented by: :class:`csc.webapi.ConceptSurfaceHandler`

    
    
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
    
    

.. function:: /api/{lang}/frame/{id}/

    
    A GET request to this URL will look up a sentence frame in a particular
    language, given its ID.
    
    This ID will appear in URLs of other objects,
    such as RawAssertions, that refer to this Frame.
    
    Implemented by: :class:`csc.webapi.FrameHandler`

    
    
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
    
    

.. function:: /api/{lang}/frame/{id}/statements/limit:{limit}/

    
    A GET request to this URL lists the RawAssertions that use a particular
    sentence frame, specified by its ID. As with other queries that return a
    list, this returns 20 results by default, but you can ask for up to 100
    by changing the value of *limit*.
    
    A POST request to this URL submits new knowledge to Open Mind. The
    POST parameters `text1` and `text2` specify the text that fills the blanks.
    
    You must either have a logged-in cookie or send `username` and
    `password` as additional parameters.
    
    Other optional parameters:
    * `activity`: a string identifying what activity or application this
      request is coming from.
    * `vote`: either 1 or -1. This will vote for or against the assertion after
      you create it, something you often want to do.
    
    Implemented by: :class:`csc.webapi.RawAssertionByFrameHandler`

    
    

.. function:: /api/{lang}/frequency/{text}/

    
    A GET request to this URL will look up a Frequency modifier by name in
    ConceptNet's natural language module. Each Frequency has a value from
    -10 to 10, so for example, you can use this to determine that
    the English modifier "sometimes" has a value of 4 in ConceptNet.
    
    Implemented by: :class:`csc.webapi.FrequencyHandler`

    
    
    **Example:** `GET /api/en/frequency/sometimes/query.yaml <http://openmind.media.mit.edu/api/en/frequency/sometimes/query.yaml>`_ ::
    
        language: {id: en}
        resource_uri: /api/en/frequency/sometimes/
        text: sometimes
        value: 4
    
    

.. function:: /api/{lang}/raw_assertion/{id}/

    
    A GET request to this URL returns information about the RawAssertion
    with a particular ID. This includes the Sentence and Assertion that it
    connects, if they exist.
    
    Implemented by: :class:`csc.webapi.RawAssertionHandler`

    
    
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
          score: 8
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
    
    

.. function:: /api/{lang}/surface/{text}/

    
    A GET request to this URL will look up a SurfaceForm in ConceptNet. The
    SurfaceForm must represent a phrase that someone has used at some point
    on ConceptNet.
    
    Implemented by: :class:`csc.webapi.SurfaceFormHandler`

    
    
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
    
    

.. function:: /api/{lang}/{dir}feature/{relation}/{concept}/limit:{limit}/

    
    A GET request to this URL will look up the
    :class:`Assertions <csc.conceptnet.models.Assertion>` that contain a
    certain :class:`Feature <csc.conceptnet.models.Feature>`.
    
    The parameter "{dir}feature" means that the URL should contain either
    `leftfeature/` or `rightfeature/`, depending on what form of feature
    you are looking for. See the :class:`Feature <csc.conceptnet.models.Feature>`
    documentation for more explanation.
    
    As with other queries that return a
    list, this returns 20 results by default, but you may ask for up to 100
    by changing the value of *limit*.
    
    Implemented by: :class:`csc.webapi.FeatureQueryHandler`

    
    
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
    
    Implemented by: :class:`csc.webapi.RatedObjectHandler`

    
    
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
          score: 8
        type: assertion
        votes:
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
        - user: {username: dab}
          vote: 1
    
    

