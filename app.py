from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder = "static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/therapy")
def therapy():
    return render_template("therapy.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)