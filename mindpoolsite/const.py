urls = {
    "root": "/",
    "services": "/services",
    "consulting": "/services/consulting",
    "training": "/services/training",
    "people": "/people",
    "teams": "/people/teams",
    "cloud-tech": "/cloud-tech",
    "open-source": "/open-source",
    "about": "/about",
    "who": "/about/who",
    "what": "/about/what",
    "culture": "/about/culture",
    "contact": "/about/contact",
    "assets": "/static/",
    }


topNavLinksSplash = [
    ("Services", urls["services"]),
    ("People", urls["people"]),
    ("Cloud Technologies", urls["cloud-tech"]),
    ("Open Source", urls["open-source"]),
    ("About", urls["about"])]


topNavLinks = [("Home", urls["root"])] + topNavLinksSplash
assetsDirectory = "./static"
breadcrumbDivider = "/"
tagline = "Providing Knowledge and Services for Tomorrow's Platforms"
