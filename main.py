#!/usr/bin/env python3
from flask import Flask, Response, jsonify, request, render_template, send_file, send_from_directory
from flask_bootstrap import Bootstrap
from deploy import deploy
from os import environ
import markdown
import logging
import json
import yaml
import os

log = logging.getLogger(__name__)
app = Flask(__name__)
Bootstrap(app)
# posts = yaml.safe_load(open("posts.yml","r"))
posts = json.load(open("posts.json"))
# sort new
posts.reverse()


def error_handler():
    return app.config.get("DEFAULT_ERROR_MESSAGE") 

@app.route("/robots.txt")
@app.route("/sitemap.xml")
def static_from_root():
    return send_file(request.path[1:])

@app.route("/static/<path:path>", methods=["GET"])
def send_static():
    #return render_template('index.html')
    return send_from_directory('static', path)

@app.route("/demo", methods=["GET"])
def demo():
    #return render_template('index.html')
    return send_from_directory('vizew', 'single-post.html')

#@app.route("/<any({}):post>".format(str( )[1:-1]))
#def posts(post):
#    return "Hello {}!".format(segment)

@app.route("/test", methods=["GET"])
def test():
    #return render_template('index.html')
    with open("static/posts/example.html", "r") as f:
        post_html = f.read()
    return render_template('layout.html', post_html=post_html)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html', posts=posts)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route("/profile", methods=["GET"])
def posts():
    with open(f"pages/profile.html", "r") as f:
        post_html = f.read()
    return render_template('layout.html', post_html=post_html)

@app.route("/posts", methods=["GET"])
def posts():
    post_list = os.listdir('posts')
    return render_template('posts.html', post_list=post_list)

@app.route('/posts/<path:path>')
def send_post(path):
    with open(f"static/posts/{path}", "r") as f:
        post_html = f.read()
    return render_template('layout.html', post_html=post_html)

@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory('vizew', path)

  

@app.route("/blog/<int:pid>", methods=["GET"])
def get_post(pid):
    for p in posts:
        if p['pid'] == pid:
            with open(f"static/posts/{p['file']}") as f:
                content = markdown.markdown(f.read(), extensions=['markdown.extensions.attr_list','markdown.extensions.fenced_code'])
                return render_template('post.html', post_title=p["title"], post_date=p["date"], post_img=p["img"], post_content=content)
    return error_handler()

if __name__ == '__main__':
    #deploy(posts)
    app.run(host='0.0.0.0', port=8080, debug=True)