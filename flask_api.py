from flask import Flask, request, jsonify
from model_training import predict_intent

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    intent = predict_intent(user_input)
    return jsonify({'intent': intent})

if __name__ == '__main__':
    app.run(debug=True)
