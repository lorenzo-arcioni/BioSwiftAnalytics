import sys	

def get_multiple_strand_from_fasta(path: str):
	'''
	Prende in input il file multifasta, dopo di chè per ogni gene aggiunge in un dizionario
	l'entry che ha per chiave il nome del gene e per valore la stringa fasta
	Arguments:
	    path: str
		il path del file
	Returns:
	    ret: dict
		il dizionario costruito
	'''
	
	last_header = None

	ret = dict()
	i = 0
	
	lista = path.split("\n")
	
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

def find_orf(sequence: str):
	lst = []
	
	begin = 0
	while True:
		
		begin = sequence.find("ATG")
		
		if begin < 0:
			break
		
		for i in range(begin, len(sequence)-2):
			if sequence[i:i+3] in ["TAG", "TAA", "TGA"] and i - begin > 100:
				lst.append((begin, i+3))
				#print((begin, i+3), sequence[begin:i+3])
		sequence = sequence[:begin] + "F" + sequence[begin+1:]
		
		begin += 3
	return lst
	
def conta(codice: str, verbose: bool = True):
	'''
	Dato una sequenza fasta (codice) restituisce un dizionario con 5 entry (una per base azotata) ed un contatore per ciascuna di esse
	Argunments:
	    codice: str
		la stringa fasta
	    verbose: bool
		se vogliamo dei print più descrittivi
	Returns:
	    il dizionario costruito
	'''
	# inizializzo il dizionario
	name_mapping = {'A': 'Adenina', 'C': 'Citosina', 'G': 'Guanina', 'T': 'Timina', 'U': 'Uracile'}
	ret = dict()
	# per ogni carattere
	for c in codice:
		c = c.upper()
		if c not in ['A', 'T', 'C', 'G', 'U']: #qualcosa non va
			continue
		else:
			if c in ret: # semplicemente aggiungo 1 alla base corrispondente
				ret[c] += 1
			else:
				ret[c] = 1
	if verbose: # faccio dei print più descrittivi
		for k in ret:
			if ret[k] == 0 and k in ['U', 'T']:
				continue
			print(f"Base azotata: {name_mapping[k]}({k}) numero occorrenze: {ret[k]} frequenza: {round(ret[k]*1.0/sum(ret.values())*100, 3)}")

	return ret

def offsetize(seq: str, offset: int = 69): #Formatta la sequenza con l'offset dato
	i = 0
	lst = []
	while True:
		if len(seq[i:]) > offset:
			lst.append(seq[i : i + offset + 1])
			i = i + offset + 1
		else:
			if seq[i:] != '':
				lst.append(seq[i:])
			break
	return lst
			
def store_fasta(dic: dict, offset: int = 69): #stampa il dizionario con le sequenze nel formato multifasta sullo stdout
	for k in dic.keys():
		print(">" + k)
		
		for x in offsetize(dic[k], offset):
			print(x)

def store_orf(fasta_dic: dict):

	orf = dict()
	
	for x in fasta_dic.keys():
		tup = find_orf(fasta_dic[x])
		i = 1
		for k in tup:
			print(">" + x + " orf " + str(i))
			for y in offsetize(fasta_dic[x][k[0]:k[1]]):
				print(y)
			i += 1

def translate(seq: str):
      
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    protein = ""
    
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    
    if len(seq)%3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    	
    return protein
		
		
	







    
    
   
