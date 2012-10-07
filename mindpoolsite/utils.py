from docutils.core import publish_string as render_rst

from twisted.web.template import Tag, XMLString


def rstToHTML(rst):
    overrides = {
        'output_encoding': 'unicode',
        'input_encoding': 'unicode'
        }
    return render_rst(
        rst.decode("utf-8"), writer_name="html", settings_overrides=overrides)


def checkTag(tag):
    if isinstance(tag, basestring):
        return False
    return True


def rstToStan(rst, xpath=""):
    html = rstToHTML(rst)
    # fix a bad encoding in docutils
    html = html.replace('encoding="unicode"', '')
    stan = XMLString(html).load()[0]
    if stan.tagName != "html":
        raise ValueError("Unexpected top-level HTML tag.")
    head, body = [x for x in stan.children if checkTag(x)]
    if head.tagName != "head":
        raise ValueError("Expected 'head' node, got '%s'" % (
            head.tagName))
    if body.tagName != "body":
        raise ValueError("Expected 'body' node, got '%s'" % (
            body.tagName))
    return body.children
