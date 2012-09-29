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
    "contact": "/about/contact",
    "assets": "/static/",
    }


splashTopNavLinks = [
    ("Services", urls["services"], LINK),
    ("People", urls["people"], LINK),
    ("Cloud Technologies", urls["cloud-tech"], LINK),
    ("Open Source", urls["open-source"], LINK),
    ("About", urls["about"], DROPDOWN)]


aboutDropDown = [
    ("Who We Are", urls["who"], LINK),
    ("What We Do", urls["what"], LINK),
    ("Our Culture", urls["culture"], LINK),
    ("Contact Us", urls["contact"], LINK),
    ("", "", DIVIDER),
    ("Velankani", "", HEADER),
    ("The Velankani Group", "http://www.velankani.net/velankani_group.htm",
     LINK),
    ("VI Systems", "http://www.visystems.org/", LINK)]


topNavLinks = [("Home", urls["root"], LINK)] + splashTopNavLinks
assetsDirectory = "./static"
breadcrumbDivider = "/"
tagline = "Providing Knowledge and Services for Tomorrow's Platforms"
officeCities = ["Bangalore", "San Francisco"]
salesEmail = "sales@mindpool.io"
