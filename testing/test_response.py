import io

from http_parser.http import HttpStream


def test_204_no_content():
    stream = io.BytesIO(b'HTTP/1.1 204 No Content\r\n\r\n')
    response = HttpStream(stream)
    assert response.status_code() == 204
    assert response.body_string() == b''
