import json
from bson import ObjectId
from datetime import datetime, timezone


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.replace(tzinfo=timezone.utc).timestamp()
        return json.JSONEncoder.default(self, o)


def encode_and_decode(data):
    return json.loads(json.dumps(data, cls=JSONEncoder))
