from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import Bot
import utilis
app = Flask(__name__)
ENV = 'prod'
if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/user-responses'
else:
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgres://bxijrzoulienmx:d7ea14adda8f72fc343d3d1aaf34a6044a3f6e69389b3e3f4a0799996cd28674@ec2-107-20-15-85.compute-1.amazonaws.com:5432/d70vhv0b3kvgjr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.String(200), unique=True)

    def __init__(self, response):
        self.response = response
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def chat():
    flag = True
    while (flag == True):
        user_response = request.args.get('msg')
        utilis.save(user_response)
        user_response = user_response.lower()
        if (user_response != 'bye'):
            if (user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                response = "You are welcome.."
                return response
            else:
                if (Bot.greeting(user_response) != None):
                    response = Bot.greeting(user_response)
                    return response
                else:

                    response = Bot.response(user_response)
                    Bot.sent_tokens.remove(user_response)
                    return response
        else:
            flag = False
            response = "Bye! take care, and if you want to say anything more you can leave a voice mail"
            return response

if __name__ == "__main__":
    app.run()
