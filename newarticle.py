#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
from datetime import date
from pathlib import Path


def prepare_content(filename):
    template = Path("content/draft.md")
    content = template.read_text()

    slug = filename.rstrip(".md")
    title = str.replace(slug, "-", " ").capitalize()
    date_string = date.today().strftime("%Y-%m-%d")

    return (
        content.replace("{TITLE}", title)
        .replace("{SLUG}", slug)
        .replace("1970-01-01", date_string)
    )


def main():
    try:
        file_path = Path(f"content/{sys.argv[1]}")
    except IndexError:
        raise RuntimeError(
            "Missing file name!\nUsage: python newarticle.py category/filename.md"
        )

    if file_path.suffix != ".md":
        if file_path.suffix == "":
            file_path = file_path.with_suffix(".md")
        else:
            raise RuntimeError("Filename should have .md extension!")

    if file_path.exists():
        raise FileExistsError("File already exists!")

    # Let's avoid creating directories because of typos
    if not file_path.parent.exists():
        raise FileNotFoundError(
            f"Directory for category '{file_path.parent.name}' does not exist!"
        )

    filename = file_path.name
    content = prepare_content(filename)

    file_path.write_text(content)
    print("File created")


if __name__ == "__main__":
    main()
