import argparse

from uniplot import parse

LOC='uniprot_receptor.xml.gz'

def dump(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def name(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

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

    ## Parse the commend line
    args = parser.parse_args()

    ## Take the func argument, which points to our function and call it
    args.func(args)

