import urllib.request
from bs4 import BeautifulSoup

def fetch_and_print(url):
    try:
        fhand = urllib.request.urlopen(url)
        for line in fhand:
            print(line.decode().strip())
    except Exception as e:
        print(f"Failed to retrieve {url}: {e}")

def find_urls(url):
    try:
        fhand = urllib.request.urlopen(url)
        html = fhand.read().decode()
        soup = BeautifulSoup(html, 'html.parser')

        # Find all URLs in href attributes using BeautifulSoup
        urls = [a['href'] for a in soup.find_all('a', href=True)]
        return urls
    except Exception as e:
        print(f"Failed to retrieve {url}: {e}")
        return []

def main():
    start_url = 'https://www.wikipedia.org/'
    to_visit = [start_url]
    visited = set()

    while to_visit:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue

        print(f"\nFetching and printing content from: {current_url}")
        fetch_and_print(current_url)
        
        visited.add(current_url)

        new_urls = find_urls(current_url)
        for new_url in new_urls:
            if new_url not in visited:
                to_visit.append(new_url)

if __name__ == "__main__":
    main()