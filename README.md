# AI Research Digest

A command-line tool that fetches recent research papers on a given topic from arXiv, cleans and structures the results, and saves them as a dated JSON digest.

## What problem does this solve?
Manually checking arXiv for new papers on a specific topic (e.g. text-to-SQL agents) is repetitive. This tool automates that check into a single command.

## How does it work?
1. `fetcher.py` queries the arXiv API for a given topic
2. `cleaner.py` removes malformed/duplicate entries and sorts by newest first
3. `digest_utils.py` saves the cleaned results as a dated JSON file
4. `digest.py` ties these together into a CLI

## Setup

    python3 -m venv venv
    source venv/bin/activate      # Windows: venv\Scripts\activate
    pip install -r requirements.txt

## Usage

    python3 digest.py --topic "text-to-SQL agents"
    python3 digest.py --topic "prompt engineering" --max-results 3

Output is saved to `digests/<date>_<topic>.json`.

## What data does it use?
Public arXiv API (no key required): http://export.arxiv.org/api/query

## Known limitations
- arXiv only — no other sources yet
- No LLM-based summarization yet (planned for Stage 05)
- Sorting relies on arXiv's `published` date string

## What's next
- Markdown digest export
- Streamlit UI
- LLM-generated one-line summaries per paper (Stage 05)