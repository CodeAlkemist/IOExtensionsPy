import iolib.util
import os
import platform
import datetime


class File:
    """ Describes a file and allows for the aplication of usefull functions.
    This class describes a file with usefull information like permissions size and other features
    like the ability to easilly hide a file OS independently (for the most common OS's).
    """
    def __init__(self, path: str, open_stream: bool=False, mode: str='rb', cache_hash: bool = True):
        """ Constructor of the File class
        :arg path -- the path to create a File instance with
        :arg open_stream -- Shall a stream be opened?
        :arg mode -- if open_stream is true pass a mode with this argument
        """
        if not os.path.exists(path):
            raise IOError(f'File {path} not found')
        self.__file_path__ = path
        self.__stream__ = None
        self.__mode__ = mode
        self.has_open_stream = False
        self.size = os.path.getsize(self.__file_path__)
        self.modate = os.path.getmtime(self.__file_path__)
        self.createdate = self.creation_date()
        self.human_modate = datetime.datetime.fromtimestamp(self.modate).isoformat()

        if open_stream:
            try:
                self.__stream__ = open(self.__file_path__, self.__mode__)
            except IOError as e:
                raise EnvironmentError(f'An IO exception has occured [{e}]')
            else:
                self.has_open_stream = True

        if cache_hash and open_stream:
            self.hash = self.get_hash()
        else:
            self.hash = None

    def __enter__(self): return self

    def __exit__(self, type, value, traceback):
        if self.has_open_stream:
            self.__stream__.close()
            self.has_open_stream = False

    def change_mode(self, mode):
        if self.has_open_stream:
            self.__stream__.close()
            self.__stream__ = open(self.__file_path__, mode)
        else:
            raise ValueError('There is not an open stream yet for this file')

    def creation_date(self):
        """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        """
        if platform.system() == 'Windows':
            return os.path.getctime(self.__file_path__)
        else:
            stat = os.stat(self.__file_path__)
            try:
                return stat.st_birthtime
            except AttributeError:
                # Probably on Linux. No easy way to get creation dates,
                # so we'll settle for when its content was last modified.
                return stat.st_mtime

    def get_hash(self):
        if self.has_open_stream:
            return iolib.util.Utils.stream_sha256_hash(self.__stream__)
        else:
            raise EnvironmentError('No open stream to retrieve data from')


if __name__ == "__main__":
    raise RuntimeError('this file is a module and should not be ran directly')
