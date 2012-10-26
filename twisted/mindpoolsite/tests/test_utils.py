from twisted.trial import unittest

from mindpoolsite import utils


class RSTTestCase(unittest.TestCase):
    """
    """
    def setUp(self):
        self.rst = (
            "###########\nHello Title\n###########\n"
            "Hello Subtitle\n**************\n"
            "Heading 1\n=========\n"
            "Heading 2\n+++++++++\n"
            "Heading 3\n^^^^^^^^^\n"
            "Heading 4\n~~~~~~~~~\n"
            "Heading 5\n---------\n"
            "Heading 6\n_________\n"
            "Paragraph 1\n\nParagraph 2\n\n"
            "* bullet 1\n\n* bullet 2")
        self.html = utils.rstToHTML(self.rst)
        self.stan = utils.rstToStan(self.rst)

    def test_rstToHTML(self):
        self.assertTrue('<h1 class="title">Hello Title</h1>' in self.html)
        self.assertTrue(
            '<h2 class="subtitle" id="hello-subtitle">Hello Subtitle</h2>'
            in self.html)
        self.assertTrue(
            '<div class="section" id="heading-1">\n<h1>Heading 1</h1>'
            in self.html)
        self.assertTrue(
            '<div class="section" id="heading-2">\n<h2>Heading 2</h2>'
            in self.html)
        self.assertTrue(
            '<div class="section" id="heading-3">\n<h3>Heading 3</h3>'
            in self.html)
        self.assertTrue(
            '<div class="section" id="heading-4">\n<h4>Heading 4</h4>'
            in self.html)
        self.assertTrue(
            '<div class="section" id="heading-5">\n<h5>Heading 5</h5>'
            in self.html)
        self.assertTrue(
            '<div class="section" id="heading-6">\n<h6>Heading 6</h6>'
            in self.html)
        self.assertTrue("<p>Paragraph 1</p>" in self.html)
        self.assertTrue("<p>Paragraph 2</p>" in self.html)
        self.assertTrue("<li>bullet 1</li>\n" in self.html)
        self.assertTrue("<li>bullet 2</li>\n</ul>" in self.html)

    def test_rstToStan(self):
        _, topDiv, _ = utils.rstToStan(self.rst)
        title, subTitle, remainder = [
            x for x in topDiv.children if utils.checkTag(x)]
        heading1 = remainder.children[1]
        heading4Parent = remainder.children[3].children[3].children[3]
        heading6Parent = heading4Parent.children[3].children[3]
        heading6 = heading6Parent.children[1]
        p1 = heading6Parent.children[3]
        p2 = heading6Parent.children[5]
        ul = heading6Parent.children[7]
        bullet1 = ul.children[1]
        bullet2 = ul.children[3]
        self.assertEqual(title.tagName, "h1")
        self.assertEqual(title.children[0], u'Hello Title')
        self.assertEqual(subTitle.tagName, "h2")
        self.assertEqual(subTitle.children[0], u'Hello Subtitle')
        self.assertEqual(heading1.tagName, "h1")
        self.assertEqual(heading1.children[0], "Heading 1")
        self.assertEqual(heading6.tagName, "h6")
        self.assertEqual(heading6.children[0], "Heading 6")
        self.assertEqual(p1.tagName, "p")
        self.assertEqual(p1.children[0], "Paragraph 1")
        self.assertEqual(p2.tagName, "p")
        self.assertEqual(p2.children[0], "Paragraph 2")
        self.assertEqual(bullet1.tagName, "li")
        self.assertEqual(bullet1.children[0], "bullet 1")
        self.assertEqual(bullet2.tagName, "li")
        self.assertEqual(bullet2.children[0], "bullet 2")
