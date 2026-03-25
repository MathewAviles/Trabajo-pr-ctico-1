from fastapi import FastAPI, HTTPException, Query
from app.models import DamageReport, DamageUpdate
from app.database import damage_reports

app = FastAPI(title="API Reporte de Daños Técnicos", version="1.0.0")

@app.get("/")
def root():
    return {
        "message": "Bienvenido al API de Reporte de Daños Técnicos",
        "status": "ok"
    }

@app.get("/health")
def health():
    return {
        "service": "running"
    }

@app.get("/damages")
def get_damages(estado: str | None = Query(default=None)):
    if estado is None:
        return {
            "total": len(damage_reports),
            "data": damage_reports
        }

    filtrados = [r for r in damage_reports if r["estado"].lower() == estado.lower()]

    return {
        "total": len(filtrados),
        "data": filtrados
    }

@app.get("/damages/{damage_id}")
def get_damage(damage_id: int):
    if damage_id < 0 or damage_id >= len(damage_reports):
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return damage_reports[damage_id]

@app.post("/damages")
def create_damage(report: DamageReport):
    new_report = report.model_dump()
    new_report["id"] = len(damage_reports)
    damage_reports.append(new_report)
    return {
        "message": "Reporte creado correctamente",
        "data": new_report
    }

@app.put("/damages/{damage_id}")
def update_damage(damage_id: int, update: DamageUpdate):
    if damage_id < 0 or damage_id >= len(damage_reports):
        raise HTTPException(status_code=404, detail="Reporte no encontrado")

    report = damage_reports[damage_id]

    if update.estado is not None:
        report["estado"] = update.estado

    if update.tecnico_asignado is not None:
        report["tecnico_asignado"] = update.tecnico_asignado

    if update.descripcion is not None:
        report["descripcion"] = update.descripcion

    return {
        "message": "Reporte actualizado correctamente",
        "data": report
    }