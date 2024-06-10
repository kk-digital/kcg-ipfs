Create a Python module named PythonExecutionEnvironment to execute Python scripts received from the FileCompactorLib in a sandboxed environment and report the result. The module should include a ScriptExecutor class with methods to load and execute the script, capture its output, and handle any errors encountered during execution. Additionally, the module should provide serialization and deserialization functionalities for transmission data, along with unit tests to ensure its correctness.

FileCompactorLib module:
File Class

    Fields:
        file_name (str): Name of the file.
        file_path (str): Path of the file relative to the root folder.
        file_type (str): Type of the file.
        file_length (int): Length of the file in bytes.
        file_hash (str): Blake20 hash of the file.
        file_data_present (bool): Boolean indicating whether the file data is present.
        file_contents (bytes): Byte string containing the file contents (empty if file data is not present).

    Methods:
        __init__(self, file_name: str, file_path: str, file_type: str, file_length: int, file_hash: str, file_data_present: bool, file_contents: bytes) - Initializes the File object with the provided information.
        to_json(self) -> str - Converts the File object to a pretty-printed JSON string.
        from_json(cls, json_str: str) -> 'File' - Deserializes the JSON string and returns a File object.
        validate_hash(self) -> Optional[str] - Validates the file hash. Returns an error string if file data is not present.

FileManager Class

    Fields:
        None

    Methods:
        read_directory(self, directory_path: str) -> List[File] - Reads a directory and creates a list of File objects.
        save_to_zip(self, file_list: List[File], zip_file_path: str) - Saves a collection of File objects to a zip file.
        load_from_zip(self, zip_file_path: str) -> List[File] - Loads a collection of File objects from a zip file.