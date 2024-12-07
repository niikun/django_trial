from socket import *
def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))  # ポート9000にバインド
        serversocket.listen(5)
        print("Server started at http://localhost:9000")
        while True:
            (clientsocket, address) = serversocket.accept()
            print(f"Connection from {address}")  # 接続元のアドレスを表示
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(f"Request: {pieces[0]}")

            # HTTPレスポンスを返す
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        serversocket.close()
        print("Server shut down.")

print('Access http://localhost:9000')
createServer()