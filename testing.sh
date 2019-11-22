test -e ssshtest || wget -q \
https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# test get_gene_counts.py conformity to PEP8
run style_test pycodestyle get_gene_counts.py
assert_no_stdout

#test to see if you get back the first col of the gene SDHB
run gene_counts_correct python get_gene_counts.py --gene_counts_file \
GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct \
--gene SDHB \
--output_file gene_counts.csv

assert_exit_code 0
assert_no_stderr
assert_stdout
assert_in_stdout SDHB
assert_in_stdout 1993

run tissue_samples_correct python get_tissue_samples.py \
--sample_attributes_file \
GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--tissue_group SMTS \
--output_file tissue_samples.csv

assert_exit_code 0
assert_stdout
assert_in_stdout Bladder
