from pydantic import BaseModel, Field
from typing import Optional

class DamageReport(BaseModel):
    cliente: str = Field(..., min_length=3, max_length=100)
    persona_reporta: str = Field(..., min_length=3, max_length=100)
    asunto: str = Field(..., min_length=5, max_length=100)
    descripcion: str = Field(..., min_length=5, max_length=300)
    tecnico_asignado: str = Field(..., min_length=3, max_length=100)
    estado: str = Field(default="pendiente")

class DamageUpdate(BaseModel):
    estado: Optional[str] = None
    tecnico_asignado: Optional[str] = None
    descripcion: Optional[str] = None