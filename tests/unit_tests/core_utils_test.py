import io
import unittest
from unittest.mock import MagicMock

from coinstac_pyprofiler.core import utils as pf_utils


class MyUtilsTestCase(unittest.TestCase):
    def test_combine_strings(self):
        self.assertEqual(pf_utils.combine_strings("a", "b", "c"), "abc")

    def test_render_html_from_json_file(self):
        with open("resources/test_merged.html", "r") as f:
            act_html = ''.join(line for line in f.readlines())
        new_html = pf_utils.render_html_from_json_file("resources/test_merged.json")
        self.assertEqual(act_html, new_html)

    def test_render_html_from_json_string(self):
        with open("resources/test_merged.html", "r") as f:
            act_html = ''.join(line for line in f.readlines())

        with io.open("resources/test_merged.json") as json_file:
            session_json = json_file.read()
            new_html = pf_utils.render_html_from_json_string(session_json)
        self.assertEqual(act_html, new_html)

    def test_write_json_to_file(self):
        pf_utils.write_to_file = MagicMock()
        pf_utils.write_json_to_file('{"temp": "test"}', "temp.json")
        pf_utils.write_to_file.assert_called_once_with('{\n    "temp": "test"\n}', "temp.json")

    def test_get_human_readable_time(self):
        self.assertEqual(pf_utils.get_human_readable_time(3661), '1:01:01')


if __name__ == '__main__':
    unittest.main()
