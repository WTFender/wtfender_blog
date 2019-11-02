#!/usr/bin/env python3
from flask import Flask, request, render_template, send_from_directory
#from deploy import deploy
import logging
import yaml

log = logging.getLogger(__name__)
app = Flask(__name__)

posts = yaml.safe_load(open("posts.yml","r"))
post_paths = []
for p in posts:
    post_paths.append(p['Link'])

def error_handler():
    return app.config.get("DEFAULT_ERROR_MESSAGE") 

@app.route("/robots.txt")
@app.route("/sitemap.xml")
def send_robots():
    return send_from_directory('static', request.path[1:])

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory('static', path)

@app.route("/")
def send_home():
    return render_template('home.html', posts=posts)

@app.route("/<any({}):path>".format(str(post_paths)[1:-1]))
def send_post(path):
    for p in posts:
        if p['Link'] == path:
            with open(f"posts/{p['File']}", "r") as f:
                post_html = f.read()
                print(post_html)
    return render_template('post.html', html=post_html)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)