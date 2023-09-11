from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def get_index():
    return render_template('index.html')


@app.route('/blog')
def get_blog():
    return render_template('blog.html')


@app.route('/contact')
def get_contact():
    return render_template('contact.html')


@app.route('/portfolio')
def get_portfolio():
    return render_template('portfolio.html')


@app.route('/resume')
def get_resume():
    return render_template('resume.html')
