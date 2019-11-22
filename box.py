import argparse
import pandas as pd
import csv
import numpy as np
import get_gene_counts
import get_tissue_samples



def initialize():
    parser = argparse.ArgumentParser(
                description='Pass parameters',
                prog='box_plot')

    parser.add_argument('--tissues',
                        type=str,
                        help='the tissues you want to plot',
                        required=True)

    parser.add_argument('--genes',
                        type=str,
                        help='the genes you want to plot',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='The file name of the plot to be saved',
                        required=True)

    parser.add_argument('--sample_attributes_file',
                        type=str,
                        help='The name of the file containing sample attrib',
                        required=True)

    parser.add_argument('--gene_counts_file',
                        type=str,
                        help='The name of the file containing gene reads',
                        required=True)

    args = parser.parse_args()
    return args


# def boxplot():






def main():
    args = initialize()
    #pull gene counts
    genes = args.genes
    gene_counts_file = args.gene_counts_file
    gene_counts = get_gene_counts.pull_gene_reads(gene_counts_file, genes)
    print(gene_counts)

    # tissues = args.tissues


    # dv.boxplot(group_counts, groups, gene_name,
               # sample_type_col_name, plot_name)


if __name__ == '__main__':
    main()
