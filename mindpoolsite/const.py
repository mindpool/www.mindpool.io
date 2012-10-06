defaultPort = 9080
domain = "localhost"
pesonaAudience = "http://%s:%s" % (domain, defaultPort)


LINK = 0
DROPDOWN = 1
DIVIDER = 2
HEADER = 3


urls = {
    "root": "/",
    "services": "/services",
    "consulting": "/services/consulting",
    "training": "/services/training",
    "people": "/people",
    "teams": "/people/teams",
    "members": "/people/members",
    "cloud-tech": "/cloud",
    "open-source": "/opensource",
    "about": "/about",
    "who": "/about/who",
    "what": "/about/what",
    "culture": "/about/culture",
    "careers": "/about/careers",
    "social": "/about/social",
    "contact": "/about/contact",
    "assets": "/static/",
    "login": "/login",
    "logout": "/logout",
    }


splashAliases = ["/", "/index", "/index.html", "/index.htm"]


splashTopNavLinks = [
    ("Services", urls["services"], LINK),
    ("People", urls["people"], LINK),
    ("Cloud Technologies", urls["cloud-tech"], LINK),
    ("Open Source", urls["open-source"], LINK),
    ("About", urls["about"], DROPDOWN)]
topNavLinks = [("Home", urls["root"], LINK)] + splashTopNavLinks


aboutDropDown = [
    ("Who We Are", urls["who"], LINK),
    ("What We Do", urls["what"], LINK),
    ("Our Culture", urls["culture"], LINK),
    ("Social Links", urls["social"], LINK),
    ("Careers", urls["careers"], LINK),
    ("Contact Us", urls["contact"], LINK),
    #("", "", DIVIDER),
    #("Investors", "", HEADER),
    #("VI Systems", "http://www.visystems.org/", LINK)]
aboutLinks = aboutDropDown


servicesLinks = [
    ("Services", urls["services"], LINK),
    ("Consulting", urls["consulting"], LINK),
    ("Training", urls["training"], LINK)]


peopleLinks = [
    ("People", urls["people"], LINK),
    ("Teams", urls["teams"], LINK),
    ("Members", urls["members"], LINK)]


assetsDirectory = "./static"
certsDirectory = "./certs"
breadcrumbDivider = "/"
tagline = "Providing Knowledge and Services for Tomorrow's Platforms"
officeCities = ["Bangalore", "San Francisco"]
salesEmail = "sales@mindpool.io"
