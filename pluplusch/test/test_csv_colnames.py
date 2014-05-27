from io import StringIO

import nose.tools as n

from pluplusch.csv_colnames import colnames

def test_csv_colnames():
    fp = StringIO('a;b;c;d\r\n3;8;9;2\r\n')
    observed = colnames(fp, delimiter = ';')
    expected = list('abcd')
    n.assert_list_equal(observed, expected)
