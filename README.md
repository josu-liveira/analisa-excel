# Aplicativo analisador de dados xlsx

Este é um aplicativo com interface gráfica em Python baseada na biblioteca tkinter, que permite importar, analisar e exportar dados de arquivos Excel.

## Funcionalidades
- Importar arquivos Excel individuais ou uma pasta inteira contendo arquivos Excel.
- Analisar os arquivos importados e combinar os dados em uma única planilha.
- Exportar o resultado da análise para um arquivo Excel de forma instantânea.

## ATENÇÃO!!

Esse código é baseado em um DataFrame do pandas. Para conseguir executá-lo, você deve modificar a extração dos dados usando o parâmetro `df.iloc[sua linha, sua coluna]` na função ```extrair_dados```, de modo que o código consiga ler sua planilha de acordo com sua necessidade. Abaixo está um exemplo:

```python
def extrair_dados(arquivo):
    df = pd.read_excel(arquivo)
    data = {
        "Parametro 1": df.iloc[4, 2],
        "Parametro 2": df.iloc[5, 2],
        "Parametro 3": df.iloc[4, 7],
        "Parametro 4": df.iloc[5, 7],
        "Parametro 5": df.iloc[9, 2],
        "Parametro 6": df.iloc[9, 7],
        "Parametro 7": df.iloc[7, 2],
}
return data
```

## Requisitos
- [X] Python versão 3.x
- [X] Bibliotecas pandas e openpyxl


## Instalação
1. Primeiramente instale o interpretador do Python em seu sistema. Você pode obtê-lo em: https://www.python.org/downloads/

2. Execute o script ```pip.cmd```. Ele é responsável por criar parâmetros no arquivo `/AppData/Roaming/pip/pip.ini`, onde o pip é setado para fazer sua busca apenas em repositórios especificados. Isso é útil quando você enfrenta problemas de certificados SSL não encontrados.
   - Para mais detalhes leia o artigo [pip install fails](https://stackoverflow.com/questions/25981703) do Stack Overflow.

3. Agora, execute os comandos em seu ambiente de terminal ou Windows PowerShell:

```python
pip install pandas
```
```python
pip install openpyxl
```

## Como Usar





1. **É NECESSÁRIO alterar o caminho do arquivo** ```analisador.py``` dentro do arquivo ```abrir.cmd``` para executar o script corretamente.


```bash
rem Defina o caminho para o arquivo Python que você deseja executar.
set PYTHON_SCRIPT=C:/Coloque/Aqui/O/Caminho/Para/Seu/Arquivo.py
```

   - Logo após, execute o arquivo `abrir.cmd` para iniciar o script python.

---

2. Use os botões para fazer as análises e exportações.


   ![image](https://github.com/josu-liveira/analisa-excel/assets/167824520/4c58533f-14c9-442d-b11b-889a21e987e9)


## Estrutura do Código
- `main.py`: Contém o código principal do aplicativo.
- `pip.cmd`: Modifica parâmetros especiais no arquivo `/AppData/Roaming/pip/pip.ini` para evitar erros.
- `abrir.cmd`: Script padrão de inicialização do código em Python
- `comandos.txt`: Se você estiver com preguiça de ler o que eu escrevi aqui no GitHub :)

## Contribuição
Se você encontrar bugs, tiver sugestões de melhorias ou quiser contribuir de outras formas, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a [LICENÇA JOSUÉ](LICENSE).
