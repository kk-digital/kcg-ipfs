# IPFS HTTP API Library User Manual

## Introduction

The IPFS HTTP API Library is a Python library that allows users to interact with the IPFS network using the Kubo RPC API. It provides a set of functions that enable users to perform various operations such as adding files and folders to the IPFS network, pinning and removing CIDs, retrieving files and folders from the network, and more.

This user manual provides detailed instructions on how to install the library, set up the environment, and use the library's functions to interact with the IPFS network.

## Table of Contents

1. [Installation](#installation)
2. [Setting Up the Environment](#setting-up-the-environment)
3. [Library Functions](#library-functions)
   - [Add a File to IPFS Network](#add-a-file-to-ipfs-network)
   - [Add a Folder to IPFS Network](#add-a-folder-to-ipfs-network)
   - [Pin a CID to Local IPFS Network](#pin-a-cid-to-local-ipfs-network)
   - [Pin a CID Recursively to Local IPFS](#pin-a-cid-recursively-to-local-ipfs)
   - [Remove a Pinned CID](#remove-a-pinned-cid)
   - [Get a File by CID from IPFS Network](#get-a-file-by-cid-from-ipfs-network)
   - [Get a Folder by CID from IPFS Network](#get-a-folder-by-cid-from-ipfs-network)
   - [Download a File by CID from IPFS Network](#download-a-file-by-cid-from-ipfs-network)
   - [Download a Folder by CID from IPFS Network](#download-a-folder-by-cid-from-ipfs-network)
   - [Read a File by CID from IPFS Network](#read-a-file-by-cid-from-ipfs-network)
4. [Examples](#examples)
5. [Unit Tests](#unit-tests)
6. [Troubleshooting](#troubleshooting)
7. [Resources](#resources)

## Installation <a name="installation"></a>

To install the IPFS HTTP API Library, you can use either `pip` or `conda`. Open your terminal or command prompt and run one of the following commands:

Using `pip`:

```
pip install ipfs-http-api-library
```

Using `conda`:

```
conda install -c conda-forge ipfs-http-api-library
```

## Setting Up the Environment <a name="setting-up-the-environment"></a>

Before using the IPFS HTTP API Library, you need to set up the environment by following these steps:

1. Make sure you have Python 3.7 or higher installed on your system. You can check the installed version by running the following command:

   ```
   python --version
   ```

2. Create a new Python virtual environment (optional but recommended). Open your terminal or command prompt and run the following command:

   ```
   python -m venv ipfs-env
   ```

   This will create a new virtual environment named `ipfs-env`.

3. Activate the virtual environment. Run the following command:

   - For Windows:

     ```
     ipfs-env\Scripts\activate
     ```

   - For macOS and Linux:

     ```
     source ipfs-env/bin/activate
     ```

4. Install the required dependencies. Run the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary dependencies for the IPFS HTTP API Library.

5. You are now ready to use the IPFS HTTP API Library in your Python environment.

## Library Functions <a name="library-functions"></a>

The IPFS HTTP API Library provides the following functions to interact with the IPFS network:

### Add a File to IPFS Network <a name="add-a-file-to-ipfs-network"></a>

```python
def add_file(file_path: str) -> str:
    """
    Adds a file to the IPFS network.

    Parameters:
        file_path (str): The path to the file to be added.

    Returns:
        str: The CID (Content Identifier) of the added file.
    """
```

This function allows you to add a file to the IPFS network. You need to provide the `file_path` parameter, which is the path to the file you want to add. The function returns the CID (Content Identifier) of the added file.

### Add a Folder to IPFS Network <a name="add-a-folder-to-ipfs-network"></a>

```python
def add_folder(folder_path: str) -> str:
    """
    Adds a folder to the IPFS network.

    Parameters:
        folder_path (str): The path to the folder to be added.

    Returns:
        str: The CID (Content Identifier) of the added folder.
    """
```

This function allows you to add a folder to the IPFS network. You need to provide the `folder_path` parameter, which is the path to the folder you want to add. The function returns the CID (Content Identifier) of the added folder.

### Pin a CID to Local IPFS Network <a name="pin-a-cid-to-local-ipfs-network"></a>

```python
def pin_cid(cid: str) -> None:
    """
    Pins a CID to the local IPFS network.

    Parameters:
        cid (str): The CID (Content Identifier) to be pinned.
    """
```

This function allows you to pin a CID to the local IPFS network. You need to provide the `cid` parameter, which is the CID you want to pin.

### Pin a CID Recursively to Local IPFS <a name="pin-a-cid-recursively-to-local-ipfs"></a>

```python
def pin_cid_recursive(cid: str) -> None:
    """
    Pins a CID recursively to the local IPFS network.

    Parameters:
        cid (str): The CID (Content Identifier) to be pinned recursively.
    """
```

This function allows you to pin a CID recursively to the local IPFS network. You need to provide the `cid` parameter, which is the CID you want to pin recursively.

### Remove a Pinned CID <a name="remove-a-pinned-cid"></a>

```python
def remove_cid(cid: str) -> None:
    """
    Removes a pinned CID.

    Parameters:
        cid (str): The CID (Content Identifier) to be removed.
    """
```

This function allows you to remove a pinned CID. You need to provide the `cid` parameter, which is the CID you want to remove.

### Get a File by CID from IPFS Network <a name="get-a-file-by-cid-from-ipfs-network"></a>

```python
def get_file(cid: str) -> str:
    """
    Retrieves a file from the IPFS network.

    Parameters:
        cid (str): The CID (Content Identifier) of the file to be retrieved.

    Returns:
        str: The path to the retrieved file.
    """
```

This function allows you to retrieve a file from the IPFS network. You need to provide the `cid` parameter, which is the CID of the file you want to retrieve. The function returns the path to the retrieved file.

### Get a Folder by CID from IPFS Network <a name="get-a-folder-by-cid-from-ipfs-network"></a>

```python
def get_folder(cid: str) -> str:
    """
    Retrieves a folder from the IPFS network.

    Parameters:
        cid (str): The CID (Content Identifier) of the folder to be retrieved.

    Returns:
        str: The path to the retrieved folder.
    """
```

This function allows you to retrieve a folder from the IPFS network. You need to provide the `cid` parameter, which is the CID of the folder you want to retrieve. The function returns the path to the retrieved folder.

### Download a File by CID from IPFS Network <a name="download-a-file-by-cid-from-ipfs-network"></a>

```python
def download_file(cid: str, save_path: str) -> None:
    """
    Downloads a file from the IPFS network.

    Parameters:
        cid (str): The CID (Content Identifier) of the file to be downloaded.
        save_path (str): The path to save the downloaded file.
    """
```

This function allows you to download a file from the IPFS network. You need to provide the `cid` parameter, which is the CID of the file you want to download, and the `save_path` parameter, which is the path where you want to save the downloaded file.

### Download a Folder by CID from IPFS Network <a name="download-a-folder-by-cid-from-ipfs-network"></a>

```python
def download_folder(cid: str, save_path: str) -> None:
    """
    Downloads a folder from the IPFS network.

    Parameters:
        cid (str): The CID (Content Identifier) of the folder to be downloaded.
        save_path (str): The path to save the downloaded folder.
    """
```

This function allows you to download a folder from the IPFS network. You need to provide the `cid` parameter, which is the CID of the folder you want to download, and the `save_path` parameter, which is the path where you want to save the downloaded folder.

### Read a File by CID from IPFS Network <a name="read-a-file-by-cid-from-ipfs-network"></a>

```python
def read_file(cid: str) -> str:
    """
    Reads the content of a file from the IPFS network.

    Parameters:
        cid (str): The CID (Content Identifier) of the file to be read.

    Returns:
        str: The content of the file.
    """
```

This function allows you to read the content of a file from the IPFS network. You need to provide the `cid` parameter, which is the CID of the file you want to read. The function returns the content of the file.

## Examples <a name="examples"></a>

Here are some examples of how to use the IPFS HTTP API Library functions:

```python
from ipfs_http_api_library import IPFSAPI

# Create an instance of the IPFSAPI class
ipfs_api = IPFSAPI()

# Add a file to the IPFS network
file_path = "path/to/file.txt"
cid = ipfs_api.add_file(file_path)
print(f"File added to IPFS network. CID: {cid}")

# Add a folder to the IPFS network
folder_path = "path/to/folder"
cid = ipfs_api.add_folder(folder_path)
print(f"Folder added to IPFS network. CID: {cid}")

# Pin a CID to the local IPFS network
cid = "Qm123456789"
ipfs_api.pin_cid(cid)
print(f"CID pinned to local IPFS network. CID: {cid}")

# Pin a CID recursively to the local IPFS network
cid = "Qm123456789"
ipfs_api.pin_cid_recursive(cid)
print(f"CID pinned recursively to local IPFS network. CID: {cid}")

# Remove a pinned CID
cid = "Qm123456789"
ipfs_api.remove_cid(cid)
print(f"Pinned CID removed. CID: {cid}")

# Get a file by CID from IPFS network
cid = "Qm123456789"
file_path = ipfs_api.get_file(cid)
print(f"File retrieved from IPFS network. File path: {file_path}")

# Get a folder by CID from IPFS network
cid = "Qm123456789"
folder_path = ipfs_api.get_folder(cid)
print(f"Folder retrieved from IPFS network. Folder path: {folder_path}")

# Download a file by CID from IPFS network
cid = "Qm123456789"
save_path = "path/to/save/file.txt"
ipfs_api.download_file(cid, save_path)
print("File downloaded from IPFS network.")

# Download a folder by CID from IPFS network
cid = "Qm123456789"
save_path = "path/to/save/folder"
ipfs_api.download_folder(cid, save_path)
print("Folder downloaded from IPFS network.")

# Read a file by CID from IPFS network
cid = "Qm123456789"
content = ipfs_api.read_file(cid)
print(f"File content: {content}")
```

## Unit Tests <a name="unit-tests"></a>

The IPFS HTTP API Library includes unit tests to ensure the correctness of its functions. To run the unit tests, you can use the following command:

```
python -m unittest discover
```

This will discover and run all the unit tests in the library.

## Troubleshooting <a name="troubleshooting"></a>

If you encounter any issues or have any questions regarding the IPFS HTTP API Library, please refer to the [official documentation](https://docs.ipfs.tech/reference/kubo/rpc/) or [open an issue](https://github.com/ipfs-http-api-library/issues) on the GitHub repository.

## Resources <a name="resources"></a>

- [IPFS Kubo RPC API Documentation](https://docs.ipfs.tech/reference/kubo/rpc/)
- [IPFS HTTP API Library GitHub Repository](https://github.com/ipfs-http-api-library)
- [IPFS Official Website](https://ipfs.io/)
- [IPFS Community Forum](https://discuss.ipfs.io/)

```

This user manual provides detailed instructions on how to install the IPFS HTTP API Library, set up the environment, and use the library's functions to interact with the IPFS network. It also includes examples, unit tests, troubleshooting information, and additional resources for further reference.

By following this user manual, users will be able to effectively utilize the IPFS HTTP API Library and leverage its functionalities to interact with the IPFS network.