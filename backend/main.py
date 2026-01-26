from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Frontend (Vite) uchun CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend ishlayapti"}

@app.post("/scan")
def scan_site(url: str):
    report = {
        "url": url,
        "issues": []
    }

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        # HTTPS tekshiruv
        if not url.startswith("https://"):
            report["issues"].append({
                "level": "high",
                "title": "HTTPS yo‘q",
                "description": "Ma'lumotlar shifrlanmagan holda uzatilmoqda"
            })

        # CSP header
        if "Content-Security-Policy" not in headers:
            report["issues"].append({
                "level": "medium",
                "title": "CSP yo‘q",
                "description": "XSS hujumlarga ochiqlik bo‘lishi mumkin"
            })

        # Clickjacking himoyasi
        if "X-Frame-Options" not in headers:
            report["issues"].append({
                "level": "medium",
                "title": "X-Frame-Options yo‘q",
                "description": "Sayt iframe ichida ochilishi mumkin"
            })

        report["server"] = headers.get("Server", "Noma'lum")

        return report

    except Exception as e:
        return {
            "error": "Saytga ulanib bo‘lmadi",
            "details": str(e)
        }
