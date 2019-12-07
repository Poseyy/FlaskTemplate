from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/', methods = ['POST'])
def search():
    text = request.form['test']
    #generate(text)
    path = 'static/images/placeholder'
    return path

@app.route('/search')
def about():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)