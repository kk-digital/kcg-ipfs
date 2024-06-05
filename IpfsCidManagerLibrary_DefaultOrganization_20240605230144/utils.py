'''
Utility functions for CID Manager Library
'''
import json
def serialize_to_json(obj):
    return json.dumps(obj)
def deserialize_from_json(json_data):
    return json.loads(json_data)