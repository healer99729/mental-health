from flask import Flask, request, render_template

from app.api import api_bp
from app.extensions import MENTAL_HEALTH_GPT

chat_history = []


def create_app():
    app = Flask(__name__)
    @app.route('/', methods=['GET', 'POST'])
    def chat():
        if request.method == 'POST':
            user_message = request.form['message']
            chat_history.append({'type': 'user', 'message': user_message})
            
            # Simulate a server response
            server_response = MENTAL_HEALTH_GPT(user_message)[:len(user_message)]
            chat_history.append({'type': 'server', 'message': server_response})

        return render_template('index.html', chat_history=chat_history)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
