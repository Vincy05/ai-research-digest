import streamlit as st
from fetcher import fetch_arxiv_papers
from paper_cleaner import clean_papers
from digest_utils import save_digest

st.title("AI Research Digest")

topic = st.text_input("Topic", value="text-to-SQL agents")
max_results = st.slider("Number of papers", min_value=1, max_value=20, value=5)

if st.button("Fetch Digest"):
    with st.spinner("Fetching papers..."):
        raw = fetch_arxiv_papers(topic, max_results=max_results)
        cleaned = clean_papers(raw)
        path = save_digest(cleaned, topic)

    st.success(f"Found {len(cleaned)} papers. Saved to {path}")

    for paper in cleaned:
        st.subheader(paper["title"])
        st.write(", ".join(paper["authors"]))
        st.write(paper["abstract"])
        st.markdown(f"[Read paper]({paper['link']})")
        st.divider()