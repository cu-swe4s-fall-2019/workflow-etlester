

python -m cProfile -s tottime plot_gtex_linear.py >> plot_gtex.linear_search.txt

python -m cProfile -s tottime plot_gtex_binary.py >> plot_gtex.binary_search.txt
