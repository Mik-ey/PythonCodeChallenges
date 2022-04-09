import re


def html2markdown(html):
    """Take in html text as input and return markdown"""
    # Convert italics
    markdown_text = re.sub(r"<[/]?em>", "*", html)

    return markdown_text
