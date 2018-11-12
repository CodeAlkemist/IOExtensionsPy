# Copyright (c) 2018 Computer Raven, All rights reserved
# IO utilities library core components

import ntpath
import os
import platform
import subprocess
import hashlib
from psutil import virtual_memory


class IOUtils(object):
    
    @staticmethod
    def use_chunks(size):
        mem = virtual_memory()
        return true if mem.total//4 >= size else False

    @staticmethod
    def hide_file(path):
        """
        Simply hides a file if in windows add the hidden attribute if in linux prepend the filename with a .
        """

        if platform.system() == 'Windows':
            subprocess.check_call(["attrib","+H",path])
        else:
            path_parts = IOUtils.split_path(path)
            os.rename(path_parts[1], f'.{path_parts[1]}')

    @staticmethod
    def split_path(path):
        head, tail = ntpath.split(path)
        result = (head, tail)
        return result

    @staticmethod
    def read_chunk(chunk_size, source):
        while True:
            data = source.read(chunk_size)
            if not data:
                break
            yield data

    @staticmethod
    def __stream_hash__(hashing_algo:str, source):
        """!!!Please note that this function is not to be used directly!!!

        This function is used internally by other methods in this class however if you still want to use it directly documentation can be found bellow
        Keyword arguments:

        hashing_algo -- algorithm to use we recommend using the hashlib.algorithms_available attribute to choose an algorithm (default none)
        source -- a binary stream with read capabilities
        """

        try:
            ha:hash = hashlib.new(hashing_algo)
        except ValueError as e:
            raise ValueError(f'Error inappropriate hashing algorithm make sure you are not using the function directly, [{e}]')
        for data in IOUtils.read_chunk(ha.block_size, source):
            ha.update(data)
        return ha.digest()

    @staticmethod
    def create_noise_file(fname, size):
        with open(fname, 'wb+') as f:


    @staticmethod
    def file_md5_hash(path):
        """
        Deprecated:
        This function is here for compatibility purposes only as MD5 shall be avoided if possible
        """
        try:
            with open(path, 'rb') as f:
                h = IOUtils.__stream_hash__('md5', f)
            return h.hex()
        except IOError as e:
            raise IOError(f'Could not open the file for hashing [{e}]')


if __name__ == '__main__':
    raise EnvironmentError('this file is a module and should not be ran directly')
