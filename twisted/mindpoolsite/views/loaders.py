# -*- coding: utf-8
from twisted.python.filepath import FilePath
from twisted.web.template import Element, XMLFile


class TemplateLoader(Element):
    """
    """
    templateDir = "templates"
    templateFile = ""

    def __init__(self, loader=None, templateFile=None):
        super(TemplateLoader, self).__init__(loader=loader)
        if templateFile:
            self.templateFile = templateFile
        self.setLoader()

    def setLoader(self, templateDir="", templateFile=""):
        if not templateDir:
            templateDir = self.templateDir
        if not templateFile:
            templateFile = self.templateFile
        template = FilePath(
            "%s/%s" % (templateDir, templateFile))
        self.loader = XMLFile(template.path)
