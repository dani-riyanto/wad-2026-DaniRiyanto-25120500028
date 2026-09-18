# wad-2026-DaniRiyanto-25120500028
📌 **PANDUAN TUGAS INDIVIDU: FASTAPI ENDPOINT**

* **T1 | Buku**: `isbn` (13 digit), `tahun_terbit` (1900–2026)

✅ **CHECKLIST DEFINITION OF DONE (DoD):**

1. **Repo Setup:**
* Nama repo: `wad-2026-individu-<NIM>` (Public, dari template).✅
* README.md jelas dan dapat diikuti.✅


2. **Endpoint Specs:**
* `POST /api/<entitas>` -> Status 201 Created + Header `Location`.✅
@app.post("/api/buku", status_code=status.HTTP_201_CREATED, response_model=BukuResponse)
def create_buku(buku: BukuCreate, response: Response):
    global current_id
    buku_dict = buku.model_dump()
    buku_dict["id"] = current_id
    
    db_buku.append(buku_dict)
    response.headers["Location"] = f"/api/buku/{current_id}"
    
    current_id += 1
    return buku_dict
* `GET /api/<entitas>` -> Status 200 OK (dukung `?skip`, `?limit`, `?search`).✅
@app.get("/api/buku", status_code=status.HTTP_200_OK, response_model=List[BukuResponse])
def get_all_buku(
    skip: int = 0, 
    limit: int = 10, 
    search: Optional[str] = Query(None)
):
    hasil = db_buku
    if search:
        hasil = [b for b in hasil if search.lower() in b["judul"].lower()]
    return hasil[skip : skip + limit]
* `GET /api/<entitas>/{id}` -> Status 404 jika ID tidak ada.✅
@app.get("/api/buku/{id}", status_code=status.HTTP_200_OK, response_model=BukuResponse)
def get_buku_by_id(id: int):
    for buku in db_buku:
        if buku["id"] == id:
            return buku
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Buku tidak ditemukan")

3. **Data & Validation:**
* Input invalid -> Status 422 Unprocessable Entity.✅
* Skema Input != Skema Output (`id` dibuat oleh server).✅
JSON
{
  "judul": "Buku Pemrograman",
  "isbn": "123",
  "tahun_terbit": 1800
}
{
  "detail": [
    {
      "type": "json_invalid",
      "loc": [
        "body",
        0
      ],
      "msg": "JSON decode error",
      "input": {},
      "ctx": {
        "error": "Expecting value"
      }
    }
  ]
}


4. **Workflow & Verification:**
* Dikerjakan di branch `feature/endpoint-individu`, PR ke `main`, lalu merge sendiri.✅
* Pengujian `python verify.py --individu` berstatus hijau (PASS).✅

