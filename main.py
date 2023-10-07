from flask import Flask, render_template, request
import requests
from mail_sender import SendMail

response = requests.get(url="https://api.npoint.io/df923a4a07ef17cbdc3d")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=response.json())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    get_h1 = f"Contact Me"
    post_h1 = f"Successfully sent your message"
    if request.method == 'GET':
        return render_template("contactv2.html", h1=get_h1)
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        SendMail(name=name, email=email, phone=phone, message=message)
        return render_template("contactv2.html", h1=post_h1)


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template("post.html", post=response.json()[post_id - 1])


@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    print(f"{name}\n{email}\n{phone}\n{message}")
    return f"<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
