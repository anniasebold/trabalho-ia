# Trabalho de Inteligência Artificial
Esse é um README sobre o Trabalho de Inteligência Artificial que tem como objetivo esclarecer a estrutura do projeto e como rodá-lo.

## 📋 Descrição

Esse trabalho tem como objetivo explorar a classficação de textos com diferentes estilos literários, nesse caso poesia, prosa e jornalismo. 
É feita a extração de textos de PDFs, os textos são pré-processados, transformados em vetores utilizando o modelo Bag of Words (BoW).

## 💾 Descrição das Pastas e Arquivos 


### `trab_IA.ipynb`
- **Descrição**: Arquivo Jupyter Notebook que contém todos os códigos Python rodados, explicações do código e sua execução e resultados.

### `text_extraction/`
- **Descrição**: Diretório que armazena o código de pré-processamento dos textos. Aqui foi feito a separação dos textos em PDFs.

### `texts/`
- **Descrição**: Diretório que armazena os textos usados para treinamento e teste (pode ser alterado para os textos de sua preferência).

### `requirements.txt`
- **Descrição**: Arquivo que contém todas as dependências necessárias.



## 📚 Instruções de Uso

Este guia explica como configurar e executar o Jupyter Notebook associado a este projeto. Ele também descreve como utilizá-lo no Google Colab e fornece instruções para visualizar os resultados sem executar os blocos de código.


## 1. Configurando o Kernel

### No VS Code:
1. Certifique-se de que o ambiente virtual `.venv` está ativo.
2. No VS Code, abra o notebook e selecione o kernel correto:
   - Clique no canto superior direito do editor do notebook.
   - Escolha o kernel associado ao ambiente virtual `.venv`.

### No Google Collab:
1. [Link para o Google Colaboratory](https://colab.research.google.com/drive/1A8UXsCPunnOYvXdtGxqDmbJ8TsHRd399?usp=sharing) 


## 2. Executando o Notebook

### Opção 1: Rodar Localmente
1. **Execução**:
   - Execute cada célula separadamente clicando em **Shift + Enter** ou clicando do lado de cada célula ou selecione **Run All** para executar todas de uma vez.

2. **Resultados**:
   - Caso queira apenas visualizar os resultados, **não execute nenhuma célula**. Os resultados já estão exibidos abaixo de cada bloco de código.


### Opção 2: Rodar no Google Colab
1. **Abrindo o Notebook no Colab**:
   - Abra o link do Google Colab

2. **Conectando ao Google Drive**:
   - Execute a célula que contém:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```
   - Siga as instruções para autenticar sua conta do Google.

3. **Caminho para os Arquivos**:
   - Verifique se os caminhos para os textos ou dados no notebook apontam corretamente para os arquivos armazenados no Google Drive.

4. **Execução**:
   - Execute cada célula separadamente clicando no botão de **Play** ao lado de cada bloco.

5. **Resultados**:
   - Caso queira apenas visualizar os resultados, **não execute nenhuma célula**. Os resultados já estão exibidos abaixo de cada bloco de código.


## 3. Observações Finais

- **Resultados Padrão**:
  - Se você não executar nenhuma célula, os resultados pré-computados já estarão exibidos abaixo de cada bloco de código.
  
- **Atenção aos Caminhos**:
  - Certifique-se de corrigir os caminhos dos arquivos de entrada para corresponder ao local onde eles estão armazenados (tanto localmente quanto no Google Drive).

- **Ajuda**:
  - Caso enfrente problemas, consultar o grupo.

