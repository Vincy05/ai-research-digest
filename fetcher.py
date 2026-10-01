import requests
import feedparser
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def fetch_arxiv_papers(query: str, max_results: int = 5) -> list[dict]:
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results={max_results}"
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        logger.error(f"Failed to reach arXiv: {e}")
        return []

    feed = feedparser.parse(response.text)
    papers = []
    for entry in feed.entries:
        papers.append({
        "title": entry.title,
        "authors": [a["name"] for a in entry.authors],
        "abstract": entry.summary.strip(),
        "published_date": entry.published,
        "link": entry.link,
    })
    return papers

if __name__ == "__main__":
    results = fetch_arxiv_papers("text-to-SQL agents")
    print(f"Found {len(results)} papers\n")
    for paper in results:
        print(paper["title"])
        print(paper["published_date"])
        print(paper["link"])
        print()