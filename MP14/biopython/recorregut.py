from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez

Entrez.email='acallejas22@ilg.cat'



generic= "mlh1 homo sapiens transcript variant"
handle= Entrez.esearch(db="nucleotide", term=generic, retmax=10 )
record=Entrez.read(handle)
handle.close()


with open("fitxerfasta.fasta", "w") as resultats:
    for i in record["IdList"]:
        handle = Entrez.efetch(db="nucleotide", id=i, rettype="fasta")
        resultats.write(handle.read())


        for req in SeqIO.parse("fitxerfasta.fasta","fasta"):
            print(req.id)
