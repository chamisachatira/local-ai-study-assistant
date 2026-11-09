from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests for any external app or website

# TODO: Initialize your local RAG / Ollama chatbot pipeline here
# from rag_engine import query_local_ai

@app.route('/api/chat', methods=['POST'])
def universal_chat_api():
    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({
                "status": "error",
                "message": "Invalid request. 'message' field is required."
            }), 400

        user_message = data.get('message')

        # --- REPLACE WITH YOUR ACTUAL RAG / OLLAMA LOGIC ---
        ai_response = f"AI Assistant received: {user_message}"
        # ---------------------------------------------------

        return jsonify({
            "status": "success",
            "query": user_message,
            "response": ai_response,
            "source": "Local RAG AI Assistant"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "model": "llama3.2"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)