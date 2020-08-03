from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import speech_recognition as sr
import Bot


app = Flask(__name__)
ENV = 'prod'
if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/user-responses'
else:
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgres://kcnrkscjpofvmw:27fa3f56086364422e130fbfca88ad36e551bc76bf1b1fcb6326428a0bf2e905@ec2-52-202-66-191.compute-1.amazonaws.com:5432/d12frn1u7p3tna'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    phone = db.Column(db.VARCHAR(200), unique=True)
    phone_company = db.Column(db.String(200))
    internet_service = db.Column(db.String(200))

    def __init__(self, name, phone, phone_company, internet_service):
        self.name = name
        self.phone = phone
        self.phone_company = phone_company
        self.internet_service = internet_service


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def chat():
        request_data = request.args.get('msg')
        response = Bot.chat(request_data)
        return str(response)


if __name__ == "__main__":
    app.run()

