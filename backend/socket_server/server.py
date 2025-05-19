import socket
import threading
import json

class BasicHTTPServer:
     def __init__(self, host='127.0.0.1', port=8000):
          self.host = host
          self.port = port
          self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
          self.socket.bind((self.host, self.port))

     def start(self):
          self.socket.listen(5)
          print(f"Server started on http://{self.host}:{self.port}")

          try:
               while True:
                    client_socket, address = self.socket.accept()
                    client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
                    client_thread.daemon = True
                    client_thread.start()
          except KeyboardInterrupt:
               print("Server shutting down")
          finally:
               self.socket.close()
     
     def handle_client(self, client_socket, address):
          print(f"Connection from {address}")
          try:
               request_data = client_socket.recv(1024).decode('utf-8')
               if not request_data:
                    return
               
               # Parse the HTTP request to get the path
               request_line = request_data.split('\r\n')[0]
               method, path, _ = request_line.split(' ')

               # Handle different endpoints
               if path == '/':
                    response = self.handle_home()
               elif path == '/api/message':
                    response = self.handle_message()
               else:
                    response = self.handle_not_found()
               
               client_socket.sendall(response.encode('utf-8'))
          except Exception as e:
               print(f"Error handling client: {e}")
          finally:
               client_socket.close()
     
     def handle_home(self):
          content = "<html><body><h1>Basic Socket Server</h1><p> Try the  /api/message endpoint</p></body></html>"
          return self.create_response(content, content_type="text/html")
     
     def handle_message(self):
          data = {"message": "Hello from Python Socket Server!"}
          return self.create_response(json.dumps(data), content_type="application/json")
     
     def handle_not_found(self):
          content = "<html><body><h1>404 Not Found</h1></body></html>"
          return self.create_response(content, status="404 Not Found")
          
     def create_response(self, content, status="200 OK", content_type="text/html"):
          response = f"HTTP/1.1 {status}\r\n"
          response += f"Content-Type: {content_type}\r\n"
          response += "Access-Control-Allow-Origin: *\r\n"
          response += f"Content-Length: {len(content)}\r\n"
          response += "\r\n"
          response += content
          return response
     
if __name__ == "__main__":
     server = BasicHTTPServer()
     server.start()
          




