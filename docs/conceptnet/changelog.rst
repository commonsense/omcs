Changelog
=========

ConceptNet 4.0rc4
-----------------
- The "num_assertions" and "score" fields should now update when new
  assertions are added to a database.
- In the database (released as ConceptNet-sqlite-4.0rc4.tar.gz), a
  number of very silly and unhelpful statements about people's names
  have been set to 0 score, and Japanese concepts now have their
  num_assertions set correctly.

ConceptNet 4.0rc3
-----------------
- Helper data for csc.nl, such as stopword lists, are now stored as
  text files instead of entries in the database. This allows most
  features of csc.nl to be used without access to a database.

ConceptNet 4.0rc2
-----------------

Major code changes:

* Made almost all of `csc.nl` work independently from the database, and only import the database settings if it absolutely needs to. This lets `csc.nl` work even when a different Django database is loaded.
* Added support for Hungarian using Snowball, in `csc.nl.hu`.
* Added experimental support for Japanese in `csc.nl.ja`, thanks to Tyson Roberts. This uses MeCab and CaboCha to tokenize and lemmatize Japanese text. This replaces the previous trivial `csc.nl.ja` module. Japanese concepts have not yet been updated, however.
* `csc.nl.euro` now contains methods for extracting relevant words and phrases from free text.

Database changes:

* Imported the Traditional Chinese ConceptNet (thanks to Yen-Ling Kuo).
* Corrected some common types of parsing errors, such as parsing "[X] is [for Y]" instead of "[X] is for [Y]". Some of these were introduced by Verbosity.
* Updated English concepts that disagreed with the lemmatizer.

The database schema has not changed, so the 4.0rc1 database should still work.

ConceptNet 4.0rc1
-----------------

Major code changes (since beta releases):

* Fixed the EOFError in `csc.nl` on Windows.
* The ConceptNet 4 models now live in `csc.conceptnet` instead of `csc.conceptnet4`. The old, unsupported `csc.conceptnet` (for ConceptNet 3) is now gone. `csc.conceptnet4` now contains bridging code that imports the correct things from csc.conceptnet, so your code will keep working.
* Added a database auto-downloader. Now, if you are missing a db_config.py file when you import csc.conceptnet.models, it will offer to download ConceptNet and set up db_config.py for you.
* Started to keep track of database migrations with South.
* Added the ConceptNet REST API.
* Added trivial support for Traditional Chinese. (`csc.nl.zh` exists, but it doesn't actually need to do anything.)

Database changes:

* Renamed many database tables to follow the Django conventions.
* Fixed the missing `functionclass_words` table in the SQLite database.
* Changed the Django ContentTypes to refer to `csc.conceptnet` models, not `csc.conceptnet4`.
* Imported data from Verbosity (thanks to Harshit Surana).

Older databases will **not** work with ConceptNet 4.0rc1 or later.

Older releases
--------------

Changelog summaries are not available for ConceptNet 4.0b11 and earlier releases, but you can look them up in the Bazaar log messages.

The defining changes between ConceptNet 3 and ConceptNet 4 were:

* Around ConceptNet 3.5, Predicates were renamed to Assertions and PredicateTypes were renamed to Relations.
* Stopped storing raw text in Assertions. Assertions are now abstracted edges of ConceptNet; RawAssertions express the actual relationships between texts; the text themselves are stored in SurfaceForms so that they can be indexed.
* Replaced the idea of "modality" with Frequency objects.
* Replaced the Rating system with the simpler `django-voting`.
* Removed the very confused, inconsistent "polarity" property from Assertions; it is now inferred from the Frequency.
* Assertions never flip polarity anymore. Assertions with different Frequencies are different Assertions.
* Added the HasA relation.
* Stopped using the Snowball stemmer in English, in favor of an MBLEM lemmatizer that can be run in reverse to generate text.
* Re-parsed all of the free text data according to the new rules.

