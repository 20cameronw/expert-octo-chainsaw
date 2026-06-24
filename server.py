#!/usr/bin/env python3
"""
Pickle Face Tracker — local web server
Run:  python server.py
Then open http://localhost:8000 in Chrome / Edge.
"""

import os
import sys
import http.server
import socketserver

PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    """Serve static files with minimal headers."""

    def end_headers(self):
        # Disable caching so changes to index.html are picked up immediately
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):  # silence request noise
        pass


def main():
    global PORT
    if len(sys.argv) == 3 and sys.argv[1] in ("--port", "-p"):
        PORT = int(sys.argv[2])

    # Always serve from the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("🥒  Pickle Face Tracker")
    print("=" * 42)
    print(f"   http://localhost:{PORT}")
    print("   Press Ctrl+C to stop")
    print("=" * 42)

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.allow_reuse_address = True
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋  Server stopped.")
    except OSError as exc:
        print(f"\n❌  Could not bind to port {PORT}: {exc}")
        print(f"   Try:  python server.py --port 8080")
        sys.exit(1)


if __name__ == "__main__":
    main()
