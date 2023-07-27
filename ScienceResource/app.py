from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/topics')
def topics():  # put application's code here
    return render_template("topics.html")


@app.route('/about')
def about():  # put application's code here
    return render_template("about.html")


@app.route('/contact')
def contact():  # put application's code here
    return render_template("contact.html")


@app.route('/Physics/index.html')
def phys():  # put application's code here
    return render_template("/Physics/index.html")


@app.route('/Astronomy/index.html')
def astro():  # put application's code here
    return render_template("/Astronomy/index.html")


@app.route('/Astronomy/Kepler1.html')
def kep1():  # put application's code here
    return render_template("/Astronomy/kepler1.html")


@app.route('/CS/index.html')
def CS():  # put application's code here
    return render_template("/CS/index.html")


@app.route('/Physics/vectorScalar.html')
def vect():  # put application's code here
    return render_template("/Physics/vectorScalar.html")


@app.route('/study')
def study():  # put application's code here
    return render_template("study.html")


if __name__ == '__main__':
    app.run()
