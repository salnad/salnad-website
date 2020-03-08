from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == "__main__":
    app.run(debug=True)