import argparse
import pandas as pd


def initialize():
    parser = argparse.ArgumentParser(
                description='Pass parameters',
                prog='gene_gene_counts')

    parser.add_argument('--gene_counts_file',
                        type=str,
                        help='The name of the file containing gene reads',
                        required=True)

    parser.add_argument('--gene',
                        type=str,
                        help='The name of the gene you wish to plot \
                        expression of',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='The file name of the plot to be saved',
                        required=True)

    args = parser.parse_args()
    return args


def pull_gene_reads(gene_counts_file, gene):
    df = pd.read_table(gene_counts_file, header=2)
    df1 = df.drop('Name', axis=1)
    df2 = df1.set_index('Description')
    gene_counts = df2.loc[[gene]]
    return gene_counts


def main():
    args = initialize()
    gene_counts = pull_gene_reads(args.gene_counts_file, args.gene)
    print(gene_counts)


if __name__ == '__main__':
    main()
