#!/usr/bin/python
# Randomly chooses background promoters among genes not in the specified cluster
# Assumes that the input BED file has the RefSeq transcript ID in the fourth
# column, delimited by "_up_" as the first token
# See the promoter annotation file (on GitHub) for reference
#      Laboratory of Ken Zaret
#      Penn Epigenetics Institute
#      Department of Cell & Developmental Biology
#      Perelman School of Medicine
#      The University of Pennsylvania
# Greg Donahue, 08-14-2018
# ------------------------------------------------------------------------------
import sys, os, random
# ------------------------------------------------------------------------------
# GLOBALS
# The usage string
usage = "USAGE: python select_random.py BED SEED"

# The promoter annotation file (made using UCSC Genome Browser Table Browser)
promoter_annotation_file = "RefSeq_Promoters1kb.hg19.bed"

# ------------------------------------------------------------------------------
# FUNCTIONS
# The main function
def main(args):

    # Check command-line arguments
    if len(args) != 3: sys.exit(usage)
    if not os.path.exists(args[1]): sys.exit("Can\t find file: "+args[1]+"\n"+ \
                                             usage)
    try: seed = int(args[2])
    except Exception as e: sys.exit("Random seed must be an integer > 0\n"+ \
                                    usage)
    if seed <= 0: sys.exit("Random seed must be an integer > 0\n"+usage)

    # Load list of target RefSeq IDs
    transcripts = list()
    with open(args[1]) as f:
        for line in f:
            t = line.rstrip().split("\t")
            transcripts.append(t[3].split("_up_")[0])
    transcripts = set(transcripts)

    # Load a dictionary REFSEQ_ID:(CHROMOSOME,START,STOP,REFSEQ_ID,STRAND)
    promoters = dict()
    with open(promoter_annotation_file) as f:
        for line in f:
            t = line.rstrip().split("\t")
            refseq_id = t[3].split("_up_")[0]
            record = (t[0],int(t[1]),int(t[2]),refseq_id,t[5])
            promoters[refseq_id] = record
    universe = set(list(promoters.keys()))

    # Get the random background transcripts and report their promoter loci
    background = random.sample(list(universe.difference(transcripts)),
                               len(transcripts))
    for B in background:
        P = promoters[B]
        print(P[0]+"\t"+str(P[1])+"\t"+str(P[2])+"\t"+B+"\t0\t"+P[4])

# ------------------------------------------------------------------------------
# The following code is executed upon command-line invocation
if __name__ == "__main__": main(sys.argv)

# ------------------------------------------------------------------------------
# EOF
