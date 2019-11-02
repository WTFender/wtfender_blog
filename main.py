#!/usr/bin/env python3
from flask import Flask, Response, jsonify, request, render_template, send_file, send_from_directory
#from flask_bootstrap import Bootstrap
from deploy import deploy
from os import environ
import markdown
import logging
import json
import yaml
import os

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
    return render_template('layout.html', html='home page')

@app.route("/test")
def send_test():
    #return render_template('index.html')
    with open("posts/example.html", "r") as f:
        post_html = f.read()
    return render_template('layout.html', html=post_html)

@app.route("/profile")
def send_profile():
    with open(f"pages/profile.html", "r") as f:
        post_html = f.read()
    return render_template('layout.html', html=post_html)

@app.route("/<any({}):path>".format(str(post_paths)[1:-1]))
def send_post(path):
    for p in posts:
        if p['Link'] == path:
            with open(f"posts/{p['File']}", "r") as f:
                post_html = f.read()
    return render_template('layout.html', html=post_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)