from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Set your API key (replace with your actual key)
API_KEY = 'YOUR_OLAMA_API_KEY'
OLAMA_URL = 'https://api.olama.com/generate'  # Replace with the actual Olama API URL

# Route to handle text generation requests
@app.route('/generate', methods=['POST'])
def generate_text():
    # Get the prompt from the incoming request
    data = request.get_json()
    prompt = data.get('prompt', '')
    max_tokens = data.get('max_tokens', 100)
    temperature = data.get('temperature', 0.7)

    # Send the prompt to Olama's API for text generation
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': 'olama-llm',  # Replace with the actual model name if needed
        'prompt': prompt,
        'max_tokens': max_tokens,
        'temperature': temperature
    }

    try:
        # Call the Olama API
        response = requests.post(OLAMA_URL, headers=headers, json=payload)
        response.raise_for_status()

        # Return the generated text in the response
        result = response.json()
        return jsonify({'generated_text': result['text']}), 200

    except requests.exceptions.RequestException as e:
        # Handle errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
