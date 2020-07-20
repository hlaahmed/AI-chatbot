from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
app = Flask(__name__)
bot = ChatBot("Python-BOT")
trainer = ListTrainer(bot)
trainer.train(['i want to call 01**', 'i am establishing a connection'])
trainer.train(['01** is busy', 'do you want to leave him a message?'])
trainer.train(['yup, it is urgent', 'ok start recording your message and i will save it'])
trainer.train(['it can wait i will call him later', 'as you like'])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
if __name__ == "__main__":
    app.run()
