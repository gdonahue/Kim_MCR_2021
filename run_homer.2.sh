#!/bin/bash
# Runs HOMER motif finding on target promoters
# Uses LSF job scheduler & UPenn School of Medicine high-performance cluster
#      Laboratory of Ken Zaret
#      Penn Epigenetics Institute
#      Department of Cell & Developmental Biology
#      Perelman School of Medicine
#      The University of Pennsylvania
# Greg Donahue, 08-14-2018
# ------------------------------------------------------------------------------
for color in {red,yellow,blue,green,purple} # For each promoter cluster...
do
    P=Promoters/"$color".bed                # Set the foreground and background
    B=Promoters/"$color".bg.bed
    mkdir -p Motifs/"$color"/PP             # Creates a folder for HOMER output
    bsub -n 16 -M 16000 -o "${P//.bed/.log}" findMotifsGenome.pl "$P" hg19 Motifs/"$color" -size given -mask -p 16 -preparsedDir Motifs/"$color"/PP -bg "$B"
done
# ------------------------------------------------------------------------------
exit 0
