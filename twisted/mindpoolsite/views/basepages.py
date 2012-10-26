from twisted.internet import protocol, reactor
from twisted.protocols import memcache
from twisted.python import log
from twisted.web.iweb import IRenderable
from twisted.web.template import flattenString, renderer

from zope.interface import implements

from klein.resource import KleinResource

from mindpoolsite import auth, config, urls, utils
from mindpoolsite.views import fragments, loaders


class MemCacheHelper(object):
    """
    """
    def __init__(self, request, pageClass):
        self.request = request
        self.pageClass = pageClass
        self.memcache = None
        self.key = ""

    def setPage(self, page):
        d = self.memcache.set(self.key, page)
        d.addErrback(log.msg)
        return page

    def getOrFlattenPage(self, result):
        flags, page = result
        if page:
            if config.debug:
                log.msg("Cache hit; skipping page generation ...")
            return page
        if config.debug:
            log.msg("No page in cache; getting and setting ...")
        d = flattenString(self.request, self.pageClass())
        d.addErrback(log.msg)
        d.addCallback(self.setPage)
        return d

    def pokeMemCache(self, mem):
        if not mem:
            if config.debug:
                log.msg("Cannot connect to memcache server!")
            return self.pageClass()
        self.memcache = mem
        d = self.memcache.get(self.key)
        d.addErrback(log.msg)
        d.addCallback(self.getOrFlattenPage)
        return d

    def getPage(self):
        """
        """
        self.key = auth.getSessionAccount(
            self.request).getKey(self.request.path)
        if config.debug:
            log.msg("Generated key:", self.key)
        client = protocol.ClientCreator(reactor, memcache.MemCacheProtocol)
        d = client.connectTCP("localhost", memcache.DEFAULT_PORT)
        d.addErrback(log.msg)
        d.addCallback(self.pokeMemCache)
        d.addErrback(log.msg)
        return d


class BasePage(loaders.TemplateLoader):
    """
    """
    templateFile = "base.xml"

    @renderer
    def head(self, request, tag):
        return fragments.HeadFragment()

    @renderer
    def bodyData(self, request, tag):
        bodyClass = ""
        if request.path in urls.splashAliases:
            bodyClass = "splash"
        else:
            bodyClass = "content-page"
        return tag.fillSlots(bodyClass=bodyClass)

    @renderer
    def topnav(self, request, tag):
        raise NotImplementedError()

    @renderer
    def contentarea(self, request, tag):
        raise NotImplementedError()

    @renderer
    def sidebar(self, request, tag):
        return tag

    @renderer
    def jsloader(self, request, tag):
        return loaders.TemplateLoader(templateFile="fragments/jsloader.xml")

    @renderer
    def footer(self, request, tag):
        return fragments.FooterFragment()


class BaseResourcePage(KleinResource):
    """
    """
    def __init__(self, app, portal):
        KleinResource.__init__(self, app)
        self.portal = portal

    def handleError(self, failure):
        print "Whoops ..."
        print failure
        print dir(failure)
        print vars(failure)


class ReSTContent(object):
    """
    """
    implements(IRenderable)

    def __init__(self, rstData):
        self.rstData = rstData

    def render(self, request):
        return utils.rstToStan(self.rstData)


class ContentPage(BasePage):
    """
    """
    contentType = config.contentTypes["rst"]
    contentData = ""
    contentDataTemplate = ""
    _cachedContent = ""

    def getContentData(self, request):
        pass

    def getContentDataTemplate(self, request):
        pass

    def getContent(self, request, templateData=""):
        if self.contentData:
            content = self.contentData
        elif self.contentDataTemplate:
            content = self.contentDataTemplate
            if templateData:
                content = content % templateData
        else:
            content = self.getContentData(request)
            if not content:
                content = self.getContentDataTemplate(request)
                if content and templateData:
                    content = content % templateData
        return content

    def renderContentData(self, request):
        if not self._cachedContent:
            if self.contentType == config.contentTypes["rst"]:
                self._cachedContent = ReSTContent(self.getContent(request))
            elif self.contentType == config.contentTypes["html"]:
                self._cachedContent = self.getContent(request)
        return self._cachedContent

    @renderer
    def topnav(self, request, tag):
        return fragments.TopNavFragment()

    @renderer
    def contentarea(self, request, tag):
        return fragments.ContentFragment(self.renderContentData(request))


class SidebarPage(ContentPage):
    """
    """
    sidebarHeading = ""
    sidebarLinks = []
    contentData = ""

    @renderer
    def contentarea(self, request, tag):
        return fragments.ContentFragment(
            self.renderContentData(request), self.sidebarLinks)
