from twisted.cred import portal
from twisted.web import static

from browserid import checker

import klein
from klein.app import _globalKleinApp as app

from mindpoolsite import auth, const, utils
from mindpoolsite.views import pages


@klein.route(const.urls["root"])
@pages.cache
def root(request):
    return pages.SplashPage()


@klein.route(const.urls["services"])
@pages.cache
def services(request):
    return pages.ServicesPage()


@klein.route(const.urls["consulting"])
@pages.cache
def consulting(request):
    return pages.ConsultingPage()


@klein.route(const.urls["training"])
@pages.cache
def training(request):
    return pages.TrainingPage()


@klein.route(const.urls["people"])
@pages.cache
def people(request):
    return pages.PeoplePage()


@klein.route(const.urls["teams"])
@pages.cache
def teams(request):
    return pages.TeamsPage()


@klein.route(const.urls["members"])
@pages.cache
def members(request):
    return pages.MembersPage()


@klein.route(const.urls["cloud-tech"])
@pages.cache
def cloudTech(request):
    return pages.CloudTechPage()


@klein.route(const.urls["langs"])
@pages.cache
def langs(request):
    return pages.LangsPage()


@klein.route(const.urls["frameworks"])
@pages.cache
def frameworks(request):
    return pages.FrameworksPage()


@klein.route(const.urls["concurrency"])
@pages.cache
def concurrency(request):
    return pages.ConcurrencyPage()


@klein.route(const.urls["messaging"])
@pages.cache
def messaging(request):
    return pages.MessagingPage()


@klein.route(const.urls["distributed"])
@pages.cache
def distributed(request):
    return pages.DistributedPage()


@klein.route(const.urls["big-data"])
@pages.cache
def data(request):
    return pages.BigDataPage()


@klein.route(const.urls["aas"])
@pages.cache
def aas(request):
    return pages.AsAServicePage()


@klein.route(const.urls["sdn"])
@pages.cache
def sdn(request):
    return pages.SDNPage()


@klein.route(const.urls["ux"])
@pages.cache
def ux(request):
    return pages.UXPage()


@klein.route(const.urls["open-source"])
@pages.cache
def openSource(request):
    return pages.OpenSourcePage()


@klein.route(const.urls["about"])
@pages.cache
def about(request):
    return pages.AboutPage()


@klein.route(const.urls["who"])
@pages.cache
def who(request):
    return pages.WhoPage()


@klein.route(const.urls["what"])
@pages.cache
def what(request):
    return pages.WhatPage()


@klein.route(const.urls["culture"])
@pages.cache
def culture(request):
    return pages.CulturePage()


@klein.route(const.urls["social"])
@pages.cache
def social(request):
    return pages.SocialLinksPage()


@klein.route(const.urls["careers"])
@pages.cache
def careers(request):
    return pages.JobsPage()


@klein.route(const.urls["contact"])
@pages.cache
def contact(request):
    return pages.ContactPage()


@klein.route(const.urls["assets"])
def assets(request):
    return static.File(const.assetsDirectory)


@klein.route(const.urls["login"], methods=["POST"])
def login(request):
    realm = auth.AccountRealm()
    loginPortal = portal.Portal(realm)
    loginPortal.registerChecker(checker.BrowserIDChecker(
        const.pesonaAudience, certsDir=const.certsDirectory))
    return pages.LoginPage(app, loginPortal)


@klein.route(const.urls["logout"])
def logout(request):
    return pages.LogoutPage(app, None)


@klein.route(const.urls["account"])
def account(request):
    return pages.AccountPage()
