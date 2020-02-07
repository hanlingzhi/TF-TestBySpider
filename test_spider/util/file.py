__author__ = 'hanlingzhi'

import hashlib, os

from os.path import join, getsize

'''
create_date: 2019.12.5
usage: file
'''


class FileUtil:
    @staticmethod
    def get_md5(file_path):
        f = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            md5_obj.update(d)
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
        return md5

    @staticmethod
    def get_file_line(path):
        if os.path.exists(path):
            count = -1
            for count, line in enumerate(open(path).readlines()):
                pass
                count += 1
            return count
        else:
            return 0

    @staticmethod
    def get_dir_size(dir_path):
        size = 0
        for root, dirs, files in os.walk(dir_path):
            size += sum([getsize(join(root, name)) for name in files])
        if size > 1024 * 1024 * 1024:
            return_size = "%sGB" % (size / 1024 / 1024 / 1024)
        elif size > 1024 * 1024:
            return_size = "%sMB" % (size / 1024 / 1024)
        else:
            return_size = "%sKB" % (size / 1024)
        return return_size
