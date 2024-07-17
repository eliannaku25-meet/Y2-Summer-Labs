from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/home')
def hello_world():
    return render_template("home.html")

@app.route('/fortune')
def fortuneFinder():
    fortunes = [
        "You will have a great day today!",
        "A new opportunity will come your way.",
        "Someone will surprise you with a kind gesture.",
        "You will overcome a challenge you are facing.",
        "Good news is on its way to you.",
        "You will make a new friend soon.",
        "An old friend will reach out to you.",
        "You will achieve something you've been working hard on.",
        "Your hard work will soon pay off.",
        "You will find joy in unexpected places."
    ]
    fortNum = random.randint(0, len(fortunes))
    
    return render_template("fortune.html", fortune=fortunes[fortNum])

if __name__ == '__main__':
    app.run(debug=True)
