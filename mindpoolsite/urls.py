from mindpoolsite import const


map = {
    "root": "/",
    # services
    "services": "/services",
    "consulting": "/services/consulting",
    "training": "/services/training",
    # people
    "people": "/people",
    "teams": "/people/teams",
    "members": "/people/members",
    # cloud tech
    "cloud-tech": "/cloud",
    "langs": "/cloud/languages",
    "frameworks": "/cloud/frameworks",
    "concurrency": "/cloud/concurrency",
    "messaging": "/cloud/messaging",
    "distributed": "/cloud/distributed",
    "big-data": "/cloud/data",
    "aas": "/cloud/aas",
    "sdn": "/cloud/sdn",
    "ux": "/cloud/ux",
    # open source
    "open-source": "/opensource",
    "github": "http://mindpool.github.com/",
    "projects": "http://github.com/mindpool",
    "blog": "http://blog.mindpool.io",
    # about
    "about": "/about",
    "who": "/about/who",
    "what": "/about/what",
    "culture": "/about/culture",
    "careers": "/about/careers",
    "social": "/about/social",
    "contact": "/about/contact",
    # members area
    "login": "/login",
    "logout": "/logout",
    "account": "/members/account",
    # misc
    "assets": "/static/",
    }


splashAliases = ["/", "/index", "/index.html", "/index.htm"]


splashTopNavLinks = [
    ("Services", map["services"], const.LINK),
    ("People", map["people"], const.LINK),
    ("Cloud Technologies", map["cloud-tech"], const.LINK),
    ("Open Source", map["open-source"], const.LINK),
    ("About", map["about"], const.DROPDOWN)]
#topNavLinks = [("Home", map["root"], LINK)] + splashTopNavLinks
topNavLinks = splashTopNavLinks


aboutDropDown = [
    ("Who We Are", map["who"], const.LINK),
    ("What We Do", map["what"], const.LINK),
    #("Our Culture", map["culture"], const.LINK),
    ("Social Links", map["social"], const.LINK),
    ("Careers", map["careers"], const.LINK),
    ("Contact Us", map["contact"], const.LINK),
    #("", "", const.DIVIDER),
    #("Investors", "", const.HEADER),
    #("VI Systems", "http://www.visystems.org/", const.LINK)]
    ]
aboutLinks = aboutDropDown


servicesLinks = [
    ("Services", map["services"], const.LINK),
    ("Consulting", map["consulting"], const.LINK),
    ("Training", map["training"], const.LINK)]


peopleLinks = [
    ("People", map["people"], const.LINK),
    ("Teams", map["teams"], const.LINK),
    #("Members", map["members"], const.LINK)]


cloudTechLinks = [
    ("Cloud Technologies", map["cloud-tech"], const.LINK),
    ("Languages as the Foundation", map["langs"], const.LINK),
    ("Frameworks", map["frameworks"], const.LINK),
    ("Concurrency", map["concurrency"], const.LINK),
    ("Messaging", map["messaging"], const.LINK),
    ("Distributed Systems", map["distributed"], const.LINK),
    ("Big Data", map["big-data"], const.LINK),
    ("IaaS and PaaS", map["aas"], const.LINK),
    ("SDNs", map["sdn"], const.LINK),
    ("User Experience", map["ux"], const.LINK)]


openSourceLinks = [
    ("Open Source", map["open-source"], const.LINK),
    ("Github Page", map["github"], const.LINK),
    ("Sponsored Projects", map["projects"], const.LINK),
    ("Dev Blog", map["blog"], const.LINK)]


membersLinks = [
    ("Account", map["account"], const.LINK),
    ]
