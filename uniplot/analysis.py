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







