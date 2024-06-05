# IPFS HTTP API Library

## Introduction

The IPFS HTTP API Library is a Python library that allows you to interact with the IPFS network using the IPFS Kubo RPC API. It provides a set of APIs for adding files and folders to the IPFS network, pinning and removing CIDs, retrieving files and folders by CID, downloading files and folders from the IPFS network, and reading files by CID. The library is designed to be easy to use and does not require any third-party IPFS library imports.

## Installation

To install the IPFS HTTP API Library, you can use pip or conda package manager.

Using pip:

```
pip install ipfs-http-api
```

Using conda:

```
conda install -c conda-forge ipfs-http-api
```

## Usage

To use the IPFS HTTP API Library, you need to create an instance of the `IpfsHttpApi` class and provide the base URL of the IPFS Kubo RPC API as a parameter. Here's an example:

```python
from ipfs_http_api import IpfsHttpApi

api = IpfsHttpApi('http://localhost:5001')
```

### Adding a File to IPFS Network

To add a file to the IPFS network, you can use the `add_file` method. It takes the file path as a parameter and returns a response JSON containing the status and CID of the added file. Here's an example:

```python
response = api.add_file('path/to/file.txt')
print(response['status'])  # success
print(response['cid'])  # Qm123456789
```

### Adding a Folder to IPFS Network

To add a folder to the IPFS network, you can use the `add_folder` method. It takes the folder path as a parameter and returns a response JSON containing the status and CID of the added folder. Here's an example:

```python
response = api.add_folder('path/to/folder')
print(response['status'])  # success
print(response['cid'])  # Qm123456789
```

### Pinning a CID to Local IPFS Network

To pin a CID to the local IPFS network, you can use the `pin_cid` method. It takes the CID as a parameter and returns a response JSON containing the status of the pinning operation. Here's an example:

```python
response = api.pin_cid('Qm123456789')
print(response['status'])  # success
```

### Pinning a CID Recursively to Local IPFS

To pin a CID recursively to the local IPFS network, you can use the `pin_cid_recursively` method. It takes the CID as a parameter and returns a response JSON containing the status of the pinning operation. Here's an example:

```python
response = api.pin_cid_recursively('Qm123456789')
print(response['status'])  # success
```

### Removing a Pinned CID

To remove a pinned CID from the local IPFS network, you can use the `remove_pinned_cid` method. It takes the CID as a parameter and returns a response JSON containing the status of the removal operation. Here's an example:

```python
response = api.remove_pinned_cid('Qm123456789')
print(response['status'])  # success
```

### Getting a File by CID from IPFS Network

To get a file by CID from the IPFS network, you can use the `get_file_by_cid` method. It takes the CID as a parameter and returns the content of the file as bytes. Here's an example:

```python
content = api.get_file_by_cid('Qm123456789')
print(content)  # b'File content'
```

### Getting a Folder by CID from IPFS Network

To get a folder by CID from the IPFS network, you can use the `get_folder_by_cid` method. It takes the CID as a parameter and returns a response JSON containing the files and directories in the folder. Here's an example:

```python
response = api.get_folder_by_cid('Qm123456789')
print(response['files'])  # ['file1.txt', 'file2.txt']
```

### Downloading a File by CID from IPFS Network

To download a file by CID from the IPFS network, you can use the `download_file_by_cid` method. It takes the CID and the save path as parameters and downloads the file to the specified path. Here's an example:

```python
api.download_file_by_cid('Qm123456789', 'path/to/save/file.txt')
```

### Downloading a Folder by CID from IPFS Network

To download a folder by CID from the IPFS network, you can use the `download_folder_by_cid` method. It takes the CID and the save path as parameters and downloads the folder to the specified path. Here's an example:

```python
api.download_folder_by_cid('Qm123456789', 'path/to/save/folder')
```

### Reading a File by CID from IPFS Network

To read a file by CID from the IPFS network, you can use the `read_file_by_cid` method. It takes the CID as a parameter and returns the content of the file as a string. Here's an example:

```python
content = api.read_file_by_cid('Qm123456789')
print(content)  # 'File content'
```

### Accessing Files from IPFS Network

To access files from the IPFS network, you can use the `access_files` method. It takes the path as a parameter and returns a response JSON containing the files and directories in the path. Here's an example:

```python
response = api.access_files('/path/to/files')
print(response)  # {'files': ['file1.txt', 'file2.txt'], 'directories': ['dir1', 'dir2']}
```

### Listing Files from IPFS Network

To list files from the IPFS network, you can use the `list_files` method. It takes the path as a parameter and returns a response JSON containing the files and directories in the path. Here's an example:

```python
response = api.list_files('/path/to/files')
print(response)  # {'files': ['file1.txt', 'file2.txt'], 'directories': ['dir1', 'dir2']}
```

### Getting Files from IPFS Network

To get files from the IPFS network, you can use the `get_files` method. It takes the path as a parameter and returns a response JSON containing the files and directories in the path. Here's an example:

```python
response = api.get_files('/path/to/files')
print(response)  # {'files': ['file1.txt', 'file2.txt'], 'directories': ['dir1', 'dir2']}
```

### Reading Files from IPFS Network

To read files from the IPFS network, you can use the `read_files` method. It takes the path as a parameter and returns a response JSON containing the files and directories in the path. Here's an example:

```python
response = api.read_files('/path/to/files')
print(response)  # {'files': ['file1.txt', 'file2.txt'], 'directories': ['dir1', 'dir2']}
```

## Testing

The IPFS HTTP API Library comes with a set of unit tests to ensure its functionality. To run the tests, you can use the `unittest` module. Here's an example:

```python
import unittest
from ipfs_http_api import IpfsHttpApi

class TestIpfsHttpApi(unittest.TestCase):
    def setUp(self):
        self.api = IpfsHttpApi('http://localhost:5001')

    # Add your test methods here

if __name__ == '__main__':
    unittest.main()
```

You can add your test methods to the `TestIpfsHttpApi` class and run the tests using the `unittest.main()` function.

## Conclusion

The IPFS HTTP API Library provides a convenient way to interact with the IPFS network using the IPFS Kubo RPC API. It allows you to add files and folders to the IPFS network, pin and remove CIDs, retrieve files and folders by CID, download files and folders from the IPFS network, and read files by CID. The library is easy to use and comes with a set of unit tests to ensure its functionality.