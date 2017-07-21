import os
from flask import Flask, render_template, url_for, redirect
import content

app = Flask(__name__)

navProjects = [
    {
        "url": "/projects/{}".format(x), 
        "name": content.research[x]["navbar"]
    } for x in content.research
][1:]


@app.context_processor
def utility_processor():
    return dict(navProjects=navProjects)

@app.route("/")
def index():
    return render_template("main-page.html")

@app.route("/aboutus")
def aboutus():
    c = content.team.copy()
    for p in c:
        c[p]['img'] = url_for('static', filename=c[p]['img'])
    return render_template("aboutus.html", team=c)

@app.route("/project")
@app.route("/project/<name>")
@app.route("/projects")
@app.route("/projects/<name>")
def project(name="placeholder"):
    c = content.research[name].copy()
    c['img'] = url_for('static', filename=c['img'])
    return render_template("projects.html", content=c)

##################### Error Handling #####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

#################### Main App #####################
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True