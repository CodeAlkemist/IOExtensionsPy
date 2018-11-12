from io_utils import ioutils

def main():
    assert (ioutils.IOUtils.file_md5_hash('./test_file1') != ioutils.IOUtils.file_md5_hash('./test_file2'))

if __name__ == '__main__':
    main()