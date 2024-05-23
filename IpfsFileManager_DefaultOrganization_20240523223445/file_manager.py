'''
File manager class for reading files, serializing to JSON, and saving JSON files.
'''
import os
import json
import hashlib
from python_file import PythonFile
class PythonFileEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PythonFile):
            return obj.__dict__
        return super().default(obj)
class FileManager:
    def read_files(self, folderDir):
        python_files = []
        for filename in os.listdir(folderDir):
            if filename.endswith(".py"):
                file_path = os.path.join(folderDir, filename)
                file_type = "Python"
                file_length = os.path.getsize(file_path)
                python_file = PythonFile(filename, file_path, file_type, file_length)
                python_files.append(python_file)
        return python_files
    def serialize_to_json(self, python_files):
        serialized_data = json.dumps(python_files, cls=PythonFileEncoder)
        return serialized_data
    def save_json_file(self, json_data, output_path):
        with open(output_path, "w") as file:
            file.write(json_data)