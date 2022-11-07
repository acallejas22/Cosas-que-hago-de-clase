from Bio import SeqIO


for seq_record in SeqIO.parse("sequence3.fasta","fasta"):
    print(seq_record + "\n")

    print("id: " + seq_record.id + "\n")
    print("name: " + seq_record.name + "\n")
    print("description: " + seq_record.description + "\n")
    print("seq: " + seq_record.seq + "\n")


    counterA = 0
    counterT = 0
    counterC = 0
    counterG = 0
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
