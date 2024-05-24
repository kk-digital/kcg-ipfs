# HTTP Request Wrapper Library

The HTTP Request Wrapper library is a Python library that provides a convenient way to handle HTTP requests and responses. It includes a `Request` class for representing an HTTP request, a `Response` class for representing an HTTP response, and an `HTTPRequestWrapper` class for serializing and deserializing requests and responses.

## Installation

To install the HTTP Request Wrapper library, you can use pip or conda. Open your terminal and run one of the following commands:

```shell
pip install http-request-wrapper
```

or

```shell
conda install -c conda-forge http-request-wrapper
```

## Usage

### Request Class

The `Request` class represents an HTTP request and has the following fields:

- `UUID` (uint64): The unique identifier for the request.
- `RequestPath` (string): The path of the request.
- `RequestParameters` (string): The parameters of the request.
- `RequestTimeSent` (timedate): The time when the request was sent.
- `RequestServerAddress` (string): The server address of the request.
- `RequestRoute` (string): The route of the request.
- `RequestBody` ([]byte): The body of the request.

#### Creating a Request Object

To create a `Request` object, you can use the following code:

```python
from http_request_wrapper import Request
from datetime import datetime

request = Request(
    UUID=123456789,
    RequestPath='/api',
    RequestParameters='param1=value1&param2=value2',
    RequestTimeSent=datetime.now(),
    RequestServerAddress='http://example.com',
    RequestRoute='/api/route',
    RequestBody=b'{"key": "value"}'
)
```

#### Serializing a Request Object to JSON

To serialize a `Request` object to JSON, you can use the `to_json()` method:

```python
request_json = request.to_json()
print(f'Request JSON: {request_json}')
```

### Response Class

The `Response` class represents an HTTP response and has the following fields:

- `ResponseErrorString` (string): The error string of the response.
- `ResponseHttpCode` (int): The HTTP code of the response.
- `ResponseBody` ([]byte): The body of the response.
- `RequestTimeStart` (timedate): The time when the request started.
- `RequestTimeFinished` (timedate): The time when the request finished.
- `RequestCompletedTime` (float): The time taken to complete the request.

#### Creating a Response Object

To create a `Response` object, you can use the following code:

```python
from http_request_wrapper import Response

response = Response(
    ResponseErrorString='Error',
    ResponseHttpCode=200,
    ResponseBody=b'Response body',
    RequestTimeStart=datetime(2022, 1, 1, 10, 0, 1),
    RequestTimeFinished=datetime(2022, 1, 1, 10, 0, 2),
    RequestCompletedTime=1.0
)
```

#### Serializing a Response Object to JSON

To serialize a `Response` object to JSON, you can use the `to_json()` method:

```python
response_json = response.to_json()
print(f'Response JSON: {response_json}')
```

### HTTPRequestWrapper Class

The `HTTPRequestWrapper` class provides functions for serializing and deserializing requests and responses.

#### Serializing a Request Object to JSON

To serialize a `Request` object to JSON using the `HTTPRequestWrapper` class, you can use the `serialize_request()` method:

```python
from http_request_wrapper import HTTPRequestWrapper

http_wrapper = HTTPRequestWrapper()
http_request_json = http_wrapper.serialize_request(request)
print(f'HTTP Request JSON: {http_request_json}')
```

#### Deserializing a Response JSON to a Response Object

To deserialize a response JSON to a `Response` object using the `HTTPRequestWrapper` class, you can use the `deserialize_response()` method:

```python
http_response = http_wrapper.deserialize_response(response_json)
print(f'HTTP Response: {http_response}')
```

## Unit Tests

The HTTP Request Wrapper library includes unit tests for the `Request`, `Response`, and `HTTPRequestWrapper` classes. These tests use randomly generated data and include assertions to ensure the correctness of the library.

To run the unit tests, you can use the following command:

```shell
python -m unittest discover
```

## Conclusion

The HTTP Request Wrapper library provides a convenient way to handle HTTP requests and responses in Python. It includes classes for representing requests and responses, as well as a wrapper class for serializing and deserializing them. The library also includes unit tests to ensure its correctness.