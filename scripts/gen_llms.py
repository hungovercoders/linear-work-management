#!/usr/bin/env python3
"""Generate docs/llms.txt and docs/llms-full.txt, the guide as plain text for agents.

The site's pages use cards, tabs and collapsed sections that suit people. An agent fetching
a URL is better served by plain Markdown, so this flattens every page in the nav:

  llms.txt       an index: each page's title, URL and opening line
  llms-full.txt  every page in nav order, with the component markup reduced to text

Both are build outputs (git-ignored) and are published at the site root.

    task llms      # or: python scripts/gen_llms.py
"""
import pathlib
import posixpath
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://hungovercoders.github.io/linear-work-management/"


def nav_pages() -> list[str]:
    """The .md paths under `nav:` in mkdocs.yml, in order."""
    text = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    nav = text[text.index("\nnav:"):]
    return re.findall(r"([\w./-]+\.md)\s*$", nav, re.MULTILINE)


def url_for(page: str) -> str:
    if page == "index.md":
        return SITE
    if page.endswith("/index.md"):
        return SITE + page[: -len("index.md")]
    return SITE + page[: -len(".md")] + "/"


def absolute_links(text: str, page: str) -> str:
    """Rewrite relative links to .md pages (and site files) as full site URLs."""
    base = posixpath.dirname(page)

    def fix(m: re.Match) -> str:
        target = m.group(2)
        if re.match(r"[a-z]+:|#", target):
            return m.group(0)
        path, _, anchor = target.partition("#")
        path = posixpath.normpath(posixpath.join(base, path))
        url = url_for(path) if path.endswith(".md") else SITE + path
        return f"{m.group(1)}({url}{'#' + anchor if anchor else ''})"

    return re.sub(r"(\[[^\]]*\])\(([^)\s]+)\)", fix, text)


def flatten(text: str, page: str) -> str:
    """Reduce a guide page to plain Markdown."""
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.DOTALL)           # front matter
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)                    # comments
    text = re.sub(r"^\s*!\[([^\]]*)\]\([^)]*\)\s*$", r"Diagram: \1", text, flags=re.MULTILINE)

    out, dedent = [], False
    for line in text.split("\n"):
        block = re.match(r'^(\?\?\?\+?|!!!|===)\s+(?:\w+\s+)?"([^"]*)"', line)
        if block:                                   # a collapsed note, callout or tab
            out.append(f"**{block.group(2)}**")
            dedent = True
            continue
        if dedent and line.startswith("    "):
            line = line[4:]
        elif dedent and line.strip():
            dedent = False
        out.append(line)
    text = "\n".join(out)

    text = re.sub(r'<span class="lwm-(?:kicker|for)">(.*?)</span>', r"\1: ", text)
    text = re.sub(r"\{\s*\.lwm-name\s*\}", ": ", text)                      # level names
    text = re.sub(r"<b>(.*?)</b>", r"**\1** ", text)
    text = re.sub(r"<small>(.*?)</small>", r" (\1)", text)
    text = re.sub(r"<code>(.*?)</code>", r"`\1`", text)
    text = re.sub(r"<li[^>]*>", "- ", text)
    text = re.sub(r"</(?:div|li|a|p)>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)                                        # remaining tags
    text = re.sub(r"\{\s*[.#][^}]*\}", "", text)                               # attribute lists
    text = re.sub(r":(?:material|octicons)-[a-z0-9-]+:\s*", "", text)          # icons
    text = absolute_links(text, page)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def title_and_lead(flat: str) -> tuple[str, str]:
    title = re.search(r"^# (.+)$", flat, re.MULTILINE)
    body = flat[title.end():] if title else flat
    lead = ""
    for para in re.split(r"\n\s*\n", body):
        para = " ".join(para.split())
        if para and not para.startswith(("#", "Diagram:", "**", "[", "|", "-")) and not para.endswith(":"):
            lead = re.split(r"(?<=[.!?])\s", re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", para))[0]
            break
    return (title.group(1).strip() if title else ""), lead


def main() -> int:
    pages = nav_pages()
    index = ["# Linear Ways of Working", "",
             "> How we use Linear: initiatives, projects, issues and BAU, the five rules, and the "
             "skills that apply them. Written for people and for agents.", "",
             "## The model as data", "",
             f"- [model.yml]({SITE}model.yml): states, labels, SLAs, cadences, thresholds and what an agent may do",
             f"- [llms-full.txt]({SITE}llms-full.txt): every page below in one file", "",
             "## Pages", ""]
    full = []
    for page in pages:
        flat = flatten((DOCS / page).read_text(encoding="utf-8"), page)
        title, lead = title_and_lead(flat)
        index.append(f"- [{title}]({url_for(page)})" + (f": {lead}" if lead else ""))
        full.append(f"<!-- {url_for(page)} -->\n\n{flat}")
    (DOCS / "llms.txt").write_text("\n".join(index) + "\n", encoding="utf-8")
    (DOCS / "llms-full.txt").write_text("\n\n---\n\n".join(full), encoding="utf-8")
    print(f"Wrote docs/llms.txt and docs/llms-full.txt ({len(pages)} page(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
