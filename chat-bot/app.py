from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
# Update CORS settings to allow all origins
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    }
})

# Initialize DeepSeek client
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

@app.route('/')
def serve_chat_interface():
    return send_from_directory('static', 'chat-interface.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    try:
        # Log the API key (first few characters)
        api_key = os.getenv("DEEPSEEK_API_KEY")
        logger.debug(f"API Key (first 5 chars): {api_key[:5] if api_key else 'None'}")
        
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful KPI dashboard assistant. Provide concise, relevant answers about dashboard metrics and insights."
                },
                {
                    "role": "user", 
                    "content": user_message
                }
            ]
        )
        
        return jsonify({
            "response": response.choices[0].message.content
        })
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == '__main__':
    # Verify API key is loaded
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        logger.error("No DeepSeek API key found!")
    else:
        logger.info("API key loaded successfully")
    
    app.run(debug=True, host='0.0.0.0', port=5001) 