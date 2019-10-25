import argparse
from uniplot import analysis
from uniplot import parse, plot

LOC = "uniprot_receptor.xml.gz"
depth = 0
pie_chart = ''
bar_graph = ''


def dump(args):
    """Print out the uncompressed file containing protein information.

    :param args: A reference to the 'dump' sub-command defined in the subparsers below.
    :return: Printed file.
    """
    for record in parse.uniprot_seqrecords(LOC):
        print(record)


def name(args):
    """Print out the names of all the proteins in the file.

    :param args: A reference to the 'name' sub-command defined in the subparsers below.
    :return: Names of proteins.
    """
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)


def average(args):
    """Print the average length of protein sequences in the file.

    :param args: A reference to the 'average' sub-command defined in the subparsers below.
    :return: Average length of protein sequences.
    """
    print("Average length is {}".format(
        # print the results of the average_len function in analysis.py
        analysis.average_len(parse.uniprot_seqrecords(LOC))))


def plot_average_by_taxa(args):
    """Display a bar graph or a pie chart with previously defined features.

    :param args: A reference to the 'taxa_average' sub-command defined in the subparsers below.
    :return: A bar graph or a pie chart with average protein sequence lengths organized by taxa.
    """
    # turning the depth variable to a dictionary to avoid the type error
    dpth = vars(args)["depth"]
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC), dpth)
    if pie_chart:
        plot.plot_pie_show(av)
    elif bar_graph:
        plot.plot_bar_show(av)
    else:
        print('Input -pie for a pie chart or -bar for a bar graph')


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
    subparsers.add_parser('taxa_average_figure', help='Display a figure depicting average protein lengths by taxa'). \
        set_defaults(func=plot_average_by_taxa)

    # Add argument to the main parser so that the help message can be displayed.
    parser.add_argument('--file_location', help='''Input the location of the file after '--file_location ',
    but before the function you want to call.''', type=str)
    parser.add_argument('-d', '--depth', help='''Input an integer for the number of taxa levels that you want the figure 
    to display averages for. The "--depth=" has to be put before the "taxa_average_graph".''', type=int, default=0)
    parser.add_argument('-pie', action='store_true', help='''Draw a pie chart with average protein lengths. Has to be
    input before the name of the function.''', dest='pie_chart')
    parser.add_argument('-bar', action='store_true', help='''Draw a bar graph with average protein lengths. Has to be
    input before the name of the function.''', dest='bar_graph')
    # Add argument to the second parser to set a default file location.
    second_parser.add_argument('--file_location', default='uniprot_receptor.xml.gz')

    # Parse the command line
    args = parser.parse_args()
    global pie_chart
    pie_chart = args.pie_chart
    global bar_graph
    bar_graph = args.bar_graph

    # Take the func argument, which points to our function and call it
    args.func(args)
