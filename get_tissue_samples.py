import argparse
import pandas as pd
import csv
import numpy as np


def initialize():
    parser = argparse.ArgumentParser(
                description='Pass parameters',
                prog='gene_gene_counts')

    parser.add_argument('--sample_attributes_file',
                        type=str,
                        help='The name of the file containing sample attrib',
                        required=True)

    parser.add_argument('--tissue_group',
                        type=str,
                        help='the tissue group you want to plot',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='The file name of the plot to be saved',
                        required=True)

    args = parser.parse_args()
    return args


def pull_tissue_type(sample_attributes_file,tissue_group):
    df = pd.read_table(sample_attributes_file, header=0)
    tissues = df[tissue_group]
    sampIDs = df['SAMPID']
    sampID_and_tissue_groups = pd.concat([tissues, sampIDs], axis=1)
    grouped = sampID_and_tissue_groups.groupby(tissue_group)['SAMPID']
    unique_tissues = tissues.unique()
    df_array = pd.DataFrame()
    for i in range(0, len(unique_tissues)):
        current_sample_IDs = grouped.get_group(unique_tissues[i])
        current_sample_IDs_list = current_sample_IDs.to_list()
        current_headder = unique_tissues[i]
        current_df = pd.DataFrame({current_headder: current_sample_IDs})
        df_array = df_array.append(current_df)
    return df_array




def main():
    args = initialize()
    grouped = pull_tissue_type(args.sample_attributes_file, args.tissue_group)
    print(grouped)
    grouped.to_csv(args.output_file)


if __name__ == '__main__':
    main()
