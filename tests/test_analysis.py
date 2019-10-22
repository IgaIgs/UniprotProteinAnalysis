import pytest
import uniplot.analysis
import uniplot.parse

TEST_UNIPROT = './resources/uniprot_sprot_small.xml.gz'


def test_average():
    """Test the 'average' function.

    :return: Information on whether the test was passed or not.
    """
    assert uniplot.analysis.average_len(
        uniplot.parse.uniprot_seqrecords(TEST_UNIPROT)
    ) == 302.72222222222223
