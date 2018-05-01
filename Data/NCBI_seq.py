from Bio import Entrez
from Bio import SeqIO
import re
Entrez.email="Candice.chen@utexas.edu"

# Download the Ideonella sakaiensis DNA genome:
download_handle = Entrez.efetch(db="nucleotide", id="BBYR01000007", rettype="gb", retmode="text")
data = download_handle.read()
record=SeqIO.read(download_handle,"genabnk")
download_handle.close()



# Store data into file "ideonella_sakaiensis.txt":
out_handle = open("Seq_bacterium.txt", "w")
out_handle.write(data)
out_handle.close()


