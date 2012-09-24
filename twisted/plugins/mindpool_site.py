# -*- coding: utf-8 -*-
from twisted.application.service import ServiceMaker


MindPoolSiteService = ServiceMaker(
    "MindPool, Inc. Web Site",
    "mindpoolsite.app",
    "MindPool, Inc. Web Site",
    "mindpool-site")
