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
    with open("NM_000900.5.gb", "r") as fitxergb:
        for rec in SeqIO.parse(fitxergb, "gb"):
            fitxer.write(rec.id)
            print(rec.features[1]) #imprime las features del archivo, siguiendo el índice
            print(rec.features[1].type) #imprime por tipo de feature que encuentra
            print(rec.features[1].qualifiers)
            for feature in rec.features:
                if feature.type == "CDS":
                    cadena = feature.qualifiers['translation']
                    print(cadena[0])
                    print(feature.qualifiers['translation'][0])

