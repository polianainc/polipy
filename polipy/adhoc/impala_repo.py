__author__ = 'David Gilmore'

from polipy.adhoc import impala_conn
from impala.util import as_pandas


def select_dataframe(sql):
    """
    Return a pandas data frame with the results of a sql query to impala
    :param sql:
    :return:
    """
    cur = impala_conn.cursor()
    cur.execute(sql)
    return as_pandas(cur)

