'''
This is the main file that will be executed to run the HTTP Request Wrapper library.
'''
from http_request_wrapper import Request, Response, HTTPRequestWrapper
from datetime import datetime
def main():
    # Create a sample Request object
    request = Request(
        UUID=123456789,
        RequestPath='/api',
        RequestParameters='param1=value1&param2=value2',
        RequestTimeSent=datetime.now(),
        RequestServerAddress='http://example.com',
        RequestRoute='/api/route',
        RequestBody=b'{"key": "value"}'
    )
    # Serialize the Request object to JSON
    request_json = request.to_json()
    print(f'Request JSON: {request_json}')
    # Create a sample Response JSON
    response_json = '''
    {
        "ResponseErrorString": "Error",
        "ResponseHttpCode": 200,
        "ResponseBody": "Response body",
        "RequestTimeStart": "2022-01-01 10:00:01",
        "RequestTimeFinished": "2022-01-01 10:00:02",
        "RequestCompletedTime": 1.0
    }
    '''
    # Deserialize the Response JSON to a Response object
    response = Response.from_json(response_json)
    print(f'Response: {response}')
    # Create an HTTPRequestWrapper object
    http_wrapper = HTTPRequestWrapper()
    # Serialize the Request object to JSON using the HTTPRequestWrapper
    http_request_json = http_wrapper.serialize_request(request)
    print(f'HTTP Request JSON: {http_request_json}')
    # Deserialize the Response JSON to a Response object using the HTTPRequestWrapper
    http_response = http_wrapper.deserialize_response(response_json)
    print(f'HTTP Response: {http_response}')
if __name__ == '__main__':
    main()