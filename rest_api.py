from fastapi import FastAPI
from yargi_mcp.tools.bedesten import search_bedesten_unified

app = FastAPI(title="Hukuk REST API")

@app.post("/api/tools/search_bedesten_unified")
async def arama_yap(payload: dict):
    # PHP'den gelen arama kelimesini alıyoruz
    aranan_kelime = payload.get("phrase", "")
    mahkemeler = payload.get("court_types", ["yargitay", "danistay", "yerel_hukuk"])
    
    # Yargı MCP'nin içindeki asıl fonksiyonu çalıştırıyoruz
    try:
        sonuc = search_bedesten_unified(
            phrase=aranan_kelime, 
            court_types=mahkemeler
        )
        # PHP'nin beklediği formata çevirip yolluyoruz
        return {"status": "success", "result": sonuc}
    except Exception as e:
        return {"status": "error", "message": str(e)}
