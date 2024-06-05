# CID Manager Library User Manual

## Introduction

The CID Manager Library is a Python library that provides functionality for managing CID (Content Identifier) data. It allows you to create and manage a list of CIDData objects, serialize them to JSON files, and deserialize them from JSON files.

This user manual will guide you through the installation process, explain the main functions of the library, and provide examples of how to use it.

## Installation

To use the CID Manager Library, you need to have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can install the CID Manager Library using pip, the Python package installer. Open a terminal or command prompt and run the following command:

```
pip install cid-manager
```

This will download and install the library and its dependencies.

## Getting Started

To get started with the CID Manager Library, you need to import the necessary classes and functions from the library. Here's an example:

```python
from cid_manager import CidManager, CidData
```

## CidData Class

The CidData class represents a CID data object. It has two fields: `Cid` and `Hash`. The `Cid` field is a string that represents the CID, and the `Hash` field is a SHA256 hash of the CID.

To create a new CidData object, you can use the following code:

```python
cid_data = CidData("Cid1", "Hash1")
```

## CidManager Class

The CidManager class is used to manage a list of CIDData objects. It has the following methods:

### add_cid_data(cid, hash)

This method adds a new CIDData object to the list. It takes two parameters: `cid` (string) and `hash` (string).

Example:

```python
cid_manager = CidManager()
cid_manager.add_cid_data("Cid1", "Hash1")
```

### serialize_cid_data(output_dir="./output")

This method serializes the list of CIDData objects to JSON files. It takes an optional parameter `output_dir` that specifies the output directory for the JSON files. The default value is "./output".

The JSON files are named after the hash of each CIDData object, and they are saved in folders named "Cid" followed by a folder count with 4-digit padding.

If the size of the output folder exceeds 500MB, a new folder is created and the remaining JSON files are saved in the new folder. This process is repeated whenever the folder size exceeds 500MB.

Example:

```python
cid_manager = CidManager()
cid_manager.add_cid_data("Cid1", "Hash1")
cid_manager.serialize_cid_data()
```

### deserialize_cid_data(input_dir="./output")

This method deserializes a list of CIDData objects from JSON files. It takes an optional parameter `input_dir` that specifies the input directory containing the JSON files. The default value is "./output".

The method returns a list of CIDData objects.

Example:

```python
cid_manager = CidManager()
cid_data_list = cid_manager.deserialize_cid_data()
```

## Testing

The CID Manager Library includes unit tests for all its methods. To run the tests, you can use the following command:

```
python -m unittest discover
```

This will run all the tests and display the results.

## Conclusion

The CID Manager Library provides a convenient way to manage CID data in your Python projects. By using the CidManager class and its methods, you can easily add, serialize, and deserialize CIDData objects. The library also includes unit tests to ensure the correctness of its functionality.

We hope this user manual has provided you with the necessary information to use the CID Manager Library effectively. If you have any further questions or need assistance, please don't hesitate to contact us.

Happy coding!
```