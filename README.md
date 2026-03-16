# Simple P2P Messenger (Python)

A lightweight decentralized peer-to-peer (P2P) communication system. Each node acts as both a Server (listening for incoming messages) and a Client (sending messages to other nodes).



## 🛠️ Features
- **Full-Duplex Communication:** Nodes can send and receive data simultaneously using Python's `threading` library.
- **TCP Protocol:** Ensures reliable data delivery and maintains message order.
- **JSON Serialization:** Structured data exchange including sender ID, message content, and timestamps.
- **Dynamic Port Binding:** Users can define their own port and label at runtime.

## 🚀 How to Run
1. Open at least two terminal windows.
2. Run the script in both terminals: `python3 main.py`
3. Terminal 1 (Node A):
   - Port: 5000
   - Name: Alfa 
4. Terminal 2 (Node B):
   - Port: 5001
   - Name: Beta
5. In Terminal 2, type `send`, then enter port `5000` to message Node A.



## 📚 Technical Logic
- **`listen()`**: Runs on a daemon thread to avoid blocking the user interface. It accepts new connections and spawns a handler thread for each.
- **`handle_connection()`**: Decodes the byte stream, parses JSON, and prints the message to the console.
- **`send_message()`**: Creates a temporary socket to connect to a target peer, sends the payload, and closes the connection.