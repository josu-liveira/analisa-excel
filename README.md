# Analisador de Dados

Este é um programa com interface gráfica em Python que permite importar, analisar e exportar dados de arquivos Excel.

## Funcionalidades
- Importar arquivos Excel individuais ou uma pasta inteira contendo arquivos Excel.
- Analisar os arquivos importados e combinar os dados em uma única planilha.
- Exportar o resultado da análise para um arquivo Excel de forma instantânea.

## Requisitos
- [X] Python versão 3.x
- [X] Bibliotecas pandas e openpyxl


## Instalação
1. Certifique-se de ter o Python 3.x instalado em seu sistema.
   
2. Instale as bibliotecas necessárias executando o seguintes comandos no terminal ou prompt de comando:

```python
pip install pandas
```
```python
pip install openpyxl
```


## Como Usar



1. Execute o script *`abrir.cmd`.

![image](https://github.com/josu-liveira/analisa-excel/assets/167824520/02d9b08c-13e9-48a4-8fe5-153211c52add)


2. Use os botões para importar arquivos individuais ou em uma pasta.


![image](https://github.com/josu-liveira/analisa-excel/assets/167824520/4c58533f-14c9-442d-b11b-889a21e987e9)


3. Clique em "Analisar arquivos" para iniciar o proecsso de análise dos dados importados.
4. Selecione um diretório de destino e clique em "Exportar análise" para salvar o resultado da análise.

DISCLAIMER: Altere o caminho do ```analisador.py``` na estrutura do arquivo ```abrir.cmd``` para evitar erros.

## Estrutura do Código
- `main.py`: Contém o código principal da interface gráfica e lógica de negócios.
- `pip.cmd`: Modifica parâmetros especiais na pasta /AppData/Roaming/pip/pip.ini de modo que o pip não exiba erros quando fizer download dos módulos.
- `abrir.cmd`: Script padrão de inicialização do código em Python
- `comandos.txt`: Se você estiver com preguiça de copiar os códigos do GitHub :)

## Contribuição
Se você encontrar bugs, tiver sugestões de melhorias ou quiser contribuir de outras formas, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
