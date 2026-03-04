#!/usr/bin/env python3
"""
Preprocess Markdown whitepapers and compile to LaTeX-quality PDFs via pandoc.
Matches typesetting style of the first 4 published academic papers.
"""

import re
import subprocess
import sys
import os
import tempfile
from pathlib import Path

# ── Paper definitions ──────────────────────────────────────────────────────────

PAPERS = [
    {
        "md": "Probabilistic_Identity_Whitepaper.md",
        "pdf": "Probabilistic_Identity_Resolution.pdf",
        "title": "Probabilistic Identity Resolution: The Privacy-First Identity Graph",
        "shorttitle": "Probabilistic Identity Resolution",
        "subtitle": "Resolving Discontinuous Customer Journeys via Weighted Clustering and Household-Level Linkage",
        "author": "Michael F. Robinson",
        "date": "January 31, 2026",
        "subject": "Data Engineering, Graph Data Science",
        "keywords": "identity resolution, probabilistic matching, graph clustering, attribution",
    },
    {
        "md": "Live_Event_Attribution_Whitepaper.md",
        "pdf": "Live_Event_Attribution.pdf",
        "title": "Live Event Attribution: Real-Time Causal Inference for High-Velocity Environments",
        "shorttitle": "Live Event Attribution",
        "subtitle": "Streaming Attribution in Sub-Second Decision Windows",
        "author": "Michael F. Robinson",
        "date": "January 31, 2026",
        "subject": "Marketing Analytics, Real-Time Systems",
        "keywords": "live events, real-time attribution, causal inference, streaming",
    },
    {
        "md": "Real_Time_Streaming_Whitepaper.md",
        "pdf": "Real_Time_Streaming_Attribution.pdf",
        "title": "Real-Time Streaming Attribution: Sub-Second Decision Architecture",
        "shorttitle": "Real-Time Streaming Attribution",
        "subtitle": "Kafka-Native Attribution at Scale",
        "author": "Michael F. Robinson",
        "date": "January 31, 2026",
        "subject": "Data Engineering, Stream Processing",
        "keywords": "streaming, Kafka, real-time, attribution, lambda architecture",
    },
    {
        "md": "Incrementality_Testing_Whitepaper.md",
        "pdf": "Incrementality_Testing_Framework.pdf",
        "title": "Incrementality Testing: The Randomized Holdout Framework",
        "shorttitle": "Incrementality Testing",
        "subtitle": "Causal Lift Measurement via Geo-Experiments and Synthetic Control",
        "author": "Michael F. Robinson",
        "date": "January 31, 2026",
        "subject": "Causal Inference, Experimental Design",
        "keywords": "incrementality, holdout testing, causal lift, geo-experiments",
    },
    {
        "md": "Marketing_Data_Connectors_Whitepaper.md",
        "pdf": "Marketing_Data_Connectors.pdf",
        "title": "Marketing Data Connectors: Unified API Architecture for Attribution",
        "shorttitle": "Marketing Data Connectors",
        "subtitle": "Standardized Ingestion Layer for Cross-Platform Attribution Data",
        "author": "Michael F. Robinson",
        "date": "January 31, 2026",
        "subject": "Data Engineering, API Architecture",
        "keywords": "data connectors, API integration, ETL, marketing data, attribution",
    },
    {
        "md": "MMM_Incrementality_Bridge_Whitepaper.md",
        "pdf": "MMM_Incrementality_Bridge.pdf",
        "title": "The MMM-Incrementality Validation Bridge",
        "shorttitle": "MMM-Incrementality Bridge",
        "subtitle": "Cross-Validating Media Mix Models with Causal Holdout Experiments",
        "author": "Michael F. Robinson",
        "date": "January 31, 2026",
        "subject": "Marketing Analytics, Causal Inference",
        "keywords": "MMM, incrementality, validation, media mix modeling, causal inference",
    },
]

# ── Preprocessing ──────────────────────────────────────────────────────────────

BOX_DRAWING_MAP = {
    # Horizontals
    "\u2500": "-",  # ─
    "\u2501": "=",  # ━
    "\u2550": "=",  # ═
    # Verticals
    "\u2502": "|",  # │
    "\u2503": "|",  # ┃
    "\u2551": "|",  # ║
    # Corners
    "\u250c": "+",  # ┌
    "\u250d": "+",  # ┍
    "\u250e": "+",  # ┎
    "\u250f": "+",  # ┏
    "\u2510": "+",  # ┐
    "\u2511": "+",  # ┑
    "\u2512": "+",  # ┒
    "\u2513": "+",  # ┓
    "\u2514": "+",  # └
    "\u2515": "+",  # ┕
    "\u2516": "+",  # ┖
    "\u2517": "+",  # ┗
    "\u2518": "+",  # ┘
    "\u2519": "+",  # ┙
    "\u251a": "+",  # ┚
    "\u251b": "+",  # ┛
    # T-shapes
    "\u251c": "+",  # ├
    "\u251d": "+",  # ┝
    "\u251e": "+",  # ┞
    "\u251f": "+",  # ┟
    "\u2520": "+",  # ┠
    "\u2524": "+",  # ┤
    "\u252c": "+",  # ┬
    "\u2534": "+",  # ┴
    "\u253c": "+",  # ┼
    # Double
    "\u2554": "+",  # ╔
    "\u2557": "+",  # ╗
    "\u255a": "+",  # ╚
    "\u255d": "+",  # ╝
    "\u2560": "+",  # ╠
    "\u2563": "+",  # ╣
    "\u2566": "+",  # ╦
    "\u2569": "+",  # ╩
    "\u256c": "+",  # ╬
}


def replace_box_drawing(text: str) -> str:
    """Replace box-drawing Unicode with ASCII equivalents."""
    for char, replacement in BOX_DRAWING_MAP.items():
        text = text.replace(char, replacement)
    return text


# Emoji/symbol replacements that can't be handled by newunicodechar
EMOJI_MAP = {
    "\U0001f534": "[RED]",  # 🔴
    "\U0001f7e2": "[GREEN]",  # 🟢
    "\U0001f7e1": "[YELLOW]",  # 🟡
    "\ufe0f": "",  # Variation selector (invisible, strip it)
}


def replace_emojis(text: str) -> str:
    """Replace emoji characters with ASCII equivalents."""
    for char, replacement in EMOJI_MAP.items():
        text = text.replace(char, replacement)
    return text


def preprocess_markdown(text: str, paper: dict) -> str:
    """Clean markdown for LaTeX compilation."""
    # Replace box-drawing chars first (they appear in code blocks where
    # newunicodechar can't reach)
    text = replace_box_drawing(text)
    # Replace emojis that LaTeX can't handle
    text = replace_emojis(text)
    lines = text.splitlines()
    out = []
    skip_metadata_table = False
    skip_toc_section = False
    abstract_lines = []
    in_abstract = False
    abstract_done = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # ── Skip the metadata Attribute/Value table ──
        # Detect: | **Attribute** | **Value** |
        if re.match(r"\|\s*\*\*Attribute\*\*\s*\|\s*\*\*Value\*\*\s*\|", line):
            skip_metadata_table = True
            i += 1
            continue
        if skip_metadata_table:
            if line.strip() == "" or not line.strip().startswith("|"):
                skip_metadata_table = False
                # don't skip this blank line, but don't add it
                i += 1
                continue
            i += 1
            continue

        # ── Skip the explicit Table of Contents section ──
        if re.match(r"^##\s+\*?\*?Table of Contents\*?\*?", line, re.IGNORECASE):
            skip_toc_section = True
            i += 1
            continue
        if skip_toc_section:
            # Stop skipping at the next ## heading or --- separator
            if re.match(r"^##\s+", line) or re.match(r"^---\s*$", line):
                skip_toc_section = False
                # fall through and process this line
            else:
                i += 1
                continue

        # ── Extract Abstract ──
        if re.match(r"^##\s+\*?\*?Abstract\*?\*?", line) and not abstract_done:
            in_abstract = True
            i += 1
            continue
        if in_abstract and not abstract_done:
            # End of abstract: next ## section or --- separator
            if re.match(r"^##\s+", line) or re.match(r"^---\s*$", line):
                in_abstract = False
                abstract_done = True
                # fall through to process this line
            else:
                if line.strip():
                    abstract_lines.append(line)
                i += 1
                continue

        # ── Skip the document title H1 (pandoc uses YAML title) ──
        if re.match(r"^#\s+", line) and not re.match(r"^##", line):
            # Only skip the very first H1 (the paper title)
            if not out:
                i += 1
                continue

        # ── Skip the subtitle line (bold italic text right after H1) ──
        # Pattern: ## Resolving Discontinuous... (H2 subtitle under title)
        # This is actually the subtitle H2, skip it since it's in YAML
        if i == 1 or (
            len(out) == 0 and re.match(r"^## .+", line) and "Table of" not in line
        ):
            # Check if this looks like a subtitle (before any content)
            pass  # handled by YAML subtitle

        # ── Strip bold markers from section headings ──
        # ## **Section Name** -> ## Section Name
        if re.match(r"^#+\s+\*\*", line):
            line = re.sub(r"^(#+\s+)\*\*(.*?)\*\*\s*$", r"\1\2", line)

        # ── Remove horizontal rules (---) — they cause LaTeX issues ──
        if re.match(r"^---+\s*$", line):
            i += 1
            continue

        # ── Convert pipe tables: strip bold from cells ──
        if line.strip().startswith("|"):
            line = re.sub(r"\*\*(.*?)\*\*", r"\1", line)

        out.append(line)
        i += 1

    abstract_text = "\n".join(abstract_lines).strip()
    return "\n".join(out).strip(), abstract_text


def build_yaml_front_matter(paper: dict, abstract: str) -> str:
    """Build YAML front matter for pandoc."""

    def esc(s):
        # Escape quotes in YAML values
        return s.replace('"', '\\"')

    lines = [
        "---",
        f'title: "{esc(paper["title"])}"',
        f'subtitle: "{esc(paper["subtitle"])}"',
        f'author: "{esc(paper["author"])}"',
        f'date: "{esc(paper["date"])}"',
        f'shorttitle: "{esc(paper["shorttitle"])}"',
        f'subject: "{esc(paper["subject"])}"',
        f'keywords: "{esc(paper["keywords"])}"',
    ]
    if abstract:
        # Multi-line YAML block scalar
        abstract_escaped = abstract.replace("\n", " ").strip()
        lines.append(f'abstract: "{esc(abstract_escaped)}"')
    lines.append("toc: true")
    lines.append("---")
    return "\n".join(lines)


# ── Compilation ────────────────────────────────────────────────────────────────


def compile_paper(paper: dict, src_dir: Path, out_dir: Path, template: Path) -> bool:
    md_path = src_dir / paper["md"]
    pdf_path = out_dir / paper["pdf"]

    print(f"\n{'=' * 60}")
    print(f"Compiling: {paper['md']}")
    print(f"Output:    {paper['pdf']}")

    # Read source
    text = md_path.read_text(encoding="utf-8")

    # Preprocess
    body, abstract = preprocess_markdown(text, paper)

    # Build YAML + body
    front_matter = build_yaml_front_matter(paper, abstract)
    full_md = front_matter + "\n\n" + body

    # Write to temp file
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8", dir="/tmp", prefix="wp_"
    ) as f:
        f.write(full_md)
        tmp_md = f.name

    try:
        # Run pandoc
        cmd = [
            "pandoc",
            tmp_md,
            "-o",
            str(pdf_path),
            "--pdf-engine=pdflatex",
            f"--template={template}",
            "--toc",
            "--toc-depth=3",
            "-V",
            "geometry:margin=2.5cm,top=3cm,bottom=3cm",
            "--highlight-style=tango",
        ]

        print(f"Running: {' '.join(cmd[:4])} ...")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(src_dir))

        if result.returncode == 0:
            size_kb = pdf_path.stat().st_size // 1024
            print(f"  SUCCESS — {size_kb} KB")
            if result.stderr:
                # Show warnings but don't fail
                warnings = [
                    l
                    for l in result.stderr.splitlines()
                    if "Missing character" not in l and l.strip()
                ]
                if warnings:
                    print(f"  Warnings: {len(warnings)} lines")
            return True
        else:
            print(f"  FAILED (exit {result.returncode})")
            print("  STDERR:")
            for line in result.stderr.splitlines()[-30:]:
                print(f"    {line}")
            return False

    finally:
        os.unlink(tmp_md)


# ── Main ───────────────────────────────────────────────────────────────────────


def main():
    src_dir = Path("/mnt/x/attribution_assets/whitepapers")
    out_dir = src_dir / "pdf_output"
    template = src_dir / "academic_pandoc.latex"

    out_dir.mkdir(exist_ok=True)

    if not template.exists():
        print(f"ERROR: Template not found: {template}")
        sys.exit(1)

    # Allow selecting a single paper by index or name
    targets = PAPERS
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.isdigit():
            targets = [PAPERS[int(arg)]]
        else:
            targets = [p for p in PAPERS if arg.lower() in p["md"].lower()]
        if not targets:
            print(f"No paper matching '{arg}'")
            sys.exit(1)

    results = []
    for paper in targets:
        md_path = src_dir / paper["md"]
        if not md_path.exists():
            print(f"  SKIP (not found): {paper['md']}")
            results.append((paper["pdf"], False))
            continue
        ok = compile_paper(paper, src_dir, out_dir, template)
        results.append((paper["pdf"], ok))

    print(f"\n{'=' * 60}")
    print("RESULTS:")
    ok_count = 0
    for name, ok in results:
        status = "OK " if ok else "FAIL"
        print(f"  [{status}] {name}")
        if ok:
            ok_count += 1
    print(f"\n{ok_count}/{len(results)} papers compiled successfully.")

    if ok_count < len(results):
        sys.exit(1)


if __name__ == "__main__":
    main()
