debug = False
cache = False
defaultPort = 9080
domain = "localhost"
pesonaAudience = "http://%s:%s" % (domain, defaultPort)
assetsDirectory = "./static"
certsDirectory = "./certs"
breadcrumbDivider = "/"
tagline = "Providing Knowledge and Services for Tomorrow's Platforms"
officeCities = ["Bangalore", "San Francisco", "Atlanta"]
salesEmail = "sales@mindpool.io"
sessionTimeout = 24 * 60 * 60  # 24 hours
contentTypes = {
    "json": "text/json",
    "html": "text/html",
    "rst": "text/rst",
    }
