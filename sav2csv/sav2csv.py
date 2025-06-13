#!/usr/bin/env python3
import argparse
import os
import sys

import pandas as pd
import pyreadstat

def parse_args():
    p = argparse.ArgumentParser(
        description="Convert SPSS .sav to CSV"
    )
    p.add_argument(
        "-f", "--file", required=True,
        help=".sav file to convert"
    )
    p.add_argument(
        "-o", "--outdir", default=None,
        help="Output directory (default: same as input file)"
    )
    return p.parse_args()

def convert(sav_path, csv_path):
    # read both data and metadata (we just dump data)
    df, meta = pyreadstat.read_sav(sav_path, apply_value_formats=False)
    df.to_csv(csv_path, index=False, encoding="utf-8")

def main():
    args = parse_args()
    in_sav = args.file
    out_dir = args.outdir or os.path.dirname(in_sav)
    base = os.path.splitext(os.path.basename(in_sav))[0]
    out_csv = os.path.join(out_dir, base + ".csv")

    try:
        convert(in_sav, out_csv)
        print(f"Written CSV to: {out_csv}")
    except Exception as e:
        print("Failed to convert:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
