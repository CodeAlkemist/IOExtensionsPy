# Copyright (c) 2018 Computer Raven, All rights reserved
# IO utilities library core components

import ntpath
import os
import platform
import subprocess


class IOUtils(object):
    @staticmethod
    def hide_file(path):
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

if __name__ == '__main__':
    print('this file is a module and should not be ran directly')
