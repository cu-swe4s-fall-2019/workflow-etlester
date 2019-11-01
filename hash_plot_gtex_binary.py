import data_viz as dv
import sys
import argparse
from hash_tables_etlester import hash_tables as ht


def initialize():
    parser = argparse.ArgumentParser(
                description='Pass parameters',
                prog='plot_gtex_binary')

    parser.add_argument('--gene_reads',
                        type=str,
                        help='The name of the file containing gene reads',
                        required=True)

    parser.add_argument('--sample_attributes',
                        type=str,
                        help='The name of the file containing sample \
                        attributes',
                        required=True)
    parser.add_argument('--gene',
                        type=str,
                        help='The name of the gene you wish to plot \
                        expression of',
                        required=True)

    parser.add_argument('--group_type',
                        type=str,
                        help='The type of sample you wish to plot',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='The file name of the plot to be saved',
                        required=True)

    args = parser.parse_args()
    return args


def linear_search(key, D):
    hit = -1
    for i in range(len(D)):
        curr = D[i]
        if key == curr:
            return i
    return -1


def binary_search(key, D):
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if (key < D[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1


def main():
    args = initialize()
    gene_name = args.gene
    plot_name = args.output_file
    gene_reads_file_name = args.gene_reads
    sample_info_file_name = args.sample_attributes
    sample_type_col_name = args.group_type
    sample_id_col_name = "SAMPID"

#   separate the headder from the sample data. Store in two parallel arrays
#   sample_info_header and samples
    sample_info_header = None
    samples = []
    for l in open(sample_info_file_name):
        if sample_info_header is None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))
#   find the column that contains the sample type info
    group_col_idx = linear_search(sample_type_col_name, sample_info_header)
    # print(group_col_idx)
#   find the column that contains the sample ids
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)
    # print(sample_id_col_idx)



    #make hash table for the sample types and sample ids
    groups = []
    members = []
    tissue_types_hash_table = ht.ChainedHash(1000, ht.h_rolling)
    # print(samples)
    for row_idx in range(len(samples)):
        curr_group = samples[row_idx][group_col_idx]
        sample_name = samples[row_idx][sample_id_col_idx]
        key = curr_group
        value = sample_name
        search_result = tissue_types_hash_table.search(curr_group)
        if (search_result is None):
            tissue_types_hash_table.add(curr_group, [sample_name])
            groups.append(curr_group)
        else:
            search_result.append(sample_name)
#       searches a growing list named groups for the current group. and returns
#       the index of the current_group in the list groups
#       if the current group is not found, it adds the current group to the
#       growing list
        curr_group_idx = linear_search(curr_group, groups)
        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
#        if the current group is present in groups, we append the sample name
#        to the growing members list at the location, current group index


    #load gene counts so that we can make a hash table with the gene ID as
    #keys and the gene counts for the specified gene
    version = None
    dim = None
    data_header = None
    gene_name_col = 1

    group_counts = [[] for i in range(len(groups))]
    for l in open(gene_reads_file_name, 'rt'):
        if version is None:
            version = 1
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header is None:
            data_header = l.rstrip().split('\t')
            continue
            # data_header = []
            # i = 0
            # for field in l.rstrip().split('\t'):
            #     data_header.append([field, i])
            #     i += 1
            # data_header.sort(key=lambda tup: tup[0])
            # continue
        A = l.rstrip().split('\t')
        #make hash table of Key = sample_ID and Value = gene_counts
        if A[gene_name_col] == gene_name:
            #initiate gene counts hash table
            gene_counts_hash_table = ht.ChainedHash(1000000, ht.h_rolling)
            #loop through
            for i in range(2, len(data_header)):
                gene_counts_hash_table.add(data_header[i], int(A[i]))

    #search first hash table using groups as keys
    #this will return sample IDs that can be used as keys for
    #hash table 2. this will return gene counts which can be plotted

    # print(tissue_types_hash_table.T)
    group_counts = []
    for i in range(len(groups)):
        counts = []
        sample_id = tissue_types_hash_table.search(groups[i])
        if sample_id is None:
            continue
        for j in sample_id:
            sample_counts = gene_counts_hash_table.search(j)
            if sample_counts is None:
                continue
            counts.append(sample_counts)
        group_counts.append(counts)

    dv.boxplot(group_counts, groups, gene_name,
               sample_type_col_name, plot_name)



if __name__ == '__main__':
    main()
