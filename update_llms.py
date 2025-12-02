import xml.etree.ElementTree as ET
import sys
import os
import requests

def update_llms_txt():
    sitemap_url = "https://a2a-protocol.org/latest/sitemap.xml"
    llms_txt_path = os.path.join(os.path.dirname(__file__), "llms.txt")

    print(f"Fetching sitemap from {sitemap_url}...")
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        xml_content = response.content
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        raise

    root = ET.fromstring(xml_content)
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    urls = []
    for url in root.findall('ns:url', namespace):
        loc = url.find('ns:loc', namespace).text
        if loc:
            urls.append(loc)

    print(f"Found {len(urls)} URLs.")

    # Categorize URLs for better llms.txt structure
    categories = {
        "Protocol Overview": [],
        "Detailed Topics": [],
        "Tutorials": [],
        "SDKs": [],
        "Specification": [],
        "Community & Roadmap": [],
        "Other": []
    }

    for url in urls:
        name = url.rstrip('/').split('/')[-1].replace('-', ' ').title()
        if not name: name = "Home"

        entry = f"- [{name}]({url})"

        if "topics" in url:
            categories["Detailed Topics"].append(entry)
        elif "tutorials" in url:
            categories["Tutorials"].append(entry)
        elif "sdk" in url:
            categories["SDKs"].append(entry)
        elif "specification" in url or "definitions" in url:
            categories["Specification"].append(entry)
        elif "community" in url or "roadmap" in url or "partners" in url:
            categories["Community & Roadmap"].append(entry)
        else:
            categories["Other"].append(entry)

    # Write llms.txt
    with open(llms_txt_path, 'w') as f:
        f.write("# A2A Protocol Documentation\n\n")
        f.write("> Documentation and specifications for the Agent2Agent (A2A) Protocol.\n")
        f.write("> Automatically generated from sitemap.xml.\n\n")

        for category, entries in categories.items():
            if entries:
                f.write(f"## {category}\n")
                for entry in sorted(entries):
                    f.write(f"{entry}\n")
                f.write("\n")

    print(f"Successfully updated {llms_txt_path}")

if __name__ == "__main__":
    update_llms_txt()
