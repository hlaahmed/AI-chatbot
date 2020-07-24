from flask import Flask, request, render_template
import Bot
app = Flask(__name__)
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
