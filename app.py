from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "TruthLens backend is connected!"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)