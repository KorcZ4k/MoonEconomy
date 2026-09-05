"""Registro central dos módulos econômicos do MoonEconomy.

Todos os módulos usam o MongoDB e as collections já existentes.
Nenhum módulo deve criar uma collection nova sem autorização explícita.
"""

EXTENSOES_ECONOMICAS = [
    "comandos.ECONOMIA.Mora",
    "comandos.ECONOMIA.ADMIN.governos",
    "comandos.ECONOMIA.GLOBAL.banco",
    "comandos.ECONOMIA.GLOBAL.banco_central",
    "comandos.ECONOMIA.GLOBAL.ciclo_automatico",
    "comandos.ECONOMIA.GLOBAL.comandos",
    "comandos.ECONOMIA.GLOBAL.comercio",
    "comandos.ECONOMIA.GLOBAL.comercio_comandos",
    "comandos.ECONOMIA.GLOBAL.comercio_internacional",
    "comandos.ECONOMIA.GLOBAL.credito",
    "comandos.ECONOMIA.GLOBAL.credito_comandos",
    "comandos.ECONOMIA.GLOBAL.crises",
    "comandos.ECONOMIA.MEMBROS.empresas",
    "comandos.ECONOMIA.MEMBROS.eventos_assentamentos",
    "comandos.ECONOMIA.MEMBROS.monstros_assentamentos",
    "comandos.ECONOMIA.MEMBROS.reinos",
]
