'''
Unit test for serializing and deserializing PythonFile objects.
'''
import unittest
import os
import json
from file_manager import FileManager
from python_file import PythonFile
class TestSerializeDeserialize(unittest.TestCase):
    def test_serialize_deserialize(self):
        sample_files = [
            PythonFile("file1.py", "/path/to/file1.py", "Python", 100),
            PythonFile("file2.py", "/path/to/file2.py", "Python", 200),
            PythonFile("file3.py", "/path/to/file3.py", "Python", 300)
        ]
        file_manager = FileManager()
        serialized_data = file_manager.serialize_to_json(sample_files)
        deserialized_files = json.loads(serialized_data)
        for i, deserialized_file in enumerate(deserialized_files):
            self.assertEqual(deserialized_file["FileName"], sample_files[i].FileName)
            self.assertEqual(deserialized_file["FilePath"], sample_files[i].FilePath)
            self.assertEqual(deserialized_file["FileType"], sample_files[i].FileType)
            self.assertEqual(deserialized_file["FileLength"], sample_files[i].FileLength)
if __name__ == "__main__":
    unittest.main()