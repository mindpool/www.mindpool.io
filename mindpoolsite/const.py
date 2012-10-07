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
    "langs": "/cloud/languages",
    "frameworks": "/cloud/frameworks",
    "concurrency": "/cloud/concurrency",
    "messaging": "/cloud/messaging",
    "distributed": "/cloud/distributed",
    "big-data": "/cloud/data",
    "virtual": "/cloud/virtualization",
    "ux": "/cloud/ux",
    "open-source": "/opensource",
    "github": "http://mindpool.github.com/",
    "projects": "http://github.com/mindpool",
    "blog": "http://blog.mindpool.io",
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
#topNavLinks = [("Home", urls["root"], LINK)] + splashTopNavLinks
topNavLinks = splashTopNavLinks


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
    ]
aboutLinks = aboutDropDown


servicesLinks = [
    ("Services", urls["services"], LINK),
    ("Consulting", urls["consulting"], LINK),
    ("Training", urls["training"], LINK)]


peopleLinks = [
    ("People", urls["people"], LINK),
    ("Teams", urls["teams"], LINK),
    ("Members", urls["members"], LINK)]


cloudTechLinks = [
    ("Cloud Technologies", urls["cloud-tech"], LINK),
    ("The Foundation of Language", urls["langs"], LINK),
    ("Libraries and Frameworks", urls["frameworks"], LINK),
    ("Concurrency", urls["concurrency"], LINK),
    ("Messaging", urls["messaging"], LINK),
    ("Distributed System", urls["distributed"], LINK),
    ("Big Data", urls["big-data"], LINK),
    ("Virtualization", urls["virtual"], LINK),
    ("User Experience", urls["ux"], LINK)]


openSourceLinks = [
    ("Open Source", urls["open-source"], LINK),
    ("Github Page", urls["github"], LINK),
    ("Sponsored Projects", urls["projects"], LINK),
    ("Dev Blog", urls["blog"], LINK)]


contentTypes = {
    "json": "text/json",
    "html": "text/html",
    "rst": "text/rst",
    }


sessionUserVar = "mindpoolMemberUser"
sessionEmailVar = "mindpoolMemberEmail"
assetsDirectory = "./static"
certsDirectory = "./certs"
breadcrumbDivider = "/"
tagline = "Providing Knowledge and Services for Tomorrow's Platforms"
officeCities = ["Bangalore", "San Francisco", "Atlanta"]
salesEmail = "sales@mindpool.io"
