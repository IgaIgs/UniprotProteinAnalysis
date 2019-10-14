import gzip
for l in gzip.open("uniprot_receptor (1).xml.gz"):
    print(l.decode().strip())

from Bio import SeqIO
handle = gzip.open("uniprot_receptor (1).xml.gz")
for record in SeqIO.parse(handle, "uniprot-xml"):
    print(record)



