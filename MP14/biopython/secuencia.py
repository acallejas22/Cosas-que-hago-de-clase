from Bio import SeqIO


for seq_record in SeqIO.parse("sequence3.fasta","fasta"):
    print(seq_record)
