from savReaderWriter import SavReader
import os.path
import sys
import csv
import argparse
from Tkinter import Tk
import tkFileDialog


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
    pa.add_argument('-f', metavar='SAV_FILE',
                    help='The .sav file to export. ' +
                    'If omitted, a graphical file chooser will be used.')
    pa.add_argument('-o', metavar='OUTPUTDIRECTORY',
                    help='The output directory. Default is the current ' +
                    'directory if SAV_FILE was given, otherwise a ' +
                    'file chooser will be used as well.')
    args = pa.parse_args(sys.argv[1:])
    return vars(args)


def _stringify(dat):
    if not isinstance(dat, basestring):
        return str(dat).encode('utf-8')
    else:
        return dat.encode('utf-8')

def convert(infile, outfile):
    with SavReader(infile, returnHeader=True, ioUtf8=True,
                   recodeSysmisTo='NA') as r:
        with open(outfile, 'w') as fout:
            for l in r:
                l = [_stringify(c) for c in l]
                writer = csv.writer(fout, dialect='RFC4180')
                writer.writerow(l)

def get_paths():
    home = os.path.expanduser('~')
    infile = parseargs()['f']
    out_dir = parseargs()['o']
    if infile is None:
        root = Tk()
        root.withdraw()
        f = tkFileDialog.askopenfile(title='Choose file to convert',
                                      filetypes=[('sav', '*.sav')],
                                      initialdir=home)
        if f:
            infile = f.name
            f.close()
        else:
            sys.exit()
        if out_dir is None:
            out_dir = tkFileDialog.askdirectory(title='Choose output directory',
                                                initialdir=home)
            if not out_dir:
                sys.exit()
        root.destroy()
    if not out_dir:
        out_dir = os.getcwd()
    return (infile, out_dir)

def main():
    csv.register_dialect(u'RFC4180', RFC4180)
    infile, out_dir = get_paths()
    outfilename = os.path.splitext(os.path.basename(infile))[0] + '.csv'
    outfile = os.path.join(out_dir, outfilename)
    convert(infile, outfile)

if __name__ == '__main__':
    main()
