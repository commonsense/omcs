Layout of a Luminoso study
==========================

A Luminoso study is a directory, containing the following subdirectories:

- `Documents/`: This is where you put the free-text documents you want to
  analyze. They should be plain text files with the extension `.txt`.
- `Canonical/`: These are text files with the same form as the ones in
  `Documents/`, which will be used as canonical documents.
- `Matrices/`: This is where you put background knowledge to be blended in.
  These should be square Divisi2 sparse matrices, mapping concepts to other
  concepts, with the extension `.assoc.smat`. An example is the
  `conceptnet.assoc.smat` file that appears in every new study.
- `Results/`: This directory may be empty to begin with. After a study is
  analyzed, it will contain the results in various formats. See
  :doc:`/luminoso/power-users` for the details.
