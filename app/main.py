from fastapi import FastAPI
from pydantic import BaseModel
from app.insights import build_insights
app=FastAPI(title="Power BI Insights Copilot",version="0.1.0")
class Filters(BaseModel): region:str|None=None; product:str|None=None; status:str|None=None
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/insights")
def insights(req:Filters): return build_insights(**req.model_dump())
