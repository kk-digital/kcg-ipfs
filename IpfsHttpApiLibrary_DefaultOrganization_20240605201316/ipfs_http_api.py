import requests
import os
class IpfsHttpApi:
    def __init__(self, base_url):
        self.base_url = base_url
    def add_file(self, file_path):
        """
        Add a file to the IPFS network.
        Args:
            file_path (str): The path of the file to be added.
        Returns:
            dict: The response JSON containing the status and CID of the added file.
        """
        url = f"{self.base_url}/add"
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files)
        return response.json()
    def add_folder(self, folder_path):
        """
        Add a folder to the IPFS network.
        Args:
            folder_path (str): The path of the folder to be added.
        Returns:
            dict: The response JSON containing the status and CID of the added folder.
        """
        url = f"{self.base_url}/add?recursive=true"
        files = []
        for root, _, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                files.append(('file', open(file_path, 'rb')))
        response = requests.post(url, files=files)
        return response.json()
    def pin_cid(self, cid):
        """
        Pin a CID to the local IPFS network.
        Args:
            cid (str): The CID to be pinned.
        Returns:
            dict: The response JSON containing the status of the pinning operation.
        """
        url = f"{self.base_url}/pin/add?arg={cid}"
        response = requests.get(url)
        return response.json()
    def pin_cid_recursively(self, cid):
        """
        Pin a CID recursively to the local IPFS network.
        Args:
            cid (str): The CID to be pinned recursively.
        Returns:
            dict: The response JSON containing the status of the pinning operation.
        """
        url = f"{self.base_url}/pin/add?arg={cid}&recursive=true"
        response = requests.get(url)
        return response.json()
    def remove_pinned_cid(self, cid):
        """
        Remove a pinned CID from the local IPFS network.
        Args:
            cid (str): The CID to be removed.
        Returns:
            dict: The response JSON containing the status of the removal operation.
        """
        url = f"{self.base_url}/pin/rm?arg={cid}"
        response = requests.get(url)
        return response.json()
    def get_file_by_cid(self, cid):
        """
        Get a file by CID from the IPFS network.
        Args:
            cid (str): The CID of the file to be retrieved.
        Returns:
            bytes: The content of the file.
        """
        url = f"{self.base_url}/cat?arg={cid}"
        response = requests.get(url)
        return response.content
    def get_folder_by_cid(self, cid):
        """
        Get a folder by CID from the IPFS network.
        Args:
            cid (str): The CID of the folder to be retrieved.
        Returns:
            dict: The response JSON containing the files and directories in the folder.
        """
        url = f"{self.base_url}/ls?arg={cid}"
        response = requests.get(url)
        return response.json()
    def download_file_by_cid(self, cid, save_path):
        """
        Download a file by CID from the IPFS network.
        Args:
            cid (str): The CID of the file to be downloaded.
            save_path (str): The path to save the downloaded file.
        Returns:
            None
        """
        url = f"{self.base_url}/get?arg={cid}"
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
    def download_folder_by_cid(self, cid, save_path):
        """
        Download a folder by CID from the IPFS network.
        Args:
            cid (str): The CID of the folder to be downloaded.
            save_path (str): The path to save the downloaded folder.
        Returns:
            None
        """
        url = f"{self.base_url}/get?arg={cid}&archive=true"
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
    def read_file_by_cid(self, cid):
        """
        Read a file by CID from the IPFS network.
        Args:
            cid (str): The CID of the file to be read.
        Returns:
            str: The content of the file.
        """
        url = f"{self.base_url}/cat?arg={cid}"
        response = requests.get(url)
        return response.text
    def access_files(self, path):
        """
        Access files from the IPFS network.
        Args:
            path (str): The path of the files to be accessed.
        Returns:
            dict: The response JSON containing the files and directories in the path.
        """
        url = f"{self.base_url}/files/ls?arg={path}"
        response = requests.get(url)
        return response.json()
    def list_files(self, path):
        """
        List files from the IPFS network.
        Args:
            path (str): The path of the files to be listed.
        Returns:
            dict: The response JSON containing the files and directories in the path.
        """
        url = f"{self.base_url}/files/ls?arg={path}"
        response = requests.get(url)
        return response.json()
    def get_files(self, path):
        """
        Get files from the IPFS network.
        Args:
            path (str): The path of the files to be retrieved.
        Returns:
            dict: The response JSON containing the files and directories in the path.
        """
        url = f"{self.base_url}/files/get?arg={path}"
        response = requests.get(url)
        return response.json()
    def read_files(self, path):
        """
        Read files from the IPFS network.
        Args:
            path (str): The path of the files to be read.
        Returns:
            dict: The response JSON containing the files and directories in the path.
        """
        url = f"{self.base_url}/files/read?arg={path}"
        response = requests.get(url)
        return response.json()