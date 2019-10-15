import argparse
import gzip
from Bio import SeqIO

def dump(args):
    handle = gzip.open('uniprot_receptor.xml.gz')
    for record in SeqIO.parse(handle,'uniprot-xml'):
        print(record)

def name(args):
    handle = gzip.open('uniprot_receptor.xml.gz')
    for record in SeqIO.parse(handle,'uniprot-xml'):
        print(record.name)

def cli():
    ## create a new parser (parser - analizator składni)
    # parser in programming: a program which breaks down the input that it receives into parts,
    # which can be then managed by other programming
    # parse - dokonywać analizy gramatycznej, opisywać gramatycznie
    parser = argparse.ArgumentParser(prog='uniplot')

    subparsers = parser.add_subparsers(help='Sub Command Help')

    ## Add subparsers
    subparsers.add_parser('dump').set_defaults(func=dump)
    subparsers.add_parser('list').set_defaults(func=name)

    ## Parse the command line
    args = parser.parse_args()

    ## Take the func argument, which points to our function and call it
    args.func(args)


