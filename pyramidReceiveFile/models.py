import time
import multiprocessing


class ModelProduct(object):

    @classmethod
    def process(cls, file_storage):
        p = multiprocessing.Process(target=cls._process, args=(file_storage,))
        p.start()
        return True

    @classmethod
    def get_result(cls, file_name):
        try:
            with open("files_processed/" + file_name) as _file:
                return _file.read()
        except FileNotFoundError:
            return None

    @staticmethod
    def _process(file_storage):
        time.sleep(10)
        open("files_processed/" + file_storage.filename, 'wb').write(file_storage.file.read())
        return True
