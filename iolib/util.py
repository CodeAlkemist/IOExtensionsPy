# Copyright (c) 2018 Computer Raven, All rights reserved
# IO utilities library core components

import ntpath
import os
import platform
import subprocess
import hashlib
import psutil


class Utils:
    
    @staticmethod
    def use_chunks(size):
        mem = psutil.virtual_memory()
        return True if mem.total//4 >= size else False

    @staticmethod
    def hide_file(path):
        """
        Simply hides a file if in windows add the hidden attribute if in linux prepend the filename with a .
        """

        if platform.system() == 'Windows':
            subprocess.check_call(["attrib","+H",path])
        else:
            path_parts = Utils.split_path(path)
            os.rename(path_parts[1], f'.{path_parts[1]}')

    @staticmethod
    def split_path(path):
        head, tail = ntpath.split(path)
        result = (head, tail)
        return result

    @staticmethod
    def read_chunk(chunk_size, file_descr):
        while True:
            data = file_descr.read(chunk_size)
            if not data:
                break
            yield data

    @staticmethod
    def write_chunk(chunks, file_desc):
            for data in chunks:
                file_desc.write(data)

    @staticmethod
    def __stream_hash__(hashing_algo:str, stream):
        """!!!Please note that this function is not to be used directly!!!

        This function is used internally by other methods in this class however if you still want to use it directly documentation can be found bellow
        Keyword arguments:

        hashing_algo -- algorithm to use we recommend using the hashlib.algorithms_available attribute to choose an algorithm (default none)
        stream -- a binary stream with read capabilities
        """

        try:
            ha: hash = hashlib.new(hashing_algo)
        except ValueError as e:
            raise ValueError(f'Error inappropriate hashing algorithm make sure you are not using the function directly, [{e}]')
        
        for data in Utils.read_chunk(ha.block_size, stream):
            ha.update(data)
        return ha.digest()

    @staticmethod
    def stream_md5_hash(stream):
        """
        Deprecated:
        This function is here for compatibility purposes only as MD5 shall be avoided if possible
        """
        h = Utils.__stream_hash__('md5', stream)
        return h.hex()
    
    @staticmethod
    def stream_sha256_hash(stream):
        """
        Use this function for most cases as for file hashing SHA256 is the recommended nowadays
        """
        h = Utils.__stream_hash__('sha256', stream)
        return h.hex()


if __name__ == '__main__':
    raise RuntimeError('this file is a module and should not be ran directly')
