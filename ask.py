import os
import sys
import chromadb
from dotenv import load_dotenv
from openai import OpenAI

# Ortam değişkenlerini yükle
load_dotenv()

# OpenAI istemcisi
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ChromaDB (kalıcı) başlat
client = chromadb.PersistentClient(path="chromab_db")
collection = client.get_or_create_collection(name="uretim_analizleri")

def get_embedding(text: str) -> list:
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def ask_question(soru):
    """Soru sor ve cevap al"""
    try:
        # En alakalı belgeyi sorgula (embedding ile)
        query_emb = get_embedding(soru)
        sonuc = collection.query(
            query_embeddings=[query_emb],
            n_results=2  # 🔹 birden fazla sonuç getirelim (opsiyonel)
        )
        
        # Belge içeriğini al
        docs = sonuc.get("documents", [])
        metas = sonuc.get("metadatas", [])
        ids = sonuc.get("ids", [])
        
        if not docs or not docs[0]:
            return "Uyarı: İlgili belge bulunamadı. Lütfen farklı bir soru deneyin."
        
        # İlk eşleşme
        icerik = docs[0][0]
        meta = metas[0][0] if metas and metas[0] else {}
        doc_id = ids[0][0] if ids and ids[0] else "bilinmiyor"
        
        # Sistem promptu
        system_prompt = (
            "Sen kumaş üretim süreçleri üzerine uzman bir danışmansın. "
            "Sadece aşağıda sağlanan teknik analizlere göre cevap ver. "
            "Bilgi yetersizse 'Bilmiyorum' de. Kendi uydurduğun bilgileri kullanma."
        )
        
        # LLM çağrısı
        chat = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Soru: {soru}\n\nID: {doc_id}\nMetadata: {meta}\n\nVeri:\n{icerik}"}
            ]
        )
        
        return chat.choices[0].message.content
        
    except Exception as e:
        return f"Sorgu hata verdi: {e}"

# CLI için ana kod
if __name__ == "__main__":
    # Soru al (CLI argümanı varsa onu kullan)
    if len(sys.argv) > 1:
        soru = " ".join(sys.argv[1:])
    else:
        soru = input("Soru: ")
    
    cevap = ask_question(soru)
    print("\n🔹 Cevap:\n", cevap)
