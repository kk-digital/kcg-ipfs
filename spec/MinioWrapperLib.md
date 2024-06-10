Create a Python library named MinioWrapperLib to provide an HTTP interface for Minio. This library enables functionalities such as listing files in a directory, reading files, and benchmarking speed. It optimizes for high-performance retrieval of large batches of Variational Autoencoders (VAEs) and images, typically used in machine learning tasks. The library leverages the HttpNetLib module for server functionalities and operates in read-only mode, without write access to Minio.

HttpNetLib Module docs

    Fields:
        None

    Classes:
        HttpServerManager - Manages HTTP servers.
        HttpClientManager - Manages HTTP clients.

HttpServerManager Class

    Fields:
        None

    Methods:
        get_server_list() -> List[Dict[str, Union[str, int]]] - Retrieves a list of HTTP servers and their ports along with the interfaces they are served on.

HttpClientManager Class

    Fields:
        None

    Methods:
        Methods for managing HTTP clients, such as sending requests, handling responses, etc.