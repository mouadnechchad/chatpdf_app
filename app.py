from flask import Flask, render_template, request, jsonify
from langchain_conv import *

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Perform authentication here
        # You can add your own logic to validate the username and password
        
        # For demonstration purposes, let's assume the login is successful
        return render_template('chat.html', username=username)
    
    # Render the login form
    return render_template('login.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        # Handle chat form submission
        print(request.form)
        data = request.get_json()
        message = data['msg']

        print(data['msg'])
        # Perform chatbot processing here
        # You can integrate with a chatbot API or implement your own logic
        reply = conv(message)

        # For demonstration purposes, let's echo the user's message

        response = {'question': message,
                    'answer': reply}
        

        return jsonify(response)  # Return response as JSON

    # Render the chat interface
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
