from fastapi import FastAPI

app = FastAPI(title="Historical Due Diligence Automation")

@app.get("/health")
def health():
    return {"ok": True}
