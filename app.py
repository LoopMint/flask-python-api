from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    user_text = data.get("text", "")
    response = f"Processed: {user_text.upper()}"  # Example logic
    return jsonify({"result": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
