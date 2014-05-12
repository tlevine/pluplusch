from io import StringIO

import nose.tools as n

from pluplusch.csv_colnames import colnames

def test_csv_colnames():
    fp = StringIO('a;b;c;d\r\n3;8;9;2\r\n')
    observed = colnames(fp, delimiter = ';')
    expected = set('abcd')
    n.assert_set_equal(observed, expected)
