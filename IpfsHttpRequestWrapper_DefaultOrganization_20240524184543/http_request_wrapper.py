'''
This file contains the implementation of the HTTP Request Wrapper library.
'''
import json
from datetime import datetime
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return super().default(obj)
class Request:
    """
    Represents an HTTP request.
    """
    def __init__(self, UUID, RequestPath, RequestParameters, RequestTimeSent, RequestServerAddress, RequestRoute, RequestBody):
        self.UUID = UUID
        self.RequestPath = RequestPath
        self.RequestParameters = RequestParameters
        self.RequestTimeSent = RequestTimeSent
        self.RequestServerAddress = RequestServerAddress
        self.RequestRoute = RequestRoute
        self.RequestBody = RequestBody
    def to_json(self):
        """
        Serialize the Request object to JSON.
        """
        data = self.__dict__.copy()
        data['RequestBody'] = self.RequestBody.decode('utf-8')
        return json.dumps(data, cls=CustomJSONEncoder)
    @staticmethod
    def from_json(json_data):
        """
        Deserialize the JSON data to a Request object.
        """
        data = json.loads(json_data)
        # Convert RequestTimeSent to datetime object
        data['RequestTimeSent'] = datetime.strptime(data['RequestTimeSent'], '%Y-%m-%d %H:%M:%S')
        return Request(**data)
class Response:
    """
    Represents an HTTP response.
    """
    def __init__(self, ResponseErrorString, ResponseHttpCode, ResponseBody, RequestTimeStart, RequestTimeFinished, RequestCompletedTime):
        self.ResponseErrorString = ResponseErrorString
        self.ResponseHttpCode = ResponseHttpCode
        self.ResponseBody = ResponseBody
        self.RequestTimeStart = RequestTimeStart
        self.RequestTimeFinished = RequestTimeFinished
        self.RequestCompletedTime = RequestCompletedTime
    def to_json(self):
        """
        Serialize the Response object to JSON.
        """
        return json.dumps(self.__dict__, cls=CustomJSONEncoder)
    @staticmethod
    def from_json(json_data):
        """
        Deserialize the JSON data to a Response object.
        """
        data = json.loads(json_data)
        return Response(**data)
class HTTPRequestWrapper:
    """
    Wrapper class for HTTP requests.
    """
    def serialize_request(self, request):
        """
        Serialize the Request object to JSON.
        """
        return request.to_json()
    def deserialize_response(self, response_json):
        """
        Deserialize the JSON data to a Response object.
        """
        return Response.from_json(response_json)