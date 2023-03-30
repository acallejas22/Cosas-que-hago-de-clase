from Bio import SeqIO, pairwise2
from Bio.Seq import Seq
from Bio import Entrez
from Bio.pairwise2 import format_alignment

Entrez.email='acallejas22@ilg.cat'

def alinea(cadena1,cadena2):
    valor = 0
    for i in range(len(cadena1)):
        if cadena1[i] == cadena2[i]:
            valor += 1
        else:
            valor -= 1
    return valor






def parsegar(cadena,diccionario):
    for req in SeqIO.parse(cadena, "fasta"):
        handle = Entrez.efetch(db="nucleotide", id=req.id, rettype="gb", retmode="text")
        for rec in SeqIO.parse(handle, "genbank"):
            print(req.description)
            print(rec.features)
            contador=0
            for feature in rec.features:
                if feature.type == "exon":
                    contador +=1
                    print("l'exó " + str(contador) + " está a: ")
                    print(feature.location)
                if feature.type == "CDS":
                    print(feature.qualifiers['translation'])
                    print(feature.location.extract(rec).seq[:150])
                    cds = feature.location.extract(rec).seq[:150]
                    arn = cds.transcribe()
                    aa = arn.translate()
                    print(aa)
                    diccionario[req.id] = aa


def counter():
    for req in SeqIO.parse("brca2.fasta", "fasta"):
        handle = Entrez.efetch(db="nucleotide", id=req.id, rettype="gb", retmode="text")
        for rec in SeqIO.parse(handle, "genbank"):
            c=0
            for feature in rec.features:
                if feature.type == "exon":
                    c +=1
    return c

diccionario = {}
generic= "brca2 homo sapiens transcript variant"
handle = Entrez.esearch(db="nucleotide", term=generic, retmax=10)
record = Entrez.read(handle)

with open("brca2.fasta", "w") as resultats:
    for i in record["IdList"]:
        handle = Entrez.efetch(db="nucleotide", id=i, rettype="fasta")
        resultats.write(handle.read())
        parsegar("brca2.fasta", diccionario)
    print(diccionario.keys())
    print(diccionario.values())



maxim = 0
cadenamaxim1 = ""
cadenamaxim2 = ""
claus = list(diccionario.keys())
with open("informe.txt", "w") as fitxer:
    for i in range(len(claus)):
        fitxer.write(" treballem amb " + claus[i] + " que te " + str(counter()) + " exons " + "\n")
        fitxer.write("---------------------------\n")
        for j in range(i + 1, len(claus)):
            valor = alinea(diccionario[claus[i]], diccionario[claus[j]])
            fitxer.write(str(valor) + " punts amb " + claus[j] + ": \n")
            if valor <= maxim:
                maxim = valor
                cadenamaxim1 = claus[i]
                cadenamaxim2 = claus[j]
        fitxer.write("---------------------------\n")
    fitxer.write("EL MILLOR ALINEAMENT ES ENTRE: " + cadenamaxim1 + " i " + cadenamaxim2 + "\n")
    fitxer.write("EL MILLOR ALINEAMENT TE: " + str(maxim) + "punts" + "\n")
    with open("iforme.txt", "w") as fitxer2:
        for i in range(len(claus)):
            for j in range(i + 1, len(claus)):
                fitxer2.write("alineaments entre: " + claus[i] + " i " + claus[j] + "\n")
                fitxer2.write("-----------------------------------------------\n")
                fitxer2.write("-----------------------------------------------\n")
                aligments = pairwise2.align.globalxx(diccionario[claus[i]], diccionario[claus[j]])

                for aligment in aligments:
                    fitxer2.write(format_alignment(*aligment))
