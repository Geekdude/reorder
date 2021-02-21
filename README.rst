*******
reorder
*******

Script to rename, reorder, add, and remove files/directories in a directory with a numerical naming scheme.

Prerequisites
=============

Python 3.6 or newer is required to run the script.

Installation
============
Copy ``reorder.py`` to ``~/bin`` or some other folder in your ``$PATH``. Optionally you can rename the file ``reorder``.

.. code:: console

    $ cp reorder.py ~/bin/reorder

Usage
=====

.. code:: console

    usage: reorder [-h] [-a] [-n] [-v] [-d] [-f FORM] [-u] [-l FILTER]
                [-s {none,-,_, }]
                directory

    Script to rename, reorder, add, and remove files/directories in a directory
    with a numerical naming scheme. Run the program and provide a directory with
    the numbered files/directories. A text buffer will be opened with the current
    files/directories in the folder using the editor specified by the EDITOR
    environment variable. If EDITOR is not set, Vim will be used by default.
    Reorder, rename, add, or delete files in the buffer. Do not change the
    numbered part of the file/directory name; these numbers will be recalculated
    and are used to match renamed files/directories. Save and exit the editor.
    Then the program with perform the operations to the files/directories in the
    directory. To cancel the operation, save an empty buffer.

    positional arguments:
    directory             The target directory

    optional arguments:
    -h, --help            show this help message and exit
    -a, --add             Add unnumbered files to numbering
    -n, --nono            Do not make changes
    -v, --verbose         Verbose output
    -d, --directory       Operate on directories instead of files
    -f FORM, --format FORM
                            Number of leading 0
    -u, --update          Force rename all files
    -l FILTER, --filter FILTER
                            Filter string for files/directories. This is
                            represented as a single string containing a space-
                            separated list of filters operated on with logical or
    -s {none,-,_, }, --separator {none,-,_, }
                            Character to separate the number from the
                            file/directory name. The none option will either
                            choose whatever is already used in the directory or
                            default to _

Acknowledgements
================

Thank you to Jonathan Ambrose who helped come up with the idea for the script and added several additional features to the script.
