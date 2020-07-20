from flask import Flask, render_template, request
from rivescript import RiveScript
import os.path
file = os.path.dirname(__file__)
Brain = os.path.join(file, 'Brain')
Bot = RiveScript()
Bot.load_directory(Brain)
Bot.sort_replies()
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(Bot.reply('localuser', userText))
if __name__ == "__main__":
    app.run()
