import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from paper_cleaner import clean_papers


def test_clean_papers_sorts_newest_first():
    papers = [
        {"title": "Old Paper", "link": "http://a.com", "published_date": "2020-01-01T00:00:00Z"},
        {"title": "New Paper", "link": "http://b.com", "published_date": "2025-01-01T00:00:00Z"},
    ]
    result = clean_papers(papers)
    print("\nTest 1 result:", result)
    assert result[0]["title"] == "New Paper"


def test_clean_papers_removes_duplicates():
    papers = [
        {"title": "Same Paper", "link": "http://a.com", "published_date": "2025-01-01T00:00:00Z"},
        {"title": "Same Paper", "link": "http://a.com", "published_date": "2025-01-01T00:00:00Z"},
    ]
    result = clean_papers(papers)
    print("Test 2 result:", result)
    assert len(result) == 1


def test_clean_papers_drops_malformed_entries():
    papers = [
        {"title": "Good Paper", "link": "http://a.com", "published_date": "2025-01-01T00:00:00Z"},
        {"title": "", "link": "http://b.com", "published_date": "2025-01-01T00:00:00Z"},
        {"title": "No Link", "link": "", "published_date": "2025-01-01T00:00:00Z"},
    ]
    result = clean_papers(papers)
    print("Test 3 result:", result)
    assert len(result) == 1