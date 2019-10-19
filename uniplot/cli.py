import argparse
from . import analysis
from uniplot import parse, plot

LOC="uniprot_receptor.xml.gz"

def dump(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

## pass 2 parameters for name function to enable you to choose between printing the names for func(names) or calculating the average for func(average)
def name(args,p=True):
    ##create an empty list of record names to use for average
    n = []
    for record in parse.uniprot_seqrecords(LOC):
        # to run name function and print record.names give the p variable a True value
        if (p == True):
            print(record.name)
            ## also add each of the printed names to the n list created at the beginning of this function definition (to be used in calculating average)
        n.append(record.name)
# return the list of names when called in average(args)
    return n

def average(args):
    print('Average Length is {}'.format(
#print the result of the average_len function calculation using the n list created in 'name' function, without printing all the names (hence p = False)
analysis.average_len(name(args, p = False))))

def plot_average_by_taxa(args):
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)

def cli():
    ## create a new parser
    # a parser in programming: a program which breaks down the input it receives into parts,
    # which can be then managed by other programs
    # parse - dokonywać analizy (gramatycznej, składni), rozbijać na części
    parser = argparse.ArgumentParser(prog='uniplot')

    subparsers = parser.add_subparsers(help='Sub Command Help')

    ## Add subparsers
    subparsers.add_parser('dump').set_defaults(func=dump)
    subparsers.add_parser('list').set_defaults(func=name)
    subparsers.add_parser('average').set_defaults(func=average)
    subparsers.add_parser('plot_average_by_taxa').set_defaults(func=plot_average_by_taxa)

    ## Parse the command line
    args = parser.parse_args()

    ## Take the func argument, which points to our function and call it
    args.func(args)

