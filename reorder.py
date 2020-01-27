#!/usr/bin/env python3
'''
This script renames, reorders, adds, and removes files in a directory with a numerical naming scheme.
'''
import re
import os
import os.path as path
import sys
import tempfile
import argparse
import subprocess

EDITOR = os.environ.get('EDITOR', 'vim')

def list_all(d):
    d = path.realpath(d)
    return [path.join(d, i) for i in os.listdir(d)]

def list_files(d):
    'return directory listing with full path names of files only'
    return [f for f in list_all(d) if path.isfile(f)]

def list_dirs(d):
    'return directory listing with full path names of folders only'
    return [f for f in list_all(d) if path.isdir(f)]

def get_previous_name(files, id):
    'Get the matching name from the previous files list'
    return [f for f in files if re.match(f'^{id}', f)]

def main(argv):
    parser = argparse.ArgumentParser(description="""Script to rename, reorder, add, and remove files in a directory with a numerical naming scheme.
    Run the program and provide a directory with the numbered files. A text buffer will be opened with the current files in the folder. Reorder, rename, add, or delete files in the buffer. Do not change the numbered part of the filename, these numbers will be recalculated and are used to match renamed files. Save and exit the editor. Then the program with perform the operations to the files in the directory.
    To cancel the operation, save an empty buffer.""")
    parser.add_argument('directory', help='The target directory')
    parser.add_argument('-a', '--add', help='Add unnumbered files to numbering', dest='add', action='store_true')
    parser.add_argument('-n', '--nono', help='Do not make changes', action='store_true')
    parser.add_argument('-v', '--verbose', help='Verbose output', action='store_true')
    args = parser.parse_args(argv[1:])

    renamed = 0
    added = 0
    deleted = 0


    # Get directory to reorder
    directory = path.realpath(args.directory)

    # Create list of files
    files = sorted([path.basename(f) for f in list_files(directory)])

    # Get separator
    try:
        sep = re.match(r'^(\d*)([_-])(.*)$', files[0])[2]
    except:
        sep = '_'

    # Remove unnumbered files
    unnumbered_files = []
    numbered_files = []
    if not args.add:
        for f in files:
            match = re.match(r'^(\d*)[_-](.*)$', f)
            if match:
                numbered_files.append(f)
            else:
                unnumbered_files.append(f)

        files = numbered_files

    # Create vim buffer content
    buf = '\n'.join(files)

    # Edit with vim
    with tempfile.NamedTemporaryFile(suffix='.tmp') as tf:
        tf.write(buf.encode('utf-8'))
        tf.flush()
        subprocess.call([EDITOR, tf.name])
        tf.seek(0)
        new_files = tf.read().decode('utf-8').rstrip().split('\n')
        new_files = [i for i in new_files if i]
        if len(new_files) == 0:
            print('Exited due to empty buffer.')
            exit()

    # Rename, Delete, Add files
    count = 1
    for f in new_files:
        # Rename
        match = re.match(r'^(\d*)[_-](.*)$', f)
        if match:
            id = match[1]
            name = match[2]
            old_name = get_previous_name(files, id)
            if len(old_name) == 1:
                if (old_name[0] != f or int(id) != count):
                    if not args.nono:
                        os.rename(path.join(directory, old_name[0]), path.join(directory, f'{count:02d}{sep}{name}'))
                    renamed += 1
                    if (args.verbose):
                        print(f'Renamed: {old_name[0]} to {count:02d}{sep}{name}.')
            else:
                print(f'Could not rename {name} since multiple old files match.')

            # Remove processed old files.
            for i in old_name:
                files.remove(i)

        # Add file to numbered list
        else:
            # Check is already exists
            if f in unnumbered_files or f in files:
                # Rename existing file
                if not args.nono:
                    os.rename(path.join(directory, f), path.join(directory, f'{count:02d}{sep}{f}'))
                renamed += 1
                if (args.verbose):
                    print(f'Renamed: {f} to {count:02d}{sep}{f}.')
                files.remove(f)
            else:
                # New file
                if not args.nono:
                    open(path.join(directory, f'{count:02d}{sep}{f}'), 'w').close()
                added += 1
                if (args.verbose):
                    print(f'Added: {count:02d}{sep}{f}.')

        count += 1

    # Delete
    for f in files:
        if not args.nono:
            os.remove(path.join(directory, f))
        deleted += 1
        if (args.verbose):
            print(f'Deleted: {f}.')

    # Print statistics
    print(f'Added: {added}  Deleted: {deleted}  Renamed: {renamed}')

if __name__ == '__main__':
    main(sys.argv)
