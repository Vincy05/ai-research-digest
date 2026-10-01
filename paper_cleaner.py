def clean_papers(papers: list[dict]) -> list[dict]:
    """Filter out malformed entries, deduplicate by link, and sort newest first."""
    seen_links = set()
    cleaned = []

    for paper in papers:
        # Step 1: skip if title or link is missing/empty
        title= paper.get("title", "").strip()
        link = paper.get("link", "").strip()
        #1. Skip if title/link is empty OR if link was already processed
        if not title or not link or link in seen_links:
            continue

        seen_links.add(link)
        cleaned.append(paper)

    # Step 3: sort newest first
    cleaned.sort(key=lambda p: p["published_date"], reverse=True)

    return cleaned


if __name__ == "__main__":
    from fetcher import fetch_arxiv_papers
    raw = fetch_arxiv_papers("text-to-SQL agents")
    cleaned = clean_papers(raw)
    for p in cleaned:
        print(p["published_date"], "-", p["title"])