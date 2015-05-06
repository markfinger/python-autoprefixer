import os
import unittest
from autoprefixer.compiler import autoprefixer, AutoprefixerError
from js_host.conf import settings

settings.configure(USE_MANAGER=True)

TEST_CSS_FILE = os.path.join(os.path.dirname(__file__), 'test.css')


class TestDjangoFrontendTools(unittest.TestCase):
    def test_autoprefixer_can_process_css_string(self):
        css = '.foo { -moz-border-radius: 100%; border-radius: 100%; }'
        expected = '.foo { border-radius: 100%; }'
        self.assertEqual(autoprefixer(css), expected)

    def test_autoprefixer_can_accept_an_options_dict(self):
        css = '.foo { -moz-border-radius: 100%; border-radius: 100%; }'
        self.assertEqual(autoprefixer(css, options={'browsers': ['Firefox 3']}), css)

    def test_autoprefixer_can_process_css_file(self):
        expected = '.foo { border-radius: 100%; }'
        self.assertEqual(autoprefixer(TEST_CSS_FILE, is_file=True), expected)

    def test_raises_autoprefixer_error(self):
        self.assertRaises(AutoprefixerError, autoprefixer, css=None)