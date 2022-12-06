def html_tag(text, html_tag):
    """
    return html tag of any text
    :param text:Any kind of string
    :param html_tag:what kind of html tag you want to generate
    :return:html tag of any text
    """
    html = f'<{html_tag}> {text}<\{html_tag}>'
    return html
print(html_tag('This is paragraph', 'p'))