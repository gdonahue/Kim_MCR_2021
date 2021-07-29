# Kim_MCR_2021
Bioinformatics code for Kim et al Mol Cancer Res 2021

Contains a bash shell script (run_homer.2.sh) used to perform motif analysis on target promoters using HOMER. Backgrounds were generated using the python script select_random.py, which samples from a list of 1kb upstream-of-TSS promoter regions.

Promoters and background promoters are included, along with promoter locations sampled to make background files. The color coding corresponds to a heatmap clustering of RNA-seq data (differentially expressed genes only) and the complete legend is given in our manuscript. Here is a brief description:

Yellow: promoters of genes (such as cell cycle regulators) significantly increased in HBP1-OE compared to controls
Blue: promoters of genes (some encoding growth factors) which are also upregulated in HBP1-OE
Purple: promoters of genes (type I interferon pathways or ncRNA processing) significantly  downregulated  in HBP1-OE
Red: same as purple
Green: other genes

Other methodological details (alignment, gene counts, etc) are given in the manuscript.

Unfortunately the random seed used to generate the background was not recorded.
