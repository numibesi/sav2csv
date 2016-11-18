from savReaderWriter import SavReader
from os import path
import sys
import csv
import argparse


class RFC4180(csv.Dialect):
    def __init__(self):
        csv.Dialect.__init__(self)
    delimiter = b','
    doublequote = True
    escapechar = None
    lineterminator = b'\r\n'
    quotechar = b'"'
    quoting = csv.QUOTE_MINIMAL
    skipinitialspace = False
    stric = True

def parseargs():
    pa = argparse.ArgumentParser(
        description='Converts an spss "sav" data file to CSV')
    pa.add_argument('file', metavar='SAV_FILE')
    args = pa.parse_args(sys.argv[1:])
    return vars(args)


def _stringify(dat):
    if isinstance(dat, basestring):
        return dat.encode('utf-8')
    else:
        return dat


def convert(infile, outfile):
    with SavReader(infile, returnHeader=True, ioUtf8=True,
                   recodeSysmisTo='NA') as r:
        with open(outfile, 'w') as fout:
            for l in r:
                l = [_stringify(c) for c in l]
                writer = csv.writer(fout, dialect='RFC4180')
                writer.writerow(l)

def main():
    csv.register_dialect(u'RFC4180', RFC4180)
    infile = parseargs()['file']
    outfile = path.splitext(infile)[0] + '.csv'
    convert(infile, outfile)

if __name__ == '__main__':
    main()
