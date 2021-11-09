import os
import base64
from config import Config


class TemporaryFileManager(object):

    def __init__(self, extra_path=''):
        self.extra_path = extra_path
        self.dir = os.path.join(Config.APP_ROOT, Config.STATIC_DIR, extra_path)
        self.file = self.dir
        self.file_name = ''

    def open_file(self, file_name=''):
        self.file_name = file_name
        self.file = os.path.join(self.dir, file_name)

    def close(self):
        if self.file:
            try:
                os.remove(self.file)
            except (FileNotFoundError, IsADirectoryError):
                pass
        self.file = ''

    def isvalid(self):
        return True if self.file_name else False

    def get_dir(self):
        return self.dir

    def get_relative_file(self):
        return os.path.join(self.extra_path, self.file_name)

    def to_relative_file(self, file):
        return os.path.join(self.extra_path, file)

    def get_extra(self):
        return self.extra_path
    # def get_relative_file(self):
        # return self.extra_path + "/" + self.file_name

    def get_abs_file(self):
        return self.file

    def get_base64(self):
        ''' 图片 返回base64编码 '''
        base64_data = ''
        with open(self.file, "rb") as f:
            base64_data = base64.b64encode(f.read())
        self.close()
        return str(base64_data, 'utf-8')

    def __str__(self):
        return self.file

    __repr__ = __str__
