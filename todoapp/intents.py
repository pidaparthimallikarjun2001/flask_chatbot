name = ''
def get_intent(data):
    global name
    m = data['message'].lower()
    if data['key'] == "name":
        name = m
        return "next"
    if any(x in m for x in ["game", "play", "tic tac toe"]):
        return "game"
    if any(x in m for x in ["tell me a quote", "quote"]):
        return "quote" 
    if(m == "who are you?"):
        return "who"
    if(m == "what can you do?"):
        return "what"
    if any(x in m for x in ["thanks", "thank you"]):
        return "thanks"
    elif "fetch" in m:
        return "fetch"
    else:
        return "echo"


def handle(data):
    global name
    from flask import render_template
    intent = get_intent(data)
    if intent == "thanks":
        return render_template("messages/thanks.html", name = name, question = {'key':'next', 'description': 'What would you like me to do?'})
    if intent == "who":
        return render_template("messages/whoareyou.html", name = name, question = {'key':'next', 'description': 'What would you like me to do?'})
    if intent == "what":
        return render_template("messages/whatcanyoudo.html", name = name, question = {'key':'next', 'description': 'What would you like me to do?'})
    if intent == "quote":
        return render_template("messages/quote.html", name = name, question = {'key':'next', 'description': 'What would you like me to do?'})
    elif intent == "next":
        return render_template('messages/greet.html', name = name,
        question = {'key':'next', 'description': 'What would you like me to do?'}) 
    else:
        return render_template("messages/defaultreply.html", data = data, question = {'key':'next', 'description': 'What would you like me to do?'})