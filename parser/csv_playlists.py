import sys

import pandas as pd


def main(*args):
    library_csv_path, *_ = args
    df = pd.read_csv(library_csv_path, encoding='utf_16_le', sep='\t')
    print(get_duplicates(df))


def get_duplicates(df):
    return df[df.duplicated(['Location'], keep=False)]


if __name__ == '__main__':
    main(*sys.argv[1:])
