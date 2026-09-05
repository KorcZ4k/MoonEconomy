import os
from dotenv import load_dotenv

load_dotenv()


def obrigatorio(nome: str) -> str:
    valor = os.getenv(nome)
    if not valor:
        raise RuntimeError(f"Variavel obrigatoria ausente: {nome}")
    return valor


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "!")
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")

# Estes processos pertencem ao MoonEconomy e podem ser controlados sem alterar dados.
CICLO_ECONOMICO_ATIVO = os.getenv("CICLO_ECONOMICO_ATIVO", "true").lower() == "true"
EVENTOS_ASSENTAMENTOS_ATIVOS = os.getenv("EVENTOS_ASSENTAMENTOS_ATIVOS", "true").lower() == "true"
