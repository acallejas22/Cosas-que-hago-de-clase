from Bio import SeqIO
#from Bio import Entrez
def  compte(cadena):
    counterAA = 0
    counterCC = 0
    counterGG = 0
    counterTT = 0
    for i in cadena:
        if i =="A":
            counterAA +=1
    return counterAA, counterCC, counterGG, counterTT

print("-------------------------------")


for seq_record in SeqIO.parse("sequence3.fasta",  "fasta"):
    print(seq_record + "\n")

    #print("id: " + seq_record.id + "\n")
    #print("name: " + seq_record.name + "\n")
    #print("description: " + seq_record.description + "\n")
    #print("seq: " + seq_record.seq + "\n")
    print(seq_record.seq)
    complementaria = seq_record.seq.complement()
    print(complementaria)
    #a,c,g,t = compte(seq_record.seq)
    #acom = compte(complementaria)
    # print(a,c,g,t, acom)
    arn = complementaria.transcribe()
    print(arn)
    protein = arn.translate()
    print(protein)

    counterA = 0
    counterT = 0
    counterC = 0
    counterG = 0
    countera = 0
    countert = 0
    counterc = 0
    counterg = 0
    for i in seq_record.seq:
        if i == "A":
            counterA +=1
        if i == "C":
            counterC +=1
        if i == "T":
            counterT +=1
        if i == "G":
            counterG +=1

    print(counterA)
    print(counterC)
    print(counterG)
    print(counterT)
    print("-------------------------------")
    for i in complementaria:

        if i == "A":
            countera +=1
        if i == "C":
            counterc +=1
        if i == "T":
            countert +=1
        if i == "G":
            counterg +=1
    print(countera)
    print(counterc)
    print(counterg)
    print(countert)





if counterA == countert:
    print("Todo bien en A y t")
elif counterT == countera:
        print("T y a tan bien")
else:
    print("T y a y A y t tan mal")

if counterC == counterg:
    print("Todo bien en C y g")
elif counterG == counterc:
        print("G y c tan bien")
else:
    print("G y c y C y g tan mal")













