import xml.etree.cElementTree as ET
from datetime import datetime


def deploy(posts):
    print("new deployment")
    create_sitemap(posts)

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
        ET.SubElement(doc, "loc").text = f"https://www.wtfender.com/blog/{p['pid']}"
        ET.SubElement(doc, "lastmod").text = dt
        ET.SubElement(doc, "changefreq").text = "weekly"
        ET.SubElement(doc, "priority").text = "0.8"
    tree = ET.ElementTree(root)
    tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)