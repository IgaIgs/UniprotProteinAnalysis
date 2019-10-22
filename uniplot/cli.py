import argparse
from uniplot import analysis
from uniplot import parse, plot

LOC = "uniprot_receptor.xml.gz"


def dump(args):
    """Print out the uncompressed file containing protein information.

    :param args: A reference to the 'dump' sub-command defined in the subparsers below.
    :return: Printed file.
    """
    for record in parse.uniprot_seqrecords(LOC):
        print(record)


# pass 2 parameters for name function to enable you to choose between printing the names for func(names) or
# calculating the average for func(average)
def name(args, p=True):
    """Print out the names of all the proteins in the file.

    :param args: A reference to the 'name' sub-command defined in the subparsers below.
    :param p: Should the names of proteins be printed?

    :return: Names of proteins.
    """
    # create an empty list of record names to use for calculating average length
    n = []
    for record in parse.uniprot_seqrecords(LOC):
        # to run name function and print record.names give the p variable a True value
        if (p == True):
            print(record.name)
        # also add each of the printed names to the n list created at the beginning of this function definition
        # (to be used in calculating average)
        n.append(record.name)
    # return the n list to the average function
    return n


def average(args):
    """Print the average length of records in the file (protein names).

    :param args: A reference to the 'average' sub-command defined in the subparsers below.
    :return: Average length of names.
    """
    print('Average Length is {}'.format(
        # print the result of the average_len function using the 'n' list created in 'name' function,
        # but DO NOT print all the record names (hence p = False)
        analysis.average_len(name(args, p=False))))


def plot_average_by_taxa(args):
    """Display a bar graph with previously defined features.

    :param args: A reference to the 'taxa_average' sub-command defined in the subparsers below.
    :return: A bar graph with average protein sequence lengths organized by taxa.
    """
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)


def cli():
    """Enable and simplify app management via the terminal."""
    # Create the main parser.
    parser = argparse.ArgumentParser(prog='uniplot', description='Access some information about the proteins.')
    # Add a second parser to enable file location configuration.
    second_parser = argparse.ArgumentParser(prog='second_uniplot')

    subparsers = parser.add_subparsers(help='Sub Command Help')

    # Add subparsers
    subparsers.add_parser('dump', help='Use dump function to display the whole file').set_defaults(func=dump, )
    subparsers.add_parser('list', help='The list function displays a list of all protein names in the file'). \
        set_defaults(func=name)
    subparsers.add_parser('average', help='This shows the average sequence length of the proteins in the file'). \
        set_defaults(func=average)
    subparsers.add_parser('taxa_average_graph', help='Display a bar graph of average protein sequence lengths by taxa'). \
        set_defaults(func=plot_average_by_taxa)

    # Add argument to the main parser so that the help message can be displayed.
    parser.add_argument('--file_location', help="Input the location of the file after '--'")
    # Add argument to the second parser to set a default file location.
    second_parser.add_argument('--file_location', default='uniprot_receptor.xml.gz')

    # Parse the command line
    # Unknown to let the function accept new file_location and 'known' to use only arguments within the parser
    args, unknown = parser.parse_known_args()

    # Take the func argument, which points to our function and call it
    args.func(args)