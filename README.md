# Reorder

Script to rename, reorder, add, and remove files/directories in a directory with a numerical naming scheme.

## Installation
Copy `reorder.py` to `~/bin` or some other folder in your `$PATH`. Optionally you can rename the file `reorder`.

    $ cp reorder.py ~/bin/reorder

## Usage

    usage: reorder [-h] [-a] [-n] [-v] [-d] [-f FORM] [-u] [-l FILTER]
                   [-s {none,-,_, }]
                   directory

    Script to rename, reorder, add, and remove files/directories in a directory
    with a numerical naming scheme. Run the program and provide a directory with
    the numbered files/directories. A text buffer will be opened with the current
    files/directories in the folder. Reorder, rename, add, or delete files in the
    buffer. Do not change the numbered part of the file/directory name, these
    numbers will be recalculated and are used to match renamed files/directories.
    Save and exit the editor. Then the program with perform the operations to the
    files/directories in the directory. To cancel the operation, save an empty
    buffer.

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
    ├── 1_introduction.tex
    ├── 2_first_topic.tex
    ├── 3_second_topic.tex
    ├── 4_future_work.tex
    └── 5_conclusion.tex

Lets say I now want to delete the future work chapter, add an abstract, and reorder the first and second topic.
First launch the reorder program again with `reorder chapters`. I am presented with the buffer:

    1_introduction.tex
    2_first_topic.tex
    3_second_topic.tex
    4_future_work.tex
    5_conclusion.tex

I then change the buffer to

    abstract.tex
    1_introduction.tex
    3_second_topic.tex
    2_first_topic.tex
    5_conclusion.tex

save and exit.
The directory now looks like:

    chapters
    ├── 1_abstract.tex
    ├── 2_introduction.tex
    ├── 3_second_topic.tex
    ├── 4_first_topic.tex
    └── 5_conclusion.tex

By default, the minimum number of leading 0's is used, so in the case above, I use no leading 0's.
Suppose I would like a number width field of 2 for the leading number.
I run `reorder -f 2 chapters` and am presented with the buffer:

    1_abstract.tex
    2_introduction.tex
    3_second_topic.tex
    4_first_topic.tex
    5_conclusion.tex

I then change the buffer to

    1_abstract.tex
    2_introduction.tex
    4_first_topic.tex
    3_second_topic.tex
    5_conclusion.tex

save and exit.
The directory now looks like:

    chapters
    ├── 1_abstract.tex
    ├── 2_introduction.tex
    ├── 03_first_topic.tex
    ├── 04_second_topic.tex
    └── 5_conclusion.tex

But wait. Why didn't `1_abstact.tex`, `2_introduction.tex`, and `5_conclusion.tex`  get changed to use 2 digits?
This happens because only renamed and added files are updated to use this number of digits.
If I want to force update all files, I can run `reorder -u -f 2 chapters` and I'll be presented with the buffer:

    1_abstract.tex
    2_introduction.tex
    03_first_topic.tex
    04_second_topic.tex
    5_conclusion.tex

I then simply save and exit.
The directory now looks like:

    chapters
    ├── 01_abstract.tex
    ├── 02_introduction.tex
    ├── 03_first_topic.tex
    ├── 04_second_topic.tex
    └── 05_conclusion.tex

By default, the separator already used for files in a given directory is used.
If no files are already numbered, `_` is used to separate the number from the filename.
Say I wanted to change the separator to use `-` instead of `_`.
I run the command `reorder -f 2 -u -s - chapters`. I am presented with this buffer

    01_abstract.tex
    02_introduction.tex
    03_first_topic.tex
    04_second_topic.tex
    05_conclusion.tex

I then simply save and exit.
The directory now looks like:

    chapters
    ├── 01-abstract.tex
    ├── 02-introduction.tex
    ├── 03-first_topic.tex
    ├── 04-second_topic.tex
    └── 05-conclusion.tex

It's worth noting that the `-f 2` is still required to maintain that formatting.  

Let's say I now have a more complex directory that looks like:

    dir
    ├── a.png
    ├── b.png
    ├── c.png
    ├── new.txt
    ├── temp.txt
    └── y.jpg

Perhaps I only want to number the `*.png` files, so the `-a` flag by itself will not help us.
If I want to do this operation, I run `reorder -al png dir`.
I am presented with the following buffer:

    a.png
    b.png
    c.png

I simply save and exit.
The directory now looks like:

    dir
    ├── 1_a.png
    ├── 2_b.png
    ├── 3_c.png
    ├── new.txt
    ├── temp.txt
    └── y.jpg

Now I've decided that I really meant to number all the pictures, which includes the `*.png` files and the `*.jpg` files.
To do this, I run `reorder -al "png jpg" dir`.
I am presented with the following buffer:

    1_a.png
    2_b.png
    3_c.png
    y.jpg

I simply save and exit.
The directory now looks like:

    dir
    ├── 1_a.png
    ├── 2_b.png
    ├── 3_c.png
    ├── 4_y.jpg
    ├── new.txt
    └── temp.txt

Say I want the `*.txt` files in an independent numbered list.
I run ` reorder -al "txt" dir`.
I am presented with the following buffer:

    new.txt
    temp.txt

I simply save and exit.
The directory now looks like:

    dir
    ├── 1_new.txt
    ├── 2_temp.txt
    ├── 1_a.png
    ├── 2_b.png
    ├── 3_c.png
    └── 4_y.jpg

It's worth noting that the `-l` command simply tries to match any of the space-separated substrings it is given, so it does not merely have to be the file extension.
If I run `reorder -al temp dir`, I am presented with the buffer:

    2_temp.txt


Lastly, all of these options can be applied the same way for use on directories instead of files using the `-d` flag.
