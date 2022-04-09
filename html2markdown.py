import re


def html2markdown(html):
    """Take in html text as input and return markdown"""
    # Convert italics
    markdown_text = re.sub(r"<[/]?em>", "*", html)

    # Remove spaces
    markdown_text = re.sub(r"\s+", " ", markdown_text)

    # Convert paragraphs
    markdown_text = re.sub(r"(</p><p>|<p>|</p>)+", "\n\n", markdown_text).strip()

    # Convert URLs
    while url := re.search(
        pattern=r"<a href=\"(?P<LINK>\S+)\">(?P<NAME>.*?)</a>", string=markdown_text
    ):
        markdown_text = (
            markdown_text[: url.start()]
            + f"[{url.group('NAME')}]({url.group('LINK')})"
            + markdown_text[url.end() :]
        )

    return markdown_text
