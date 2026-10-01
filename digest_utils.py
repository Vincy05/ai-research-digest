import json
import os
from datetime import date

def save_digest(papers: list[dict], topic: str, output_dir: str = "digests") -> str:
    os.makedirs(output_dir, exist_ok=True)

    safe_topic = topic.lower().replace(" ","-")       # replace spaces with hyphens, e.g. "text-to-sql-agents"
    filename = f"{output_dir}/{date.today()}_{safe_topic}.json"

    with open(filename, "w") as f:
        json.dump(papers,f, indent = 2) # write papers to f as JSON

    return filename


if __name__ == "__main__":
    from fetcher import fetch_arxiv_papers
    from cleaner import clean_papers

    raw = fetch_arxiv_papers("text-to-SQL agents")
    cleaned = clean_papers(raw)
    path = save_digest(cleaned, "text-to-SQL agents")
    print(f"Saved to: {path}")