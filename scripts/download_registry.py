"""Download every record of the APKG registry as JSON (one file per record),
optionally with its CWL, and optionally convert them to RDF with json2rdf.py.

Instructions: see README.md in this folder.
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_URL = "https://iliad-registry.inesctec.pt/collections/apkg/items"


def get(url, accept="application/json", retries=3):
    req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": "apkg-ldap-download/2.0"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8")
        except Exception as e:
            if attempt == retries - 1:
                raise
            print(f"   retrying ({e})")
            time.sleep(2 * (attempt + 1))


def with_params(url, **params):
    parts = urllib.parse.urlsplit(url)
    q = dict(urllib.parse.parse_qsl(parts.query))
    q.update({k: str(v) for k, v in params.items()})
    return urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(q)))


def next_link(page):
    for l in page.get("links") or []:
        if l.get("rel") == "next" and l.get("href"):
            return l["href"]
    return None


def safe_name(rid):
    name = re.sub(r"^urn:apkg:", "", rid)
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name)


def main():
    ap = argparse.ArgumentParser(description="Download all APKG registry records as JSON.")
    ap.add_argument("-o", "--output", default=str(ROOT / "examples" / "json"),
                    help="folder for the JSON files (default: examples/json)")
    ap.add_argument("--url", default=DEFAULT_URL, help="items endpoint of the registry collection")
    ap.add_argument("--limit", type=int, default=100, help="records requested per page (the server may return fewer)")
    ap.add_argument("--fast", action="store_true",
                    help="keep the records as given in the listing pages, without downloading each record; "
                         "faster, but the listing does not include the links of the records")
    ap.add_argument("--with-cwl", action="store_true",
                    help="also download each record's CWL (?f=cwl) and store it in the field 'cwl', "
                         "so that json2rdf.py can extract the secrets")
    ap.add_argument("--convert", action="store_true",
                    help="after downloading, run json2rdf.py on the files (Turtle and JSON-LD, then validation)")
    ap.add_argument("--rdf-output", default=str(ROOT / "examples"),
                    help="output folder for --convert (default: examples/)")
    args = ap.parse_args()

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    url = with_params(args.url, f="json", limit=args.limit)
    seen, offset, total = set(), 0, None
    while url:
        print(f"page: {url}")
        page = json.loads(get(url))
        features = page.get("features") or []
        total = page.get("numberMatched", total)
        for rec in features:
            rid = rec.get("id") or (rec.get("properties") or {}).get("identifier")
            if not rid or rid in seen:
                continue
            seen.add(rid)
            item_url = f"{args.url}/{urllib.parse.quote(rid, safe=':')}"
            if not args.fast:  # the full record (with its links) is only given by the record's own URL
                try:
                    rec = json.loads(get(with_params(item_url, f="json")))
                except Exception as e:
                    print(f"   could not download the full record {rid} (kept the listing version): {e}")
            if args.with_cwl:
                cwl_url = (rec.get("properties") or {}).get("url") or with_params(item_url, f="cwl")
                try:
                    rec.setdefault("properties", {})["cwl"] = get(cwl_url, accept="application/cwl+yaml, text/plain, */*")
                except Exception as e:
                    print(f"   could not download the CWL of {rid}: {e}")
            target = out / f"{safe_name(rid)}.json"
            target.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"   {len(features)} records (total so far: {len(seen)}{f' of {total}' if total else ''})")
        if not features:
            break
        offset += len(features)
        nxt = next_link(page)
        if nxt:
            url = nxt
        else:  # no "next" link: page with offset until all records are read
            if total is not None and offset >= total:
                break
            url = with_params(args.url, f="json", limit=args.limit, offset=offset)

    print(f"\n{len(seen)} records saved in {out}")
    if total is not None and len(seen) != total:
        print(f"warning: the registry reports {total} records")

    if args.convert and seen:
        print("\nConverting with json2rdf.py\n---------------------------")
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import json2rdf
        sys.argv = ["json2rdf.py", str(out), "--format", "both", "-o", args.rdf_output]
        return json2rdf.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
