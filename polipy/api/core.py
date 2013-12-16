import json

from urllib import urlencode
from urllib2 import urlopen
from urllib2 import HTTPError
from polipy.api import config

_str_type = basestring

__author__ = 'David Gilmore'


class Caller():

    def get(self, top_level_object, **kwargs):
        """ Make a call to the root domain for the given object with certain arguments. If successful,
        return a dict of the decoded json.
        """
        url = self._get_url(top_level_object, **kwargs)

        try:
            r = urlopen(url)
            return_data = r.read().decode('utf8')
            return self._decode_response(return_data)
        except HTTPError as e:
            raise e

    def _get_url(self, endpoint, **kwargs):
        """ Encode URL with ROOT_URL from config, the given endpoint, and the arguments and return.
        """
        url_args = self.preencode_values(self.flatten_dict(kwargs))
        url = "{0}/{1}{2}".format(config.ROOT_URL, endpoint, self.safe_encode(url_args))
        return url

    def flatten_dict(self, d):
        """ Flatten a nested dict of key word arguments if necessary and return.
        """
        def flat_items():
            for k, v in d.items():

                # If a value is a dict, recursively flatten it
                if isinstance(v, dict):
                    for kk, vv in self.flatten_dict(v).items():
                        yield '{0}.{1}'.format(k, kk), vv
                else:
                    yield k, v

        return dict(flat_items())

    def preencode_values(self, d):
        """ Handle kwargs that aren't in URL string convention and return new values.
        """
        for k, v in d.items():
            if isinstance(v, bool):
                d[k] = str(v).lower()
        return d

    def safe_encode(self, kwargs):
        """ Use urllib to encode values after converting all string values to UTF and return.
        """
        kwargs = kwargs.copy()
        for k, v in kwargs.items():
            if isinstance(v, _str_type):
                kwargs[k] = v.encode('utf8')
        return urlencode(kwargs)

    def _decode_response(self, response):
        """ Load json as a dict and return.
        """
        try:
            data = json.loads(response)
            return data
        except ValueError:
            print "The response could not be decoded as a JSON object"

        return response.encode('utf-8')
