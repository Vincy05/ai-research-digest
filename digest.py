import argparse
from fetcher import fetch_arxiv_papers
from cleaner import clean_papers
from digest_utils import save_digest

def main():
    parser = argparse.ArgumentParser(description="Fetch a research digest from arXiv on a given topic.")
    parser.add_argument("--topic", type=str, required=True, help="Topic to search for, e.g. 'text-to-SQL agents'")
    parser.add_argument("--max-results", type=int, default=5, help="Number of papers to fetch")
    args = parser.parse_args()

    raw = fetch_arxiv_papers(args.topic, max_results=args.max_results)
    cleaned = clean_papers(raw)
    path = save_digest(cleaned, args.topic)

    print(f"Fetched {len(raw)} papers, kept {len(cleaned)} after cleaning.")
    print(f"Saved digest to: {path}")

if __name__ == "__main__":
    main()