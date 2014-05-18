__author__ = 'David Gilmore'

import numpy as np
import matplotlib.pyplot as plt

from polipy.api.core import Caller


class SponsorshipAnalysis(Caller):

    def get_sponsorship_matrix(self, chamber, begin, end):
        """ Call endpoint legislators/sponsorship-matrix with a chamber and time period
        :return: A dictionary with fields:
            chamber:
            begin_timestamp:
            end_timestamp:
            sponsorship_matrix:
            id_to_index:
        """
        # TODO: implement best practice for API calls
        call = "legislators/sponsorship-matrix/{0}/{1}/{2}".format(chamber, begin, end)
        res = self.get(call)
        return res

    def plot_ideology_distribution(self, name, vh, legislators, dim):
        """ Given a SVD rank reduction, plot each dimension with parties represented by color
        """

        rep = []
        dem = []

        for legislator in legislators:
            if legislator["party"] == u'Republican':
                rep.append(vh[dim, legislator["index"]])
            if legislator["party"] == u'Democrat':
                dem.append(vh[dim, legislator["index"]])


        plt.plot(rep, 'red')
        plt.plot(dem, 'blue')
        plt.savefig("../images/{0}.png".format(name))
        plt.clf()

    def plot_svd(self, chamber, begin, end):
        """
        :param chamber:
        :param begin:
        :param end:
        :return:
        """
        sponsorship_data = self.get_sponsorship_matrix(chamber, begin, end)
        u, s, vh = np.linalg.svd(sponsorship_data["sponsorship_matrix"])
        self.plot_ideology_distribution(u, s, vh, sponsorship_data["legislators"], 1)

    def plot_all_vh_dimensions(self, chamber, begin, end):
        """
        :param chamber:
        :param begin:
        :param end:
        :return:
        """
        sponsorship_data = self.get_sponsorship_matrix(chamber, begin, end)
        u, s, vh = np.linalg.svd(sponsorship_data["sponsorship_matrix"])
        for i in xrange(len(vh)):
            name = "{0}_{1}_{2}_ideology_dim_{3}".format(chamber, begin, end, i)
            self.plot_ideology_distribution(name, vh, sponsorship_data["legislators"], i)
