import io
import unittest

from coinstac_pyprofiler.core import utils as pf_utils


class RendererTestCase(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
