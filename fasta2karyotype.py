import sys

from optparse import OptionParser


def get_multiple_strand_from_fasta(path: str):
	
    with open(path) as f:
        fasta_file = f.read()
        f.close()
		
    last_header = None

    ret = dict()
    i = 0

    lista = fasta_file.split("\n")

    lista = list(filter(lambda a: a != "", lista))
	
    for line in lista:
        # se inizia con '>' è una nuova sequenza
        if line[0] == '>': 
            # prendo il nome del gene evitando '>' (1:) e lo pulisco (strip)
            last_header = line[1:]
            ret[last_header] = "" # inizializzo il suo valore nel dizionario
        # se non inizia con '>' è un pezzo di sequenza
        else:
            ret[last_header] += line.strip().upper() # Aggiungo la sequenza pulita ed in maiuscolo all'ultimo gene trovato
    return ret

def get_karyotype_from_fasta(path: str, output: str = "karyotype.tsv"):
    
    fasta_dic = get_multiple_strand_from_fasta(path)

    with open(output, "w") as karyotype_file:
        karyotype_file.write("chr\tstart\tend\n")

        for k in fasta_dic.keys():
            karyotype_file.write(k.split(" ")[0] + "\t" + str(0) + "\t" + str(len(fasta_dic[k])) + "\n")
        karyotype_file.close()


get_karyotype_from_fasta("/home/lorenzo/Documenti/microalghe/Stramenopiles/Craspedostauros_australis_2/GCA_026770025.1/GCA_026770025.1_DD_uo2022_genomic.fna")

