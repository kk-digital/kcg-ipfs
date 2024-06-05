# CID Manager Library

The CID Manager Library is a Python library that provides functionality for managing CID data. It includes a `CidData` class to represent CID data and a `CidManager` class to manage a list of CID data entries.

## Installation

To install the CID Manager Library, you can use pip:

```
pip install cid-manager
```

## Usage

### CidData Class

The `CidData` class represents a CID data entry. It has two fields: `Cid` (string) and `Hash` (SHA256 hash).

```python
from cid_manager import CidData

# Create a CidData object
cid_data = CidData("Cid1", "Hash1")

# Access the fields
print(cid_data.Cid)  # Output: Cid1
print(cid_data.Hash)  # Output: Hash1
```

### CidManager Class

The `CidManager` class manages a list of CID data entries. It provides methods to add CID data entries, serialize the list of CID data to JSON files, and deserialize CID data from JSON files.

```python
from cid_manager import CidManager

# Create a CidManager object
cid_manager = CidManager()

# Add CID data entries
cid_manager.add_cid_data("Cid1", "Hash1")
cid_manager.add_cid_data("Cid2", "Hash2")
cid_manager.add_cid_data("Cid3", "Hash3")

# Serialize CID data to JSON files
cid_manager.serialize_cid_data()

# Deserialize CID data from JSON files
cid_data_list = cid_manager.deserialize_cid_data()

# Access the deserialized CID data
for cid_data in cid_data_list:
    print(cid_data.Cid, cid_data.Hash)
```

### Testing

The CID Manager Library includes unit tests for all methods of the `CidManager` class. To run the tests, you can use the pytest framework.

```bash
pytest
```

The tests include a specific test case for serializing 10MB worth of CID data to the "./output" folder.

## Dependencies

The CID Manager Library has the following dependencies:

- Python 3.6+
- hashlib
- json
- os

You can install the dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Conclusion

The CID Manager Library provides a convenient way to manage CID data. It includes classes for representing CID data and managing a list of CID data entries. The library also includes unit tests to ensure the correctness of its functionality.