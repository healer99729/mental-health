from flask import Flask, render_template, request, url_for

app = Flask(__name__)
chat_history = []  # This will store the chat history

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.form['message']
        chat_history.append({'type': 'user', 'message': user_message})
        
        # Simulate a server response
        server_response = "Echo: " + user_message  # Here, customize the response logic as needed
        chat_history.append({'type': 'server', 'message': server_response})

    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run()