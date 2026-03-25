"""PubMed Paper Search — Search 36M+ biomedical papers with zero setup."""
import requests
import csv
import argparse

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def search(term, limit=10, email=None):
    params = {"db": "pubmed", "term": term, "retmode": "json", "retmax": limit, "sort": "relevance"}
    if email:
        params["email"] = email
    r = requests.get(f"{BASE}/esearch.fcgi", params=params)
    data = r.json()["esearchresult"]
    return int(data["count"]), data["idlist"]

def fetch_details(ids, email=None):
    params = {"db": "pubmed", "id": ",".join(ids), "retmode": "json"}
    if email:
        params["email"] = email
    r = requests.get(f"{BASE}/esummary.fcgi", params=params)
    results = r.json()["result"]
    papers = []
    for pmid in ids:
        if pmid in results:
            p = results[pmid]
            papers.append({
                "pmid": pmid,
                "title": p.get("title", ""),
                "authors": ", ".join(a["name"] for a in p.get("authors", [])[:5]),
                "journal": p.get("source", ""),
                "date": p.get("pubdate", ""),
                "doi": next((eid["value"] for eid in p.get("articleids", []) if eid["idtype"] == "doi"), "")
            })
    return papers

def export_csv(papers, filename="pubmed_results.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["pmid", "title", "authors", "journal", "date", "doi"])
        writer.writeheader()
        writer.writerows(papers)

def main():
    parser = argparse.ArgumentParser(description="Search PubMed — 36M+ biomedical papers")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--email", help="Your email (recommended by NCBI)")
    parser.add_argument("--csv", help="Export to CSV")
    args = parser.parse_args()

    total, ids = search(args.query, args.limit, args.email)
    print(f"\nFound {total:,} papers for '{args.query}'\n")
    
    if ids:
        papers = fetch_details(ids, args.email)
        for i, p in enumerate(papers, 1):
            print(f"{i}. [{p['pmid']}] {p['title']}")
            print(f"   {p['authors']} | {p['journal']} | {p['date']}\n")
        if args.csv:
            export_csv(papers, args.csv)
            print(f"Exported to {args.csv}")

if __name__ == "__main__":
    main()
