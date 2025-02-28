import socket
import datetime
import sys

port = 8080

def response_message():
    if data[:3] == "GET":
        URI =  data[4 : 4 + data[4:].find(" ")]
        if URI == "/":
            URI = "/index.html"
        URI = URI[1:]
        try:
            with open(URI, "r") as file:
                response = "200 OK\n\n" + file.read()+"\n"
        except FileNotFoundError:
            response = "404 Not Found\n\n404 Not Found\n"
    else:
        response = "501 Not Implemented\n\n501 Not Implemented\n"
    return "HTTP/1.0 "+response

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", port))
server.listen()

while True:
    try:
        client, addr = server.accept()
        data = client.recv(81920).decode("UTF-8")
        with open("server.log", "a") as log:
            log.write(str(datetime.datetime.now()) + "\n" + data + "\n")
        response = response_message()
        client.sendall(response.encode("utf-8"))
        client.close()
    except Exception as e:
        print(e)
        server.close()
        sys.exit()