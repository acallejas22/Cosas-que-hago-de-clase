from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez

Entrez.email = 'acallejas22@ilg.cat'



def CountExon(handle):

    for rec3 in SeqIO.parse(handle, "genbank"):
        contador1 = 0
        for feature1 in rec3.features:
            if feature1.type == "exon":
                contador1 += 1
        print(contador1)
        return contador1

def alinea(cadena1,cadena2):
    lenght = 50
    #cambia el tamaño si el array es mas pequeño que el limite de 50
    if len(cadena1) < lenght:
        lenght = len(cadena1)
    elif len(cadena2) < lenght:
        lenght = len(cadena2)

    valor = 0
    for i in range(lenght):
        if cadena1[i] == cadena2[i]:
            valor += 1
        else:
            valor -= 1
    return valor
#compare



aa = ""
aa2 = ""
with open("resultat.txt", "w") as fitxer:
    with open("Homo_sapiens.gb", "w") as fitxer2:
        handle = Entrez.efetch(db="nucleotide", id="NM_001354619.2", rettype="gb", retmode="text")
        for rec3 in SeqIO.parse(handle, "genbank"):
            contador1 = 0
            for feature1 in rec3.features:
                if feature1.type == "exon":
                    contador1 += 1
                if feature1.type == "CDS":
                    cds = feature1.location.extract(rec3).seq[:150]
                    arn = cds.transcribe()
                    aa = arn.translate()
            print(str(contador1))
            print(aa)
    with open("Mus_musculus.gb", "w") as fitxer3:
        handle2 = Entrez.efetch(db="nucleotide", id="NM_001324522.1", rettype="gb", retmode="text")
        for rec2 in SeqIO.parse(handle2, "genbank"):
            contador2 = 0
            for feature2 in rec2.features:
                if feature2.type == "exon":
                    contador2 += 1
                if feature2.type == "CDS":
                    cds2 = feature2.location.extract(rec2).seq[:150]
                    arn2 = cds2.transcribe()
                    aa2 = arn2.translate()
            print(str(contador2))
            print(str(aa2))
    fitxer.write("Les cadenes d'aminoacids de l'homo sapiens i el mus musculis son: " + "\n")
    fitxer.write("------" + "\n")
    fitxer.write(str(aa) + "\n")
    fitxer.write(str(aa2) + "\n")
    fitxer.write("----------------------------------------------------------" + "\n")
    fitxer.write("L'homo sapiens te: " + str(contador1) + " exons" + "\n")
    fitxer.write("El mus musculus te: " + str(contador2) + " exons" + "\n")
    cadena = ""
    fitxer.write("----------------------------------------------------------" + "\n")
    fitxer.write("El percentatje de similitut del seus aminoacids es: " + (str((alinea(aa,aa2)*100)/50)) + "%" + "\n")





