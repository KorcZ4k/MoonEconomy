import asyncio
import datetime
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from moon_economy.extensions import EXTENSOES_ECONOMICAS

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(
    command_prefix=os.getenv("COMMAND_PREFIX", "!"),
    intents=intents,
    case_insensitive=True,
)


@bot.event
async def on_ready():
    fuso_horario = datetime.timezone(datetime.timedelta(hours=-3))
    agora = datetime.datetime.now(fuso_horario)
    print(f"MoonEconomy conectado como {bot.user} em {agora.isoformat()}")
    print(f"[MoonEconomy] {len(bot.cogs)} cogs carregados.")


async def carregar_extensoes():
    extensoes = list(dict.fromkeys(EXTENSOES_ECONOMICAS))

    for extensao in extensoes:
        try:
            await bot.load_extension(extensao)
            print(f"[EXTENSAO][OK] {extensao}")
        except ModuleNotFoundError as erro:
            print(f"[EXTENSAO][ERRO] Modulo ausente: {extensao}: {erro}")
            raise
        except commands.ExtensionAlreadyLoaded:
            continue
        except Exception as erro:
            print(f"[EXTENSAO][ERRO] {extensao}: {type(erro).__name__}: {erro}")
            raise


async def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN nao encontrada. Configure o .env antes de iniciar.")

    async with bot:
        await carregar_extensoes()
        await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
