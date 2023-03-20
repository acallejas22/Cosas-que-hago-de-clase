import Bio
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment


def alinea(cadena1,cadena2):
    valor = 0
    for i in range(len(cadena1)):
        if cadena1[i] == cadena2[i]:
            valor += 1
        else:
            valor -= 1
    return valor

def trencaid(identificador):
    vector = identificador.split("|")
    return vector[3]


## en el diccionari creem les parelles claus valors tals que, cada clau és l'identificador, prèviament
## tractat, i cada valor són els 200 primers nucleòtids de cada seqüència

diccionari = {}

for i in SeqIO.parse("ls_orchid.fasta","fasta"):
    valor = trencaid(i.id) #en valor vull només una part del id
    diccionari[valor] = i.seq[:200]

# a màxim guardarem la màxima puntuació d'una alineació i a cadenammaxim1 i cadenamaxim2 guardarem
## els identificadors de les dues cadenes que tene el màxim alineament

maxim = 0
cadenamaxim1 = ""
cadenamaxim2 = ""
## per crear el document heu de recórrer totes les claus del diccionari i alinear el seu valor amb 
## tots els altres valors
## haureu també de guardar

claus = list(diccionari.keys())

with open("informe.txt", "w") as fitxer:
    for i in range(len(claus)):
        fitxer.write(" treballem amb " + claus[i] + "\n")
        fitxer.write("---------------------------\n")
        for j in range(i + 1, len(claus)):
            valor = alinea(diccionari[claus[i]], diccionari[claus[j]])
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
                aligments = pairwise2.align.globalxx(diccionari[claus[i]], diccionari[claus[j]])

                for aligment in aligments:
                    fitxer2.write(format_alignment(*alignment))
