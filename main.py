#!/usr/bin/env python3
from flask import Flask, Response, jsonify, request, render_template, send_file
from flask_bootstrap import Bootstrap
from deploy import deploy
from os import environ
import markdown
import logging
import json

log = logging.getLogger(__name__)
app = Flask(__name__)
Bootstrap(app)

posts = json.load(open("posts.json"))
# sort new
posts.reverse()


def error_handler():
    return app.config.get("DEFAULT_ERROR_MESSAGE") 

@app.route("/robots.txt")
@app.route("/sitemap.xml")
def static_from_root():
    return send_file(request.path[1:])

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html', posts=posts)

@app.route("/blog/<int:pid>", methods=["GET"])
def get_post(pid):
    for p in posts:
        if p['pid'] == pid:
            with open(f"static/posts/{p['file']}") as f:
                content = markdown.markdown(f.read(), extensions=['markdown.extensions.attr_list','markdown.extensions.fenced_code'])
                return render_template('post.html', post_title=p["title"], post_date=p["date"], post_img=p["img"], post_content=content)
    return error_handler()

if __name__ == '__main__':
    deploy(posts)
    app.run(host='127.0.0.1', port=8080, debug=True)