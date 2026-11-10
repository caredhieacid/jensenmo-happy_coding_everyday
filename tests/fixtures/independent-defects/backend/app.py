from backend.auth import authenticate
from gateway.proxy import forward_headers


def handle(headers, via_gateway=True):
    """Entry point used by the server: browser requests arrive through the gateway."""
    if via_gateway:
        headers = forward_headers(headers)
    return authenticate(headers)
