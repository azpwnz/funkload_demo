"""Zain FunkLoad test

$Id$
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
from webunit.utility import Upload


class Milo(FunkLoadTestCase):
    """This test uses the configuration file Milo.conf."""

    def setUp(self):
        """Setting up test."""
        # Get value from "main" section and "url" key
        self.server_url = self.conf_get('main', 'url')

    def home(self):
        # Open home page using variable from setUp
        res = self.get(self.server_url, description='Get Home Page')
        self.assert_(res.code == 200, "expecting a 200")

    def overview(self):
        self.get(self.server_url + 'start/overview/', description='Get Web Products Page')
        self.assert_('Why Django?' in self.getBody(), "Wrong page")

    def download(self):
        res = self.get(self.server_url + 'download/', description='Get Our Team Page')
        self.assert_(res.code == 200, "expecting a 200")

    def community(self):
        res = self.get(self.server_url + 'community/', description='Get Contact Page')
        self.assert_(res.code == 200, "expecting a 200")

    def test_django_website(self):
        self.home()
        self.overview()
        self.download()
        self.community()


class Dummy(FunkLoadTestCase):
    """
    This test uses the configuration file Milo.conf.
    These tests use fake urls and will not work.
    """

    def setUp(self):
        """Setting up test."""
        # Get value from "main" section and "url" key
        self.server_url = self.conf_get('main', 'url')

    # Get test
    def home(self):
        # Open home page using variable from setUp
        res = self.get(self.server_url, description='Get Home Page')
        self.assert_(res.code == 200, "expecting a 200")

    # Submit a form using POST request
    def form_submit(self):
        self.get(self.server_url + 'hello/world/',
                 description='Get Some Page')

        res = self.post(self.server_url + "hello/world/",
                        params=[['username', 'hello'], ['password', 'qwerty']],
                        description="Login")
        self.assert_(res.code in [200, 302], "expecting a 200 or 302")

    # Submit a form with an image using POST request
    def file_upload(self):
        self.get(self.server_url + 'hello/world/',
                 description='Get Some Page')

        res = self.post(self.server_url + "hello/world/",
                        params=[['email', 'john@doe.com'], ['photo', Upload('files/hello.png')]],
                        description="Upload Photo")
        self.assert_(res.code in [200, 302], "expecting a 200 or 302")

    def test_dummy(self):
        self.home()
        self.form_submit()
        self.file_upload()


if __name__ in ('main', '__main__'):
    unittest.main()
