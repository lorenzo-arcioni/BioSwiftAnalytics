import argparse
import os
from collections import defaultdict

# Funzione per leggere il dizionario da un file di testo.
def read_dictionary(dict_file):
    with open(dict_file, 'r') as file:
        # Crea un dizionario dove ogni linea del file viene divisa in chiave e valore.
        return {line.split()[0]: line.split()[1] for line in file.readlines()}

# Funzione per trovare file corrispondenti in base ai valori del dizionario.
def find_matching_files(input_dir, file_extension, value_dict):
    matching_files = defaultdict(list)
    for file in os.listdir(input_dir):
        # Controlla se il file termina con l'estensione desiderata.
        if file.endswith(file_extension):
            for key, value in value_dict.items():
                # Se il valore del dizionario è presente nel nome del file, aggiungi il file alla lista corrispondente.
                if value in file:
                    matching_files[key].append(os.path.join(input_dir, file))
    return matching_files

# Funzione per leggere gli ID dei geni da una lista di percorsi di file.
def read_gene_ids(file_paths):
    gene_ids = set()
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            next(file)  # Salta la prima riga (intestazioni dei campi)
            for line in file:
                parts = line.split()
                if parts:
                    gene_id = parts[0]
                    gene_ids.add(gene_id)
    return gene_ids


# Funzione principale del programma.
def main():
    parser = argparse.ArgumentParser(description="Gene ID Matching Tool")
    # Definisce gli argomenti che il programma accetterà dalla riga di comando.
    parser.add_argument("--dict", required=True, help="Path to dictionary file")
    parser.add_argument("--inputdir", required=True, help="Input directory path")
    parser.add_argument("--ext", required=True, help="File extension to search")
    parser.add_argument("--outdir", required=True, help="Output directory path")
    args = parser.parse_args()

    # Assegna i valori degli argomenti alle variabili corrispondenti.
    dict_file = args.dict
    input_dir = args.inputdir
    file_extension = args.ext
    out_dir = args.outdir

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Legge il dizionario e trova i file corrispondenti.
    value_dict = read_dictionary(dict_file)
    matching_files = find_matching_files(input_dir, file_extension, value_dict)

    # Crea un dizionario per tracciare gli ID dei geni condivisi.
    shared_gene_ids = defaultdict(set)
    for key, file_paths in matching_files.items():
        gene_ids = read_gene_ids(file_paths)
        for gene_id in gene_ids:
            # Aggiunge la chiave del dizionario agli ID dei geni condivisi.
            shared_gene_ids[gene_id].add(key)

    # Scrive i risultati nei file di output.
    for gene_id, keys in shared_gene_ids.items():
        if len(keys) > 1:
            filename = '_'.join(sorted(keys)) + '.txt'
            with open(os.path.join(out_dir, filename), 'a') as file:
                file.write(gene_id + '\n')

# Esegue la funzione principale se lo script è il modulo principale eseguito.
if __name__ == "__main__":
    main()

