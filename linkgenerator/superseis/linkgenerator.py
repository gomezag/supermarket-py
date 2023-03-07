import requests
from bs4 import BeautifulSoup

def main():
    base_url = "https://www.superseis.com.py/"
    response = requests.get(base_url)

    soup = BeautifulSoup(response.text, "html.parser")

    all_a = soup.find_all("a")
    seen_links = set()

    for link in all_a:
        href = link.get("href")
        if href is not None and href not in seen_links and 'category' in href:
            seen_links.add(href)
            resp = requests.post('http://localhost:8000/api/link/', data={'supermarket': 1, 'url': href})

main()