import statistics


def average_len(records):
    """Calculate the average length of proteins' sequences (records).

    :param records: a list of proteins in a file.

    :return: The average length of all lengths in the 'lengths' list (average length of records.)
    """
    # Create an empty list 'lengths' to which the lengths of individual records will be added.
    # This will enable the calculation of the average length.
    lengths = []
    for name in records:
        # Add each of the records' length to the lengths list
        lengths.append(len(name))
    return statistics.mean(lengths)


def average_len_taxa(records):
    """Calculate the average length of proteins' sequences for the top level taxa.

    :param records: a list of proteins in a file.
    :return: an average length of protein sequences by taxa.
    """
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][0]
        record_by_taxa.setdefault(taxa, []).append(r)

    return{taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
