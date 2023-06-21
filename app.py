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
        son peuple et le ralliement de celui-ci aux rois de l’époque ont permis de créer une vraie  nation unie.   Le pays entre dans l’ère moderne avec la dynastie alaouite. La nation marocaine s’est  dotée de fondements étatiques dont le pouvoir central était entre les mains du Makhzen 13,  d’une diplomatie incarnant l’Ét at et d’une armée nationale.    La prise d’Alger le 5 juillet 1830 a entraîné  le début d’une période tumultueuse au  Maroc. La victoire des Français, ressentie comme  une menace à l’intégrité du pays et à la foi  musulmane au Maghreb, marque le début des hos tilités franco-marocaines. En effet, Moulay  Abderrahmane (1822-1859), le sultan alaouite au pouvoir, vole au secours des habitants de  Tlemcen (Algérie) leur assurant vivres et armes. Les Français répliquent violemment et occupent non seulement la ville de Tlemcen en  1836, mais installent un fort militaire à Lalla  Maghnia, non loin de la ville marocaine d’Oujda.
        '''
        # Perform chatbot processing here
        reply = conv(message,passage)

        response = {'question': message,
                    'passage' : passage,
                    'answer': reply}
        

        return jsonify(response)  # Return response as JSON

    # Render the chat interface
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
