import ntpath
import os
import platform
import subprocess

from ioutils import IOUtils


class ShadowFile(object):
    """
    Creates a bit by bit backup of a file and allows you to revert the original file to that backup or commit your changes
    """
    def __init__(self, path, chunk_size:int = 1024):
        try:
            path_split = IOUtils.split_path(path)
            shadow_path = os.path.join(path_split[0], f'.~~shadow~~.{path_split[1]}.dat')
            os.remove(shadow_path)
            self._origin = open(path, 'r+b')
            self._shadow = open(shadow_path, 'w+b')
            IOUtils.hide_file(shadow_path)
            self._chunk_size = chunk_size
            self._closed = False
            self.copy_to_shadow()
        except EnvironmentError as e:
            raise IOError(f'Could not find the file {path} or could not open it, exception n {e.errno}')
    
    def copy_to_shadow(self):
        for data in IOUtils.read_chunk(self._chunk_size, self._origin):
            self._shadow.write(data)

    def copy_to_origin(self):
        for data in IOUtils.read_chunk(self._chunk_size, self._shadow):
            self._origin.write(data)

    def commit(self):
        self._origin.seek(0, 0)
        self.copy_to_shadow()

    def revert(self):
        self._shadow.seek(0, 0)
        self.copy_to_origin()
    
    def get_origin_dscr(self):
        return self._origin

    def close(self):
        self._origin.close()
        self._shadow.close()
        self._closed = True

if __name__ == '__main__':
    print('this file is a module and should not be ran directly')
