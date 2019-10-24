import statistics


def average_len(records):
    """Calculate the average length of proteins' sequences.

    :param records: a list of proteins in a file.

    :return: Mean length of proteins found in analysed file.
    """
    # Create an empty list 'lengths' to which the lengths of individual protein records will be added.
    # This will enable the calculation of the average length.
    lengths = []
    for sequence in records:
        # Add each of the records' length to the lengths list
        lengths.append(len(sequence))
    return statistics.mean(lengths)


def average_len_taxa(records, depth):
    """Calculate the average length of proteins' sequences for the top level taxa.

    :param depth: The number of taxa that this function will calculate averages for.
    :param records: a list of proteins in a file.
    :return: an average length of protein sequences by taxa.
    """
    record_by_taxa = {}
    for r in records:
        # only run the function with the specified depth if the record has all the required taxa levels specified.
        if len(r.annotations['taxonomy']) > depth:
            taxa = r.annotations["taxonomy"][depth]
            record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa: average_len(record) for (taxa, record) in record_by_taxa.items()}
