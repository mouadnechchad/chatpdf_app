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

        # print(data['msg'])

        passage = '''
        became a destination for many British and American diplomats, spies, writers , and  businessmen . Consequently, English was the language of communication between the  different nationalities settled in Tangiers.     b.  The American landings:       The second major event was during the Second World War  when thousands of American  soldiers landed in Morocco and established some military bases in Casablanca,  Kenitra , and  Tangiers. This event is considered to be the most important historical link between Moroccans  and English (Ennaji, 2005); it dates back to 1942 when the U.S.A decided to condu ct military  landings on Morocco to prepare for a future attack on Southern Europe. These landings were  a part of Operation Torch intended to put an end to the Nazis (militaryhistory.about.com ).  Accordin gly, it became  familiar to hear English in the major cities of Morocco as the  American soldiers stayed there. There was a huge interaction between Moroccans and the  American soldiers to
        '''
        # Perform chatbot processing here
        reply = conv(message,passage)

        response = {'question': message,
                    'answer': reply}
        

        return jsonify(response)  # Return response as JSON

    # Render the chat interface
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
