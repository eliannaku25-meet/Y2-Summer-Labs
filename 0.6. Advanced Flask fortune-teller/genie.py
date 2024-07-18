from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

fortunes = {
    "January": "This year brings new beginnings and fresh starts. Embrace the changes.",
    "February": "Love and friendship will flourish this year. Keep an open heart.",
    "March": "New opportunities will come your way. Be ready to seize them.",
    "April": "This is a year of growth and renewal. Focus on personal development.",
    "May": "Expect positive changes in your career. Your hard work will pay off.",
    "June": "Adventure and excitement are in store for you. Enjoy the ride.",
    "July": "This is a year to focus on family and home. Cherish the moments.",
    "August": "You will find inspiration in unexpected places. Stay curious.",
    "September": "New learning experiences await you. Embrace the knowledge.",
    "October": "This year is about balance and harmony. Seek peace in all areas.",
    "November": "Transformation and change are on the horizon. Be adaptable.",
    "December": "Joy and celebration will fill your days. Share your happiness."
}


@app.route('/home', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('home.html')

    input_month = request.form['birthmonth']
    for x in fortunes.keys():
        if x == input_month:
            return redirect(url_for('fortuneFinder', month=input_month))

    return redirect(url_for('error'))

@app.route('/fortune/<month>')
def fortuneFinder(month):
    return render_template("fortune.html", fortune=fortunes[month])

@app.route('/error')
def error():
    return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
