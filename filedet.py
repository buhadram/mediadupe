#!/usr/bin/python3

import os

class fcollect:
    #startdir = '.'

    def __init__(self, start_dir):
        self.startdir = start_dir
        self.found_files = []

        print(f"Collecting files from {self.startdir }")
        for dirname, dirnames, filenames in os.walk(self.startdir):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))

            # print path to all filenames.
            for filename in filenames:
                #print(os.path.join(dirname, filename))
                self.found_files.append(os.path.join(dirname, filename))

            # Advanced usage:
            # editing the 'dirnames' list will stop os.walk() from recursing into there.
            if '.git' in dirnames:
                # don't go into any .git directories.
                dirnames.remove('.git')

    def get_list(self):
        return self.found_files