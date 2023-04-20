from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez

Entrez.email = 'acallejas22@ilg.cat'
diccionario = {}



"""--------------------- Código no completado ----------------------"""






""" Moléculas: NM_001190839.3, XM_003816517.4, XM_520764.6, NM_000900.5"""





with open("XM_520764.6.gb", "w") as fitxer:
    handle = Entrez.efetch(db="nucleotide", id="NM_001190839.3, XM_003816517.4, XM_520764.6, NM_000900.5", rettype="gb", retmode="text")
    record = Entrez.read(handle)
    fitxer.write(handle.read())

with open("resultatgb.txt", "w") as fitxer:
    with open("XM_520764.6.gb", "r") as fitxergb:
        for rec in SeqIO.parse(fitxergb, "gb"):
            fitxer.write(rec.id)
            for feature in rec.features:
                if feature.type == "CDS":
                    cadena = feature.qualifiers['translation']
                    #print(cadena[0])
                    print(feature.qualifiers['translation'][0])

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
            contador=0
            for feature in rec.features:
                if feature.type == "exon":
                    contador +=1
                if feature.type == "CDS":
                    cds = feature.location.extract(rec).seq[:150]
                    arn = cds.transcribe()
                    aa = arn.translate()
                    diccionario[req.id] = aa


with open("brca2.fasta", "w") as resultats:
    for i in record["IdList"]:
        handle = Entrez.efetch(db="nucleotide", id=i, rettype="fasta")
        resultats.write(handle.read())
        parsegar("brca2.fasta", diccionario)



maxim = 0
cadenamaxim1 = ""
cadenamaxim2 = ""
claus = list(diccionario.keys())
with open("informe.txt", "w") as fitxer:
    for i in range(len(claus)):
        fitxer.write(" treballem amb " + claus[i]  + "\n")
        fitxer.write("---------------------------\n")
        for j in range(i + 1, len(claus)):
            valor = alinea(diccionario[claus[i]], diccionario[claus[j]])
            fitxer.write(str(valor) + " punts amb " + claus[j] + ": \n")
            if valor <= maxim:
                maxim = valor
                cadenamaxim1 = claus[i]
                cadenamaxim2 = claus[j]
