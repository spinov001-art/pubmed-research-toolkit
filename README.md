# PubMed Research Toolkit

Search 36M+ biomedical papers using PubMed's free E-utilities API. No API key required.

## Features

- Search papers by keyword, author, journal, MeSH terms
- Fetch paper details (title, authors, abstract, journal, dates)
- Track drug research trends over time
- Monitor clinical trials by disease/drug
- Export to CSV for analysis
- Zero setup — no API key needed

## Quick Start

```bash
pip install requests
python search_pubmed.py "machine learning cancer" --limit 10
```

## Usage

```python
import requests

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
params = {"db": "pubmed", "term": "CRISPR", "retmode": "json", "retmax": 5}
data = requests.get(url, params=params).json()
print(f"Found {data['esearchresult']['count']} papers about CRISPR")
```

## Related

- [OpenAlex Research Toolkit](https://github.com/spinov001-art/openalex-research-toolkit) — 250M+ papers across all fields
- [Full tutorial on Dev.to](https://dev.to/0012303/pubmed-has-a-free-api-search-36m-medical-papers-programmatically-1in3)
- [77 Web Scrapers on Apify](https://apify.com/knotless_cadence)

## License
MIT

---
*Built by [AI Entrepreneur](https://spinov001-art.github.io)*
