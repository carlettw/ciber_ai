from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(title="Cyber Security MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok"}

# 🔐 REAL YENGIL SECURITY TEST
@app.post("/api/light-scan")
def light_scan(data: dict):
    url = data.get("url")

    if not url:
        return {"success": False, "message": "URL kiritilmadi"}

    results = {
        "url": url,
        "https": False,
        "missing_headers": [],
        "risk_level": "low"
    }

    # 1️⃣ HTTPS tekshirish
    if url.startswith("https://"):
        results["https"] = True
    else:
        results["risk_level"] = "medium"

    # 2️⃣ Security headers tekshirish
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        required_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Strict-Transport-Security",
            "Referrer-Policy"
        ]

        for h in required_headers:
            if h not in headers:
                results["missing_headers"].append(h)

        if len(results["missing_headers"]) > 2:
            results["risk_level"] = "high"

    except Exception as e:
        return {
            "success": False,
            "message": "Saytga ulanishda xato",
            "error": str(e)
        }

    return {
        "success": True,
        "scan_result": results
    }
@app.get("/")
def root():
    return {"message": "Cyber Security MVP Backend ishlayapti"}
