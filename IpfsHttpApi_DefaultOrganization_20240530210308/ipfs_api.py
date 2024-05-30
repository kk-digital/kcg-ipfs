'''
This file contains the IPFSAPI class which provides the functionality to interact with the IPFS network using the Kubo RPC API.
'''
import os
import requests
class IPFSAPI:
    def __init__(self):
        self.base_url = "https://api.ipfs.tech/kubo/rpc"
    def add_file(self, file_path):
        url = self.base_url + "/add/file"
        files = {"file": open(file_path, "rb")}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            return response.json()["cid"]
        else:
            raise Exception("Failed to add file to IPFS network.")
    def add_folder(self, folder_path):
        url = self.base_url + "/add/folder"
        files = []
        for root, _, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                files.append(("files", open(file_path, "rb")))
        response = requests.post(url, files=files)
        if response.status_code == 200:
            return response.json()["cid"]
        else:
            raise Exception("Failed to add folder to IPFS network.")
    def pin_cid(self, cid):
        url = self.base_url + "/pin"
        data = {"cid": cid}
        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise Exception("Failed to pin CID to local IPFS network.")
    def pin_cid_recursive(self, cid):
        url = self.base_url + "/pin/recursive"
        data = {"cid": cid}
        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise Exception("Failed to pin CID recursively to local IPFS network.")
    def remove_cid(self, cid):
        url = self.base_url + "/pin/remove"
        data = {"cid": cid}
        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise Exception("Failed to remove pinned CID.")
    def get_file(self, cid):
        url = self.base_url + "/get/file"
        params = {"cid": cid}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            file_path = f"{cid}.file"
            with open(file_path, "wb") as file:
                file.write(response.content)
            return file_path
        else:
            raise Exception("Failed to get file from IPFS network.")
    def get_folder(self, cid):
        url = self.base_url + "/get/folder"
        params = {"cid": cid}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            folder_path = f"{cid}.folder"
            os.makedirs(folder_path, exist_ok=True)
            for file_name, file_content in response.json().items():
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, "wb") as file:
                    file.write(file_content.encode("utf-8"))
            return folder_path
        else:
            raise Exception("Failed to get folder from IPFS network.")
    def download_file(self, cid, save_path):
        file_path = self.get_file(cid)
        if file_path:
            os.rename(file_path, save_path)
    def download_folder(self, cid, save_path):
        folder_path = self.get_folder(cid)
        if folder_path:
            os.rename(folder_path, save_path)
    def read_file(self, cid):
        file_path = self.get_file(cid)
        if file_path:
            with open(file_path, "r") as file:
                return file.read()
        else:
            return None