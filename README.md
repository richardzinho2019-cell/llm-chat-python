# Terminal Chat — Local AI

Chat de terminal em Python que utiliza um modelo de linguagem GGUF executado localmente com `llama-cpp-python`.

## Requisitos

- Python 3.10 ou superior.
- Git e um compilador C/C++ disponíveis, caso a instalação precise compilar a biblioteca.
- Modelo GGUF compatível.
- Aproximadamente 16 GB de RAM recomendados para o modelo de 3B parâmetros, considerando também o consumo do sistema.

## 1. Baixar o projeto

Entre na pasta do projeto:

```bash
cd terminal-chat
```

## 2. Criar o ambiente virtual

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows — PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 3. Instalar as bibliotecas

Atualize o instalador:

```bash
python -m pip install --upgrade pip
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

**Observação:** a instalação de `llama-cpp-python` pode exigir compilação nativa. Consulte a documentação oficial se ocorrer algum erro de compilação: https://github.com/abetlen/llama-cpp-python

## 4. Baixar o modelo de IA

Acesse o repositório:

https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF

Baixe a versão `Q4_K_M` em formato `.gguf`.

Crie a pasta `models` na raiz do projeto e coloque o arquivo nela com o seguinte nome:

```text
models/Qwen2.5-3B-Instruct-Q4_K_M.gguf
```

Se o arquivo baixado tiver outro nome, renomeie-o para corresponder ao caminho esperado pelo programa.

## 5. Executar o chat

Com o ambiente virtual ativado:

```bash
python main.py
```

Aguarde o carregamento do modelo. Depois, digite suas mensagens no terminal.

## 6. Encerrar o programa

Digite:

```text
/exit
```

Também é possível encerrar com `Ctrl+C`.

## Estrutura do projeto

```text
terminal-chat/
├── main.py
├── requirements.txt
├── README.md
└── models/
    └── Qwen2.5-3B-Instruct-Q4_K_M.gguf
```

## Observações

- O modelo é executado localmente, sem necessidade de API externa.
- O histórico é mantido somente durante a execução do programa.
- O histórico antigo é limitado para controlar o uso do contexto.
- A execução inicial utiliza a CPU.
- A qualidade das respostas depende do modelo, da quantização e das instruções fornecidas.
