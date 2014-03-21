__author__ = 'David Gilmore'

from impala import dbapi

IMPALA_HOST = "ec2-54-227-18-49.compute-1.amazonaws.com"
IMPALA_PORT = 21050

impala_conn = dbapi.connect(host=IMPALA_HOST, port=IMPALA_PORT)
