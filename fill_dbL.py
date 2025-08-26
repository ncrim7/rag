import os
import json
from dotenv import load_dotenv
import chromadb
from tqdm import tqdm
from openai import OpenAI

# Ortam değişkenlerini yükle
load_dotenv()

# ChromaDB (kalıcı) başlat
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="uretim_analizleri")

# OpenAI Embedding istemcisi
openai_api_key = os.getenv("OPENAI_API_KEY")
embedding_client = OpenAI(api_key=openai_api_key)

def get_embedding(text: str) -> list:
    response = embedding_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

with open("data/case_cards.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(tqdm(f)):
        line = line.strip()
        if not line:
            continue
        
        item = json.loads(line)

        prompt = item.get("prompt", "")
        completion = item.get("completion", {})
        
        # Tamamlayıcı metni birleştir
        full_text = f"{prompt}\n\n"
        full_text += f"Özet: {completion.get('summary', '')}\n"
        full_text += f"Neden Analizi: {completion.get('root_cause_analysis', '')}\n"
        full_text += f"Anında Aksiyonlar: {', '.join(completion.get('immediate_actions', []))}\n"
        full_text += f"Uzun Vadeli Aksiyonlar: {', '.join(completion.get('long_term_actions', []))}\n"
        full_text += f"Beklenen Sonuç: {completion.get('expected_outcome', '')}"

        metadata = item.get("metadata", {})
        sanitized_metadata = {}
        for key, value in metadata.items():
            if isinstance(value, list):
                sanitized_metadata[key] = ", ".join(map(str, value))
            elif isinstance(value, (str, int, float, bool)) or value is None:
                sanitized_metadata[key] = value
            else:
                sanitized_metadata[key] = str(value)

        collection.add(
            documents=[full_text],
            embeddings=[get_embedding(full_text)],
            metadatas=[sanitized_metadata],
            ids=[item.get("id", f"item_{i}")]
        )


print("Veritabanı başarıyla oluşturuldu.")
