"""
This is a basic backend server
to experiment with AJAX and jQuery requests.
This server receives an application/json content-type
and mirror that content to the client.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any


class Handler(BaseHTTPRequestHandler):
    def set_header(self, status_code: int = 200) -> None:
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, POST, PUT, DELETE, OPTIONS",
        )
        self.end_headers()

    def set_response(self, context: dict[str, Any]) -> None:
        self.wfile.write(json.dumps(context).encode())

    def read_body(self) -> dict[str, Any]:
        content_length = int(self.headers.get("Content-Length", "0"))
        body_content = self.rfile.read(content_length)
        body_json = json.loads(body_content)
        return body_json

    def do_GET(self):
        self.set_header()
        self.set_response({"message": "Hello AJAX GET"})

    def do_POST(self):
        request_data = self.read_body()
        self.set_header(201)
        self.set_response(request_data)

    def do_OPTIONS(self):
        self.set_header()
        self.set_response({"message": "Hello AJAX OPTION"})


HTTPServer(("localhost", 8000), Handler).serve_forever()
