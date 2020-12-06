from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def introduce():
    from .data.about import bot
    return render_template('index.html', 
                data=bot,
                question={'key':"name", "text": "How should I call you?"}
            )

@app.route("/message", methods=['POST'])
def user_messsage():
    if request.method == 'POST':
        from .intents import handle
        return handle(request.form)
        return render_template("messages/echo.html", data=request.form)
    else:
        return "INVALID"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)