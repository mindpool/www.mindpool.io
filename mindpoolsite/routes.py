from twisted.web import static

from klein import route

from mindpoolsite import const
from mindpoolsite.views import pages


@route(const.urls["root"])
def root(request):
    return pages.SplashPage()


@route(const.urls["about"])
def about(request):
    return pages.AboutPage()


@route(const.urls["contact"])
def contact(request):
    return pages.ContactPage()


@route(const.urls["people"])
def contact(request):
    return pages.PeoplePage()


@route(const.urls["assets"])
def assets(request):
    return static.File(const.assetsDirectory)
