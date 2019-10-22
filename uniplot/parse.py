import gzip
from Bio import SeqIO


def uniprot_seqrecords(file_location):
    """Create a list of protein records found in the file.

    :param file_location: The location of the file to be analysed.
    :return: A list of protein records.
    """
    records = []

    handle = gzip.open(file_location)
    for record in SeqIO.parse(handle, 'uniprot-xml'):
        records.append(record)

    return records
