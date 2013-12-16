from unittest import TestCase
from nose.tools import eq_

from polipy.api.core import Caller
from polipy.api.core import config

__author__ = 'David Gilmore'


class TestCaller(TestCase):

    def setUp(self):
        # TODO: setup mocking. For now, testing is integrated, requires spring API to be running
        config.ROOT_URL = "http://localhost:8080"

    def test_get(self):
        # TODO: Double TODO cause this is super jank testing
        c = Caller()
        res = c.get("hello")
        eq_(res, 'Hello World!')
