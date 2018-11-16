# Copyright (c) 2018 Computer Raven, All rights reserved
# IO utilities library core components

import ntpath
import os
import platform
import subprocess
import psutil
import swan.util
import io


def use_chunks(size):
    mem = psutil.virtual_memory()
    return True if mem.total//4 >= size else False


def hide_file(path):
    """
    Simply hides a file if in windows add the hidden attribute if in linux prepend the filename with a .
    """

    if platform.system() == 'Windows':
        subprocess.check_call(["attrib", "+H", path])
    else:
        path_parts = split_path(path)
        os.rename(path_parts[1], f'.{path_parts[1]}')


def split_path(path):
    return ntpath.split(path)


def write_chunk(chunks, file_desc):
        for data in chunks:
            file_desc.write(data)


@swan.util.deprecated('This function is here for compatibility purposes only as MD5 shall be avoided if possible')
def stream_md5_hash(stream: io.BytesIO):
    """
    Deprecated:
    This function is here for compatibility purposes only as MD5 shall be avoided if possible
    """
    h = swan.util.__stream_hash__('md5', stream)
    return h.hex()


def stream_sha256_hash(stream: io.BytesIO):
    """
    Use this function for most cases as for file hashing SHA256 is the recommended nowadays
    """
    h = swan.util.__stream_hash__('sha256', stream)
    return h, h.hex()


if __name__ == '__main__':
    raise RuntimeError('this file is a module and should not be ran directly')
