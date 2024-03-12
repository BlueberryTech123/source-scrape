import requests
import os

# INSECURLY: https://insecurly.vercel.app
print("Scraping insecurly...")
url = "https://insecurly.vercel.app"

page = requests.get(url)
open("index.html", "w").write(page.content.decode())
os.system("python -m http.server 8000")