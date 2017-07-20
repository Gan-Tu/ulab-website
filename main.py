import os
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main-page.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/projects")
def project():
    return render_template("project-template.html")





#################### Main App #####################
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True