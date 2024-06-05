'''
CidManager class for CID Manager Library
'''
import os
import json
import hashlib
from cid_data import CidData
class CidManager:
    def __init__(self):
        self.cid_data_list = []
    def add_cid_data(self, cid, hash):
        cid_data = CidData(cid, hash)
        self.cid_data_list.append(cid_data)
    def serialize_cid_data(self, output_dir="./output", folderSizeLimitInMB=1):
        folder_count = 0
        folder_size = 0
        folder_path = os.path.join(output_dir, f"Cid{folder_count:04d}")
        os.makedirs(folder_path, exist_ok=True)
        for cid_data in self.cid_data_list:
            json_data = json.dumps(cid_data.__dict__)
            # Calculate the hash of the json_data
            hash_object = hashlib.sha256(json_data.encode())
            hash_value = hash_object.hexdigest()
            # Update the hash field of the CidData object
            cid_data.hash = hash_value
            # Save the json file with the hash as the filename
            file_path = os.path.join(folder_path, f"{hash_value}.json")
            with open(file_path, "w") as file:
                file.write(json_data)
            # Update the folder size
            folder_size += os.path.getsize(file_path)
            # Check if the current folder size exceeds the given folderSizeLimitInMB
            if folder_size > folderSizeLimitInMB * 1024 * 1024:
                folder_count += 1
                folder_path = os.path.join(output_dir, f"Cid{folder_count:04d}")
                os.makedirs(folder_path, exist_ok=True)
                folder_size = 0  # Reset the folder size
    def deserialize_cid_data(self, input_dir="./output"):
        cid_data_list = []
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Read the json file
                with open(file_path, "r") as file:
                    json_data = file.read()
                # Deserialize the json data
                cid_data = CidData(**json.loads(json_data))
                cid_data_list.append(cid_data)
        return cid_data_list