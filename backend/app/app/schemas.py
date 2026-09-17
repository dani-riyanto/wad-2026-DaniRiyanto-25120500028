from pydantic import BaseModel, Field

# 1. Skema Input (dikirim oleh client)
class BukuCreate(BaseModel):
    judul: str
    isbn: str = Field(..., min_length=13, max_length=13, description="Harus 13 digit")
    tahun_terbit: int = Field(..., ge=1900, le=2026, description="Tahun 1900-2026")

# 2. Skema Output (dikembalikan oleh server)
class BukuResponse(BukuCreate):
    id: int