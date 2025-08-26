import os
import sys
import chromadb
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ChromaDB (kalıcı) başlat
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="uretim_analizleri")

# OpenAI istemcisi (hem embedding hem chat için)
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str) -> list:
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Soru al (CLI argümanı varsa onu kullan)
if len(sys.argv) > 1:
    soru = " ".join(sys.argv[1:])
else:
    soru = input("Soru: ")

# En alakalı belgeyi sorgula (embedding ile)
try:
    query_emb = get_embedding(soru)
    sonuc = collection.query(
        query_embeddings=[query_emb],
        n_results=1
    )
except Exception as e:
    print(f"Sorgu hata verdi: {e}")
    exit(1)

# Belge içeriğini güvenli biçimde al
docs = sonuc.get("documents", [])
if not docs or not docs[0]:
    print("Uyarı: İlgili belge bulunamadı. Lütfen farklı bir soru deneyin.")
    exit(0)

icerik = docs[0][0]

# Sistem promptu
system_prompt = (
    "Sen kumaş üretim süreçleri üzerine uzman bir danışmansın. "
    "Sadece aşağıda sağlanan teknik analizlere göre cevap ver. "
    "Bilgi yetersizse 'Bilmiyorum' de. Kendi uydurduğun bilgileri kullanma."
)

# OpenAI'den cevap al (v1 SDK)
chat = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"{soru}\n\nVeri:\n{icerik}"}
    ]
)

print("\nCevap:\n", chat.choices[0].message.content)
