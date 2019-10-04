# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

Update:
- binary search was 12.718 seconds faster than linear search on the
same gene (ACTA2)
- updated .travis.yml



What this repo does:
- This script takes in a variety of RNAseq expression datasets as well as a
file that describes the samples, and a gene name and plots the gene expression
data by tissue type as a histogram

Usage examples:
- Plot tissue gene expression data for the gene BRCA2:

'''
python plot_gtex_binary.py \
--gene_reads \
GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct \
--sample_attributes \
GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene BRCA2 \
--group_type SMTSD \
--output_file plot_test.png
'''

Installation:
- To install python, we first have to install homebrew

'''
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
'''

Next, install python3 using homebrew

'''
brew install python
'''

Now we can install conda

'''
cd $HOME
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
. $HOME/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels r
echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
'''

create an environment and activate it

'''
conda create --yes -n my_env
conda activate my_env
'''

install argparse and pycodestyle using conda

'''
conda install pycodestyle
conda install argparse
'''

Next you can try running plot_gtex_binary.py on your own data

'''
python plot_gtex_binary.py \
--gene_reads \
GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct \
--sample_attributes \
GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene BRCA2 \
--group_type SMTSD \
--output_file plot_test.png
'''

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
