__author__ = 'David Gilmore'

from unittest import TestCase
from mock import patch
import pandas


class TestIndividualContributions(TestCase):
    """
    Test interactions with individual contribution dataset
    """

    def setUp(self):
        """

        """
        self.individual_contributions = pandas.io.parsers.read_csv('../data/indiv_contr.txt', sep='|')


    @patch('polipy.adhoc.impala_repo.select_dataframe')
    def test_select_dataframe(self, select_dataframe):
        """
        Get a mocking system set up
        """

        select_dataframe.return_value = self.individual_contributions

        df = select_dataframe("SELECT contrib_id, bioguide_id, transaction_dt, zip, type, amount, l.gender, birthday, religion, real_code FROM entities.legislators l JOIN crp.individual_contributions i ON recip_id = opensecrets_id WHERE transaction_ts > 1375590539")
        print df

