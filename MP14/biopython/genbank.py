from Bio import Entrez
from Bio import SeqIO


Entrez.email="acallejas22@ilg.cat"

# NM_001128143.2
handle=Entrez.efetch(db="nucleotide", id="NM_001128143.2", rettype="gb", retmode="text")

for rec in SeqIO.parse(handle,"genbank"):
    print(rec.features)
    for feature in rec.features:
        if feature.type == "CDS":
            print(feature.qualifiers['translation'])
            cds = feature.location.extract(rec).seq[:150]
            print(cds)
            arn=cds.transcribe()
            print(arn)
            aa = arn.translate()
            print(aa)
