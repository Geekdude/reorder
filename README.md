# Reorder

Script to rename, reorder, add, and remove files in a directory with a numerical naming scheme.

## Installation
Copy `reorder.py` to `~/bin` or some other folder in your `$PATH`. Optionally you can rename the file `reorder`.

    $ cp reorder.py ~/bin/reorder

## Usage
    usage: reorder [-h] [-a] [-n] [-v] directory

    Script to rename, reorder, add, and remove files in a directory with a
    numerical naming scheme. Run the program and provide a directory with the
    numbered files. A text buffer will be opened with the current files in the
    folder. Reorder, rename, add, or delete files in the buffer. Do not change the
    numbered part of the filename, these numbers will be recalculated and are used
    to match renamed files. Save and exit the editor. Then the program with
    perform the operations to the files in the directory. To cancel the operation,
    save an empty buffer.

    positional arguments:
    directory      The target directory

    optional arguments:
    -h, --help     show this help message and exit
    -a, --add      Add unnumbered files to numbering
    -n, --nono     Do not make changes
    -v, --verbose  Verbose output

## Examples
Say I had the following directory:

    chapters/
    ├── conclusion.tex
    ├── first_topic.tex
    ├── future_work.tex
    ├── introduction.tex
    └── second_topic.tex

To rename the files using a numerical numbering scheme I can run `reorder -a chapters`.
I am then presented with the buffer:

    conclusion.tex
    first_topic.tex
    future_work.tex
    introduction.tex
    second_topic.tex

I then change the buffer to 

    introduction.tex
    first_topic.tex
    second_topic.tex
    future_work.tex
    conclusion.tex

save and exit.

The directory now looks like:

    chapters/
    ├── 01_introduction.tex
    ├── 02_first_topic.tex
    ├── 03_second_topic.tex
    ├── 04_future_work.tex
    └── 05_conclusion.tex

Lets say I now want to delete the future work chapter, add an abstract, and reorder the first and second topic.
First launch the reorder program again with `reorder chapters`. I am presented with the buffer:

    01_introduction.tex
    02_first_topic.tex
    03_second_topic.tex
    04_future_work.tex
    05_conclusion.tex

I then change the buffer to

    abstract.tex
    01_introduction.tex
    03_second_topic.tex
    02_first_topic.tex
    05_conclusion.tex

save and exit.
The directory now looks like:

    chapters
    ├── 01_abstract.tex
    ├── 02_introduction.tex
    ├── 03_second_topic.tex
    ├── 04_first_topic.tex
    └── 05_conclusion.tex
