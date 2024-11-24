import re
import argparse
from argparse import RawTextHelpFormatter
from fpdf import FPDF


def identify_text_sections(content, text_type):
    """
    Identifica e separa as seções do texto com base no tipo especificado.

    :param content: Conteúdo do texto completo.
    :param text_type: Tipo de texto (poetry, prose, journalistic).
    :return: Lista de textos separados por seções.
    """
    patterns = {
        "poetry": r"POETRY 100|POETRY [1-9]?[0-9]",
        "prose": r"PROSE 100|PROSE [1-9]?[0-9]",
        "journalistic": r"JOURNAL 100|JOURNAL [1-9]?[0-9]",
    }

    if text_type not in patterns:
        raise ValueError(f"Tipo de texto inválido: {text_type}")

    pattern = patterns[text_type]
    sections = re.split(pattern, content)
    return [section.strip() for section in sections if section.strip()]


def txt_to_pdf(text, filename):
    """
    Converte um texto para PDF.

    :param text: Texto a ser convertido.
    :param filename: Nome do arquivo PDF de saída.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    for line in text.splitlines():
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(filename)


def load_file(filepath):
    """
    Carrega o conteúdo de um arquivo de texto.

    :param filepath: Caminho do arquivo a ser carregado.
    :return: Conteúdo do arquivo como string.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo '{filepath}' não foi encontrado.")
    except Exception as e:
        raise RuntimeError(f"Erro ao ler o arquivo '{filepath}': {e}")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Converte texto em arquivos PDF separados com base em seções específicas.\n\n"
            "Exemplo de uso:\n"
            "  python txt_to_pdf.py input.txt poetry\n"
        ),
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        "input_file", type=str, help="Nome do arquivo de texto de entrada."
    )
    parser.add_argument(
        "text_type",
        type=str,
        choices=["poetry", "prose", "journalistic"],
        help=(
            "Tipo do arquivo de texto de entrada:\n"
            "  'poetry':        Textos poéticos com cabeçalhos 'POETRY 1' até 'POETRY 100'.\n"
            "  'prose':         Textos em prosa com cabeçalhos 'PROSE 1' até 'PROSE 100'.\n"
            "  'journalistic':  Textos jornalísticos com cabeçalhos 'JOURNAL 1' até 'JOURNAL 100'."
        ),
    )
    args = parser.parse_args()

    try:
        # Carrega o conteúdo do arquivo de entrada
        content = load_file(args.input_file)
        
        # Identifica e separa as seções do texto
        separated_texts = identify_text_sections(content, args.text_type)
        
        if not separated_texts:
            print("Nenhuma seção foi encontrada no texto.")
            return
        
        # Criação dos PDFs
        print("Gerando PDFs...")
        for i, text in enumerate(separated_texts, start=1):
            filename = f"section_{i}.pdf"
            txt_to_pdf(text, filename)
            print(f"PDF '{filename}' criado com sucesso.")
        print("Todos os PDFs foram gerados com sucesso!")

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
