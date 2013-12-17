from unittest import TestCase

from polipy.api import config
from polipy.ideology.sponsorship_analysis import SponsorshipAnalysis

__author__ = 'David Gilmore'


class TestSponsorshipAnalysis(TestCase):

    def setUp(self):
        config.ROOT_URL = "http://localhost:8080"
        self.analysis = SponsorshipAnalysis()

    def test_get_sponsorship_matrix(self):
        # res = self.analysis.get_sponsorship_matrix("s", 1086484277, 1186484277)
        # assert res
        pass

    def test_plot_svd(self):
        self.analysis.plot_all_vh_dimensions("s", 1086484277, 1186484277)
        assert True