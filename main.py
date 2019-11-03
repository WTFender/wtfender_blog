#!/usr/bin/env python3
from flask import Flask, request, render_template, send_from_directory
import xml.etree.cElementTree as ET
from datetime import datetime
import logging
import yaml

log = logging.getLogger(__name__)
app = Flask(__name__)

paths = yaml.safe_load(open("paths.yaml","r"))
posts = paths['posts']
pages = paths['pages']

def create_sitemap(posts):
    dt = datetime.now().strftime ("%Y-%m-%d")
    root = ET.Element('urlset')
    root.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
    root.attrib['xsi:schemaLocation']="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    root.attrib['xmlns']="http://www.sitemaps.org/schemas/sitemap/0.9"
    
    doc = ET.SubElement(root, "url")
    ET.SubElement(doc, "loc").text = "https://www.wtfender.com/"
    ET.SubElement(doc, "lastmod").text = dt
    ET.SubElement(doc, "changefreq").text = "weekly"
    ET.SubElement(doc, "priority").text = "1.0"
    
    for p in posts:
        doc = ET.SubElement(root, "url")
        ET.SubElement(doc, "loc").text = f"https://www.wtfender.com/{p}"
        ET.SubElement(doc, "lastmod").text = dt
        ET.SubElement(doc, "changefreq").text = "weekly"
        ET.SubElement(doc, "priority").text = "0.8"
    tree = ET.ElementTree(root)
    tree.write('static/sitemap.xml', encoding='utf-8', xml_declaration=True)

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

# /any('post1', 'post2')
@app.route("/<any({}):path>".format(str(list(posts.keys()))[1:-1]))
def send_post(path):
    return render_template('post.html', post=posts[path])

# /any('page1', 'page2')
# @app.route("/<any({}):path>".format(str(list(pages.keys()))[1:-1]))
# def send_post(path):
#     return render_template('post.html', post=pages[path])

if __name__ == '__main__':
    posts.update(pages)
    create_sitemap(posts)
    app.run(host='0.0.0.0', port=8080, debug=True)