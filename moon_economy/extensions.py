"""Registro central dos módulos econômicos do MoonEconomy.

Todos os módulos usam o MongoDB e as collections já existentes.
Nenhum módulo deve criar uma collection nova sem autorização explícita.
"""

from config import CICLO_ECONOMICO_ATIVO, EVENTOS_ASSENTAMENTOS_ATIVOS

EXTENSOES_ECONOMICAS = [
    # Economia individual e mercado
    "comandos.ECONOMIA.Mora",
    "comandos.ECONOMIA.loja",
    "comandos.ECONOMIA.loja_canais",
    "comandos.ECONOMIA.cassino",
    "comandos.ECONOMIA.recompensas",

    # Administração econômica
    "comandos.ECONOMIA.ADMIN.governos",

    # Economia global
    "comandos.ECONOMIA.GLOBAL.banco",
    "comandos.ECONOMIA.GLOBAL.banco_central",
    "comandos.ECONOMIA.GLOBAL.comandos",
    "comandos.ECONOMIA.GLOBAL.comercio",
    "comandos.ECONOMIA.GLOBAL.comercio_comandos",
    "comandos.ECONOMIA.GLOBAL.comercio_internacional",
    "comandos.ECONOMIA.GLOBAL.credito",
    "comandos.ECONOMIA.GLOBAL.credito_comandos",
    "comandos.ECONOMIA.GLOBAL.crises",

    # Economia territorial
    "comandos.ECONOMIA.MEMBROS.empresas",
    "comandos.ECONOMIA.MEMBROS.reinos",
    "comandos.ECONOMIA.MEMBROS.monstros_assentamentos",
]

if CICLO_ECONOMICO_ATIVO:
    EXTENSOES_ECONOMICAS.append("comandos.ECONOMIA.GLOBAL.ciclo_automatico")

if EVENTOS_ASSENTAMENTOS_ATIVOS:
    EXTENSOES_ECONOMICAS.append("comandos.ECONOMIA.MEMBROS.eventos_assentamentos")
