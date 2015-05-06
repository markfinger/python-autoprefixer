import sys
from optional_django import six
from js_host.function import Function
from js_host.exceptions import FunctionError

js_host_function = Function('autoprefixer')


class AutoprefixerError(Exception):
    pass


def autoprefixer(css, is_file=None, options=None):
    if is_file:
        with open(css, 'r') as content_file:
            css = content_file.read()

    try:
        return js_host_function.call(css=css, options=options)
    except FunctionError as e:
        six.reraise(AutoprefixerError, AutoprefixerError(*e.args), sys.exc_info()[2])