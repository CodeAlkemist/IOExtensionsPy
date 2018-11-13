import iolib


def main():
    with iolib.fs.File('../LICENSE', True) as f:
        print(f.hash)
        f.change_mode('r')
        print(f.__stream__.read())


if __name__ == '__main__':
    main()
