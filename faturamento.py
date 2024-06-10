
import os
import pandas as pd

def read_text_files(directory):
    dataframes = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                # Leitura do arquivo de texto
                content = file.readlines()
                # Para arquivos de texto tenha colunas separadas por vírgula(csv) ou tabulação.
                # Ajuste o delimitador conforme necessário.
                delimiter = ','  # ou '\t' para tabulação
                data = [line.strip().split(delimiter) for line in content]
                df = pd.DataFrame(data[1:], columns=data[0])  # Supondo que a primeira linha seja o cabeçalho
                dataframes.append((filename, df))
    return dataframes

# Conversão dos arquivos texto para excel
def save_to_excel(dataframes, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for filename, df in dataframes:
            sheet_name = os.path.splitext(filename)[0]
            df.to_excel(writer, sheet_name=sheet_name, index=False)

# Caminho de input dos arquivos txt
def main():
    input_directory = '/var/input_txt'
    output_file = '/var/output/tabela.xlsx'
    
    dataframes = read_text_files(input_directory)
    save_to_excel(dataframes, output_file)
    print(f'Arquivos de texto foram convertidos no caminho: {output_file}')

if __name__ == "__main__":
    main()

def xlsx_to_csv(xlsx_file, csv_file):
    # Ler o arquivo XLSX
    df = pd.read_excel(xlsx_file, header=None)
    
    # Salvar como arquivo CSV
    df.to_csv(csv_file, index=False, header=False)

# Caminho dos arquivos
xlsx_file = '/var/output/tabela.xlsx'
csv_file = '/var/output/tabela.csv'

# Converter XLSX para CSV
xlsx_to_csv(xlsx_file, csv_file)