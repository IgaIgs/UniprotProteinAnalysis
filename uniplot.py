import gzip
for l in gzip.open("uniprot_receptor (1).xml.gz"):
    print(l.decode().strip())


