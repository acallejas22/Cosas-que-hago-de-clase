from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez

Entrez.email='acallejas22@ilg.cat'




handle=Entrez.efetch(db="nucleotide", id="NM_000900.5", rettype="fasta", retmode="text")
handle2=Entrez.efetch(db="nucleotide", id="NM_000900.5", rettype="gb", retmode="text")


with open("fitxerfasta.fasta", "w") as resultats:
        resultats.write(handle.read())

with open("fitxerfasta.gb", "w") as resultats2:
        resultats2.write(handle2.read())
