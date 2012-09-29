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
    ("Services", urls["services"]),
    ("People", urls["people"]),
    ("Cloud Technologies", urls["cloud-tech"]),
    ("Open Source", urls["open-source"]),
    ("About", urls["about"])]


topNavLinks = [("Home", urls["root"])] + splashTopNavLinks
assetsDirectory = "./static"
breadcrumbDivider = "/"
tagline = "Providing Knowledge and Services for Tomorrow's Platforms"
officeCities = ["Bangalore", "San Francisco"]
salesEmail = "sales@mindpool.io"
