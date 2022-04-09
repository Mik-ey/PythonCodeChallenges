import re


def html2markdown(html):
    """Take in html text as input and return markdown"""
    # Convert italics
    markdown_text = re.sub(r"<[/]?em>", "*", html)

    # Remove spaces
    markdown_text = re.sub(r"\s+", " ", markdown_text)

    # Convert paragraphs
    markdown_text = re.sub(r"(</p><p>|<p>|</p>)+", "\n\n", markdown_text).strip()

    return markdown_text
