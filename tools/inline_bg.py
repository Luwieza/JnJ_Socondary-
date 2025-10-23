#!/usr/bin/env python3
"""
Inline the Johnson & Johnson building image into styles.css as a base64 data URL.

Usage: Run from anywhere; script uses project-relative paths.
It finds the first background-image: url(...) in recociliator/static/styles.css,
loads that local file under recociliator/static/, and replaces just that url(...)
with a data URI. If the CSS points to a remote URL, it will not inline it.
"""
from __future__ import annotations
import base64
import mimetypes
from pathlib import Path
import sys
import re
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
CSS_PATH = ROOT / "recociliator/static/styles.css"
STATIC_DIR = ROOT / "recociliator/static"


def main() -> int:
    if not CSS_PATH.exists():
        print(f"ERROR: CSS not found: {CSS_PATH}")
        return 1

    css = CSS_PATH.read_text(encoding="utf-8")

    # Find the first background-image URL (supports quotes or no quotes)
    m = re.search(r"background-image:\s*url\(([^)]+)\)", css)
    if not m:
        print("WARNING: No background-image URL found to replace in styles.css. No changes made.")
        return 2

    raw_url = m.group(1).strip()
    # Strip surrounding quotes if present
    if (raw_url.startswith("\"") and raw_url.endswith("\"")) or (raw_url.startswith("'") and raw_url.endswith("'")):
        raw_url = raw_url[1:-1]

    # Ignore data URIs or remote URLs
    if raw_url.startswith("data:"):
        print("INFO: Background already inlined as data URI. Nothing to do.")
        return 0
    if raw_url.startswith("http://") or raw_url.startswith("https://"):
        print("WARNING: Background URL is remote. Please point it to a local file under recociliator/static/ then re-run.")
        return 2

    # Resolve the local file path (relative to static dir)
    local_rel = urllib.parse.unquote(raw_url)
    local_path = (STATIC_DIR / local_rel).resolve()

    if not local_path.exists():
        print(f"ERROR: Local background image not found: {local_path}\n"
              f"Ensure the CSS points to an existing file under recociliator/static/.")
        return 1

    mime, _ = mimetypes.guess_type(str(local_path))
    if not mime:
        mime = "application/octet-stream"

    data = local_path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    data_url = f"data:{mime};base64,{b64}"

    # Replace only the matched url(...) portion with the data URL
    start, end = m.span(1)
    new_css = css[:start] + f"'{data_url}'" + css[end:]

    CSS_PATH.write_text(new_css, encoding="utf-8")
    print("SUCCESS: Inlined image into styles.css")
    return 0


if __name__ == "__main__":
    sys.exit(main())
