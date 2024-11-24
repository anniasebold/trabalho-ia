Conversor de Arquivos de Texto para PDF

Este script Python converte arquivos de texto em PDFs separados com base em cabeçalhos específicos. 
Ele é útil para converter textos poéticos, em prosa, ou jornalísticos que estejam formatados de maneira apropriada em arquivos PDF.

Funcionalidades:
 - Conversão de arquivos de texto em PDFs: Converte um arquivo de texto em múltiplos PDFs, separados por cabeçalhos específicos.
 - Suporte a múltiplos tipos de texto: Pode lidar com três tipos de texto: poético, em prosa, e jornalístico.
 - Criação automática de PDFs nomeados sequencialmente: Cada seção separada é salva como um PDF com nomes sequenciais (ex. 1.pdf, 2.pdf, etc.).


Estrutura do Arquivo de Texto de Entrada

Para que o script funcione corretamente, o arquivo de texto de entrada deve conter cabeçalhos específicos que dividem o texto em seções. 
Esses cabeçalhos devem seguir o formato abaixo:

 - Poetry: Cabeçalhos POETRY 1 até POETRY 100.
 - Prose: Cabeçalhos PROSE 1 até PROSE 100.
 - Journalistic: Cabeçalhos JOURNAL 1 até JOURNAL 100.

Esses cabeçalhos serão usados como delimitadores para separar o conteúdo em seções distintas.

Exemplo de arquivo .txt válido:
    PROSE 1
    Esta é a primeira seção de texto em prosa.

    PROSE 2
    Esta é a segunda seção de texto em prosa.

    PROSE 3
    Esta é a terceira seção de texto em prosa.


Como Usar

python txt_to_pdf.py <nome_do_arquivo_de_entrada.txt> <tipo_de_texto> -> {"poetry", "prose", "journalistic"}


Observações
 - Fonte DejaVuSans.ttf: Certifique-se de ter o arquivo DejaVuSans.ttf no mesmo diretório do script para que a fonte seja carregada corretamente.