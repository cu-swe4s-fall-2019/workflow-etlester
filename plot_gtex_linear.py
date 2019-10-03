import data_viz as dv


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

        if key == D[mid]:
            return D[mid]

        if (key < D[mid]):
            hi = mid
        else:
            lo = mid

    return -1


def main():
    gene_name = "ACTA2"
    tissue_type = "SMTS"
    plot_name = 'test.png'

    gene_reads_file_name = 'GTEx_Analysis_2017-06-05_v8_' \
        'RNASeQCv1.1.9_gene_reads.acmg_59.gct'
    sample_info_file_name = 'GTEx_Analysis_v8_Annotations' \
        '_SampleAttributesDS.txt'
    sample_type_col_name = tissue_type
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

    groups = []
    members = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]
#       searches a growing list named groups for the current group. and returns
#       the index of the current_group in the list groups
#       if the current group is not found, it adds the current group to the
#       growing list
        curr_group_idx = linear_search(curr_group, groups)
        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])
#        if the current group is present in groups, we append the sample name
#        to the growing members list at the location, current group index
        members[curr_group_idx].append(sample_name)
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

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    member_idx = linear_search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break

    # print(group_counts)
    dv.boxplot(group_counts, groups, gene_name, tissue_type, plot_name)


if __name__ == '__main__':
    main()
