import socket
import threading
import json
import time

class P2P:
    def __init__(self, port, label):
        self.host = "127.0.0.1"
        self.port = port
        self.label = label
        self.peers = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))

    def start(self):
        threading.Thread(target=self.listen, daemon=True).start()
        print(f"Node {self.label} online on port {self.port}")
    
    def listen(self):
        self.server.listen(5)
        while True:
            connection , address = self.server.accept()
            threading.Thread(target=self.handle_connection, args=(connection, address), daemon=True).start()
    
    def handle_connection(self, connection, address):
        try:
            data = connection.recv(1024).decode('utf-8')
            message = json.loads(data)
            print(f"\n[{self.label}] Recieved from {message['sender']}: {message['content']}")
            print("> ", end="")
        except:
            pass
        finally:
            connection.close()
    
    def send_message(self, target_port, content):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.host, target_port))

            payload = {
                "sender": self.label,
                "content": content,
                "timestamp": time.time()
            }
            client.send(json.dumps(payload).encode('utf-8'))
            client.close()
        except:
            print(f"\n[Error] Node on port {target_port} not found.")

if __name__ == "__main__":
    import sys

    # Pede as configurações iniciais
    my_door = int(input("In which door will this node run on? (ex: 5000): "))
    my_name = input("Whats your name?: ")

    # Inicia o nó
    node = P2P(my_door, my_name)
    node.start()

    time.sleep(1) # Pequena pausa para o servidor subir

    print(f"\n--- Commands: 'send' to send a message or 'exit' to end communication ---")

    while True:
        comando = input("> ").strip().lower()
        
        if comando == "send":
            target = int(input("Porta do destino: "))
            msg = input("Mensagem: ")
            node.send_message(target, msg)
        elif comando == "exit":
            break