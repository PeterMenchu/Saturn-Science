from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/simulations/drop.html', methods=["POST", "GET"])
def drop():  # put application's code here
    return render_template("simulations/drop.html")

@app.route("/<data>")
def res(data):
    return f"<h1>{data}</h1>"

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

# Physics
@app.route('/Physics/index.html')
def phys():  # put application's code here
    return render_template("/Physics/index.html")

@app.route('/Physics/vectorScalar.html')
def vect():  # put application's code here
    return render_template("/Physics/vectorScalar.html")

# astro section
@app.route('/Astronomy/index.html')
def astro():  # put application's code here
    return render_template("/Astronomy/index.html")


@app.route('/Astronomy/Kepler1.html')
def kep1():  # put application's code here
    return render_template("/Astronomy/kepler1.html")

# CS section
@app.route('/CS/index.html')
def CS():  # put application's code here
    return render_template("/CS/index.html")

# Software section
@app.route('/Software')
def software():  # put application's code here
    return render_template("/Software/index.html")
@app.route('/Software/agile')
def agile():  # put application's code here
    return render_template("/Software/agile.html")


@app.route('/study')
def study():  # put application's code here
    return render_template("study.html")

@app.route('/simulations/index.html')
def simulations():  # put application's code here
    return render_template("simulations/index.html")


if __name__ == '__main__':
    app.run()
