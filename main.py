import filedet as fd

if __name__ == "__main__":
    g = fd.fcollect('/home/lutfi/Pictures.win')
    f = g.get_list()
    for item in f:
        print(f)