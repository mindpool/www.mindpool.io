from docutils.core import publish_string as render_rst

from twisted.internet import protocol, reactor
from twisted.protocols import memcache
from twisted.python import log
from twisted.web.template import flattenString, XMLString


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


def rstToStan(rst):
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


class MemCacheHelper(object):
    """
    """
    def __init__(self, request, key, pageClass):
        self.request = request
        self.key = key
        self.pageClass = pageClass
        self.memcache = None

    def getHTML(self, page):
        d = self.memcache.set(self.key, page)
        d.addErrback(log.msg)
        return page

    def getMemPage(self, result):
        flags, page = result
        if page:
            # XXX change to debug log
            print "Cache hit; skipping page generation ..."
            return page
        # XXX change to debug log
        print "No page in cache; getting and setting ..."
        d = flattenString(self.request, self.pageClass())
        d.addErrback(log.msg)
        d.addCallback(self.getHTML)
        return d

    def getPage(self, mem):
        self.memcache = mem
        d = self.memcache.get(self.key)
        d.addErrback(log.msg)
        d.addCallback(self.getMemPage)
        return d


# XXX these parameters are ugly... we can probably fix this with a class
def cacheOrStash(request, pageClass, auth):
    """
    """
    account = auth.getSessionAccount(request)
    key = "%s%s%s" % (request.path, account.sessionID, str(account.email))
    # XXX change to debug log
    print "Generated key:", key
    memHelper = MemCacheHelper(request, key, pageClass)

    client = protocol.ClientCreator(reactor, memcache.MemCacheProtocol)
    d = client.connectTCP("localhost", memcache.DEFAULT_PORT)
    d.addErrback(log.msg)
    d.addCallback(memHelper.getPage)
    d.addErrback(log.msg)
    return d
