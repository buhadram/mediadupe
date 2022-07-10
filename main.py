#!/usr/bin/python3

import filedet

if __name__ == "__main__":
    start_dir = '/home/lutfi/Pictures.win/2018'
    print(f"Starting Directory = f{start_dir}")

    coll = filedet.fcollect(start_dir)
    f = coll.get_list()
    for item in f:
        print(f"berkas = {item}")
    print(len(f))
