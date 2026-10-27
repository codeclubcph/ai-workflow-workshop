"""Minimal HTTP API (standard library only, no extra installs).

Run:  python -m orders.app    (from the src/ folder)
Then: http://localhost:8000/health
      http://localhost:8000/orders?page=1
"""
import json
from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from .delivery import estimated_delivery
from .pagination import paginate

SAMPLE_ORDERS = [{"id": i, "customer": f"customer-{i}"} for i in range(1, 26)]


class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, body: dict) -> None:
        payload = json.dumps(body, default=str).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:  # noqa: N802
        url = urlparse(self.path)
        query = parse_qs(url.query)

        if url.path == "/health":
            self._send(200, {"status": "ok"})
        elif url.path == "/orders":
            page = int(query.get("page", ["1"])[0])
            self._send(200, paginate(SAMPLE_ORDERS, page))
        elif url.path == "/delivery":
            self._send(200, {"estimated": estimated_delivery(date.today())})
        else:
            self._send(404, {"error": "not found"})


def main(port: int = 8000) -> None:
    print(f"Listening on http://0.0.0.0:{port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
