'''
Python file class with fields: FileName, FilePath, FileType, FileLength, FileHash.
'''
import hashlib
class PythonFile:
    def __init__(self, file_name, file_path, file_type, file_length):
        self.FileName = file_name
        self.FilePath = file_path
        self.FileType = file_type
        self.FileLength = file_length
        self.FileHash = None
    def calculate_hash(self):
        with open(self.FilePath, "rb") as file:
            file_content = file.read()
            self.FileHash = hashlib.blake2b(file_content).hexdigest()