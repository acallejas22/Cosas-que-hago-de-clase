from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez

Entrez.email='acallejas22@ilg.cat'



generic= "brca2 homo sapiens transcript variant"
handle= Entrez.esearch(db="nucleotide", term=generic, retmax=10 )
record=Entrez.read(handle)
handle.close()

def parsegar(cadena):
    for req in SeqIO.parse(cadena, "fasta"):
        handle = Entrez.efetch(db="nucleotide", id=req.id, rettype="gb", retmode="text")
        handle.close()

def obtaincds(cadena):
    for req in SeqIO.parse(cadena, "fasta"):
        handle = Entrez.efetch(db="nucleotide", id=req.id, rettype="gb", retmode="text")
        for rec in SeqIO.parse(handle, "genbank"):
            print(rec.features)
            for feature in rec.features:
                if feature.type == "CDS":
                    print(feature.qualifiers['translation'])
                    cds = feature.location.extract(rec).seq[:150]
                    print(cds)
                    arn = cds.transcribe()
                    print(arn)
                    aa = arn.translate()
                    print(aa)

with open("brca2.fasta", "w") as resultats:
    for i in record["IdList"]:
        handle = Entrez.efetch(db="nucleotide", id=i, rettype="fasta")
        resultats.write(handle.read())
        parsegar("brca2.fasta")
      




