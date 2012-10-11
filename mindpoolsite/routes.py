from twisted.cred import portal
from twisted.web import static

from browserid import checker

import klein
from klein.app import _globalKleinApp as app

from mindpoolsite import auth, config, urls
from mindpoolsite.views import pages


@klein.route(urls.map["root"])
@pages.cache
def root(request):
    return pages.SplashPage


@klein.route(urls.map["services"])
@pages.cache
def services(request):
    return pages.ServicesPage


@klein.route(urls.map["consulting"])
@pages.cache
def consulting(request):
    return pages.ConsultingPage


@klein.route(urls.map["training"])
@pages.cache
def training(request):
    return pages.TrainingPage


@klein.route(urls.map["people"])
@pages.cache
def people(request):
    return pages.PeoplePage


@klein.route(urls.map["teams"])
@pages.cache
def teams(request):
    return pages.TeamsPage


@klein.route(urls.map["members"])
@pages.cache
def members(request):
    return pages.MembersPage


@klein.route(urls.map["solutions"])
@pages.cache
def Solutions(request):
    return pages.SolutionsPage


@klein.route(urls.map["langs"])
@pages.cache
def langs(request):
    return pages.LangsPage


@klein.route(urls.map["frameworks"])
@pages.cache
def frameworks(request):
    return pages.FrameworksPage


@klein.route(urls.map["concurrency"])
@pages.cache
def concurrency(request):
    return pages.ConcurrencyPage


@klein.route(urls.map["messaging"])
@pages.cache
def messaging(request):
    return pages.MessagingPage


@klein.route(urls.map["distributed"])
@pages.cache
def distributed(request):
    return pages.DistributedPage


@klein.route(urls.map["big-data"])
@pages.cache
def data(request):
    return pages.BigDataPage


@klein.route(urls.map["aas"])
@pages.cache
def aas(request):
    return pages.AsAServicePage


@klein.route(urls.map["sdn"])
@pages.cache
def sdn(request):
    return pages.SDNPage


@klein.route(urls.map["ux"])
@pages.cache
def ux(request):
    return pages.UXPage


@klein.route(urls.map["open-source"])
@pages.cache
def openSource(request):
    return pages.OpenSourcePage


@klein.route(urls.map["about"])
@pages.cache
def about(request):
    return pages.AboutPage


@klein.route(urls.map["who"])
@pages.cache
def who(request):
    return pages.WhoPage


@klein.route(urls.map["what"])
@pages.cache
def what(request):
    return pages.WhatPage


@klein.route(urls.map["culture"])
@pages.cache
def culture(request):
    return pages.CulturePage


@klein.route(urls.map["social"])
@pages.cache
def social(request):
    return pages.SocialLinksPage


@klein.route(urls.map["careers"])
@pages.cache
def careers(request):
    return pages.JobsPage


@klein.route(urls.map["contact"])
@pages.cache
def contact(request):
    return pages.ContactPage


@klein.route(urls.map["assets"])
def assets(request):
    return static.File(config.assetsDirectory)


@klein.route(urls.map["login"], methods=["POST"])
def login(request):
    realm = auth.AccountRealm()
    loginPortal = portal.Portal(realm)
    loginPortal.registerChecker(checker.BrowserIDChecker(
        config.pesonaAudience, certsDir=config.certsDirectory))
    return pages.LoginPage(app, loginPortal)


@klein.route(urls.map["logout"])
def logout(request):
    return pages.LogoutPage(app, None)


@klein.route(urls.map["account"])
def account(request):
    return pages.AccountPage()
