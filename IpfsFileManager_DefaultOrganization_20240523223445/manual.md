# ChatDev Python Tool User Manual

## Introduction

Welcome to the user manual for the ChatDev Python Tool! This tool is designed to help you manage and analyze Python files in a given directory. It provides functionality for reading files, calculating file hashes, and serializing/deserializing data to JSON format.

## Table of Contents

1. Installation
2. Usage
3. File Structure
4. Unit Testing
5. Dependencies

## 1. Installation

To install the ChatDev Python Tool, follow these steps:

1. Clone the repository from GitHub: `git clone https://github.com/ChatDev/Python-Tool.git`
2. Navigate to the project directory: `cd Python-Tool`
3. Install the required dependencies: `pip install -r requirements.txt`

## 2. Usage

To use the ChatDev Python Tool, follow these steps:

1. Open the terminal or command prompt.
2. Navigate to the project directory: `cd Python-Tool`
3. Run the main.py file with the desired folder directory as a parameter: `python main.py <folderDir>`
   - Replace `<folderDir>` with the path to the directory containing the Python files you want to analyze.
4. The tool will calculate the file hashes using the Blake2 algorithm and store the data in the PythonFile class.
5. The output, a serialized JSON file, will be saved in the `/output` folder.

## 3. File Structure

The ChatDev Python Tool consists of the following files:

- `main.py`: The main script that accepts the folder directory parameter and performs the file analysis.
- `file_manager.py`: The FileManager class that handles file operations, serialization, and saving JSON files.
- `python_file.py`: The PythonFile class that represents a Python file and stores its attributes.
- `test/`: The folder containing unit tests for the tool.

## 4. Unit Testing

The ChatDev Python Tool includes unit tests to ensure the correctness of its functionality. To run the unit tests, follow these steps:

1. Open the terminal or command prompt.
2. Navigate to the project directory: `cd Python-Tool`
3. Run the unit test file: `python -m unittest discover -s test`
4. The unit tests will execute, and the results will be displayed in the terminal.

## 5. Dependencies

The ChatDev Python Tool requires the following dependencies:

- `json`: A Python library for working with JSON data.
- `hashlib`: A Python library for cryptographic hashing algorithms.

These dependencies are listed in the `requirements.txt` file and will be installed automatically during the installation process.

If you encounter any issues or have any questions, please don't hesitate to reach out to our support team at support@chatdev.com.

Happy coding with the ChatDev Python Tool!