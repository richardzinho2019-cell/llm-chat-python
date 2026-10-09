
import os
import sys
from pathlib import Path

from llama_cpp import Llama

# Configurações do chat
MODEL_PATH = Path("models/Qwen2.5-3B-Instruct-Q4_K_M.gguf")
CONTEXT_SIZE = 4096
MAX_TOKENS = 256
MAX_HISTORY_MESSAGES = 12

SYSTEM_PROMPT = """
Você é um assistente virtual executado localmente.
Responda em português brasileiro, de forma clara e objetiva.
Prefira respostas curtas, normalmente com até 5 frases.
Use listas somente quando forem úteis.
Não repita a pergunta do usuário.
Se precisar de mais informações, faça uma pergunta curta.
Não invente informações quando não souber a resposta.
""".strip()

# Cores ANSI para o terminal
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"


def print_banner():
    """Exibe o cabeçalho do chat."""
    print(CYAN + BOLD)
    print("+--------------------------------------+")
    print("|           TERMINAL CHAT              |")
    print("|       Local AI Assistant             |")
    print("+--------------------------------------+")
    print(RESET)
    print("Comando: /exit para sair.")
    print("Digite uma mensagem para conversar.\n")


def load_model():
    """Carrega o modelo GGUF local."""
    if not MODEL_PATH.is_file():
        print(RED + f"Modelo não encontrado: {MODEL_PATH}" + RESET)
        print("Baixe o modelo e coloque-o na pasta models/.")
        sys.exit(1)

    print(YELLOW + "Carregando modelo de IA..." + RESET)

    try:
        model = Llama(
            model_path=str(MODEL_PATH),
            n_ctx=CONTEXT_SIZE,
            n_gpu_layers=0,
            verbose=False,
        )
        print(GREEN + "Modelo carregado com sucesso.\n" + RESET)
        return model
    except Exception as error:
        print(RED + f"Erro ao carregar modelo: {error}" + RESET)
        sys.exit(1)


def generate_response(model, history):
    """Gera uma resposta usando o histórico da conversa."""
    result = model.create_chat_completion(
        messages=history,
        max_tokens=MAX_TOKENS,
        temperature=0.7,
        top_p=0.9,
        repeat_penalty=1.1,
    )

    return result["choices"][0]["message"]["content"].strip()


def trim_history(history):
    """Mantém apenas as mensagens recentes, além do system prompt."""
    recent_messages = history[1:][-MAX_HISTORY_MESSAGES:]
    history[:] = [history[0], *recent_messages]


def main():
    """Inicializa e executa o chat interativo."""
    os.system("cls" if os.name == "nt" else "clear")
    print_banner()

    model = load_model()

    history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        try:
            user_input = input(GREEN + "Você > " + RESET).strip()

            if not user_input:
                continue

            if user_input.lower() == "/exit":
                print(YELLOW + "\nChat encerrado." + RESET)
                break

            history.append({
                "role": "user",
                "content": user_input,
            })

            print(CYAN + "\nIA > " + RESET, end="", flush=True)

            response = generate_response(model, history)

            print(response + "\n")

            history.append({
                "role": "assistant",
                "content": response,
            })

            trim_history(history)

        except KeyboardInterrupt:
            print(YELLOW + "\n\nChat encerrado." + RESET)
            break

        except EOFError:
            print(YELLOW + "\n\nEntrada encerrada." + RESET)
            break

        except Exception as error:
            print(RED + f"\nErro durante a resposta: {error}\n" + RESET)

            # Remove a mensagem atual se a geração falhar.
            if history and history[-1]["role"] == "user":
                history.pop()


if __name__ == "__main__":
    main()
