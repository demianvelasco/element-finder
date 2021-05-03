from Finder import ElementFinder
from test_site import TestServer
from test_globals import TESTS
import unittest
from parameterized import parameterized


class TestElementFinder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = TestServer()
        cls.server.start_server()

    @classmethod
    def tearDownClass(cls):
        cls.server.stop_server()

    @parameterized.expand(TESTS)
    def test_attribute_and_content(self, init_parms, element, element_id, url, csv, debug, single_site, expected_amount):
        self.finder = ElementFinder(**init_parms)
        self.assertEqual(self.finder.element, element)
        self.assertEqual(self.finder.element_id, element_id)
        self.assertEqual(self.finder.url, url)
        self.assertEqual(self.finder.csv, csv)
        self.assertEqual(self.finder.debug, debug)
        self.assertEqual(self.finder.single_site, single_site)
        content = self.finder.find_element_in_site(
            self.finder.element, self.finder.element_id)
        self.assertEqual(len(content), expected_amount)


if __name__ == '__main__':
    unittest.main()
