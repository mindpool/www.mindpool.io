from twisted.web import static

from klein import route

from mindpoolsite import const
from mindpoolsite.views import pages


@route(const.urls["root"])
def root(request):
    return pages.SplashPage()


@route(const.urls["services"])
def services(request):
    return pages.ServicesPage()


@route(const.urls["consulting"])
def consulting(request):
    return pages.ConsultingPage()


@route(const.urls["training"])
def training(request):
    return pages.TrainingPage()


@route(const.urls["people"])
def people(request):
    return pages.PeoplePage()


@route(const.urls["teams"])
def teams(request):
    return pages.TeamsPage()


@route(const.urls["members"])
def members(request):
    return pages.WhoPage()


@route(const.urls["cloud-tech"])
def cloudTech(request):
    return pages.CloudTechPage()


@route(const.urls["open-source"])
def openSource(request):
    return pages.OpenSourcePage()


@route(const.urls["about"])
def about(request):
    return pages.AboutPage()


@route(const.urls["who"])
def who(request):
    return pages.WhoPage()


@route(const.urls["what"])
def what(request):
    return pages.WhatPage()


@route(const.urls["culture"])
def culture(request):
    return pages.CulturePage()


@route(const.urls["social"])
def social(request):
    return pages.SocialLinksPage()


@route(const.urls["careers"])
def careers(request):
    return pages.JobsPage()


@route(const.urls["contact"])
def contact(request):
    return pages.ContactPage()


@route(const.urls["assets"])
def assets(request):
    return static.File(const.assetsDirectory)
