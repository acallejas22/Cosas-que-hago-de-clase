from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez

Entrez.email = 'acallejas22@ilg.cat'

with open("NM_000900.5.fasta", "w") as fitxer:
    handle = Entrez.efetch(db="nucleotide", id="NM_000900.5", rettype="fasta", retmode="text")
    fitxer.write(handle.read())

with open("resultat.txt", "w") as fitxer:
    with open("NM_000900.5.fasta") as handle:
        for rec in SeqIO.parse(handle, "fasta"):
            fitxer.write(rec.id + "\n")
            fitxer.write(rec.description + "\n")
            fitxer.write(str(rec.seq))
            fitxer.write(str(rec.seq)[0:50])
            print(rec)

with open("NM_000900.5.gb", "w") as fitxer:
    handle = Entrez.efetch(db="nucleotide", id="NM_000900.5", rettype="gb", retmode="text")
    fitxer.write(handle.read())

with open("resultatgb.txt", "w") as fitxer:
    with open("NM_000900.5.gb") as fitxergb:
        fitxer.write(rec.id)


"""with open("fitxerfasta.gb", "w") as resultats2:
        resultats2.write(handle2.read())
with open("fitxerfasta.txt", "w") as resultats3:
        for rec in SeqIO.parse(handle2, "genbank"):
             resultats3.write(rec.id)"""
