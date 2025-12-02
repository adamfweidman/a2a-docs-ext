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
        print("Using provided sitemap content for demonstration if fetch fails...")
        # Fallback to the content provided by the user if the fetch fails
        xml_content = """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://a2a-protocol.org/latest/</loc></url>
<url><loc>https://a2a-protocol.org/latest/community/</loc></url>
<url><loc>https://a2a-protocol.org/latest/definitions/</loc></url>
<url><loc>https://a2a-protocol.org/latest/partners/</loc></url>
<url><loc>https://a2a-protocol.org/latest/roadmap/</loc></url>
<url><loc>https://a2a-protocol.org/latest/specification/</loc></url>
<url><loc>https://a2a-protocol.org/latest/sdk/</loc></url>
<url><loc>https://a2a-protocol.org/latest/sdk/python/</loc></url>
<url><loc>https://a2a-protocol.org/latest/topics/a2a-and-mcp/</loc></url>
<url><loc>https://a2a-protocol.org/latest/topics/agent-discovery/</loc></url>
<url><loc>https://a2a-protocol.org/latest/topics/enterprise-ready/</loc></url>
<url><loc>https://a2a-protocol.org/latest/topics/extensions/</loc></url>
<url><loc>https://a2a-protocol.org/latest/topics/key-concepts/</loc></url>
<url><loc>https://a2a-protocol.org/latest/topics/life-of-a-task/</loc></url>
<url><loc>https://a2a-protocol.org/latest/topics/streaming-and-async/</loc></url>
<url><loc>https://a2a-protocol.org/latest/topics/what-is-a2a/</loc></url>
<url><loc>https://a2a-protocol.org/latest/tutorials/</loc></url>
<url><loc>https://a2a-protocol.org/latest/tutorials/python/1-introduction/</loc></url>
<url><loc>https://a2a-protocol.org/latest/tutorials/python/2-setup/</loc></url>
<url><loc>https://a2a-protocol.org/latest/tutorials/python/3-agent-skills-and-card/</loc></url>
<url><loc>https://a2a-protocol.org/latest/tutorials/python/4-agent-executor/</loc></url>
<url><loc>https://a2a-protocol.org/latest/tutorials/python/5-start-server/</loc></url>
<url><loc>https://a2a-protocol.org/latest/tutorials/python/6-interact-with-server/</loc></url>
<url><loc>https://a2a-protocol.org/latest/tutorials/python/7-streaming-and-multiturn/</loc></url>
<url><loc>https://a2a-protocol.org/latest/tutorials/python/8-next-steps/</loc></url>
</urlset>"""

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
