import statistics


def average_len(records):
    #create an empty list 'lengths' to which the lenghts of individual record names will be added
    #this will enable the calculation of the average length
    lengths = []
    for name in records:
        #add each of the records' length to the lenghts list
        lengths.append(len(name))
#calculate the average lenght of all lengths in lenght list (so the average lenght of the records)
    return statistics.mean(lengths)


def average_len_taxa(records):
    """Returns the average length for the top level taxa"""
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][0]
        record_by_taxa.setdefault(taxa, []).append(r)

    return{taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
