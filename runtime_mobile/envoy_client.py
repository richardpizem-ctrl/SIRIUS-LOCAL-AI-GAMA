import json
from http.client import HTTPConnection, HTTPException
from urllib.parse import urlencode


def lookup_beta_entity(entity):
    entity = entity.strip()
    if not entity or len(entity) > 120:
        return {'status': 'invalid_input'}
    connection = HTTPConnection('127.0.0.1', 8766, timeout=2)
    try:
        connection.request('GET', '/v1/kg/entity?' + urlencode({'entity': entity}))
        response = connection.getresponse()
        if response.status != 200:
            return {'status': 'error', 'http_status': response.status}
        body = response.read(32769)
        if len(body) > 32768:
            return {'status': 'error', 'reason': 'response_too_large'}
        return json.loads(body)
    except (OSError, HTTPException):
        return {'status': 'unavailable', 'message': 'Most BETA je nedostupny.'}
    except ValueError:
        return {'status': 'error', 'reason': 'invalid_response'}
    finally:
        connection.close()
