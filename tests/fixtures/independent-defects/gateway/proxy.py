HOP_BY_HOP = {"connection", "keep-alive", "transfer-encoding", "upgrade"}


def forward_headers(headers):
    """Headers to send on to the backend. Names are normalized for the HTTP/2 upstream."""
    return {name.lower(): value for name, value in headers.items() if name.lower() not in HOP_BY_HOP}
