import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
    raise RuntimeError("MONGODB_URI não encontrada no ambiente")

# Usa exclusivamente a database já existente configurada no ambiente.
# Este módulo não cria databases ou collections por conta própria.
client = MongoClient(
    uri,
    tls=True,
    serverSelectionTimeoutMS=10000,
    connectTimeoutMS=10000,
)

db = client[os.getenv("MONGODB_DATABASE")]
