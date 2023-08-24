import http.server
import socketserver
import os

count_file = "visit_count.txt"  # 存储访问次数的文件名

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/get_count"):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(str(self.get_count()).encode())
        elif self.path.startswith("/update_count"):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(str(self.update_count()).encode())
        else:
            super().do_GET()

    def get_count(self):
        try:
            with open(count_file, "r") as file:
                count = file.read()
                return int(count) if count.strip().isdigit() else 0
        except FileNotFoundError:
            return 0

    def update_count(self):
        count = self.get_count() + 1
        with open(count_file, "w") as file:
            file.write(str(count))
        return count

PORT = 8000

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
