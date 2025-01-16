from fastapi import FastAPI
from core.database import Base, engine
from modules.admin.controller import router as admin_router
from modules.pelanggan.controller import router as pelanggan_router
from modules.kendaraan.controller import router as kendaraan_router
from modules.wisata.controller import router as wisata_router
from modules.transaksi.controller import router as transaksi_router
from fastapi.middleware.cors import CORSMiddleware

# Buat tabel database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ayo Lulus Deden!!! Pasti Bisa!!!")

# Menambahkan middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Mengizinkan akses dari semua origin (domain)
    allow_credentials=True,
    allow_methods=["*"],  # Mengizinkan semua metode HTTP (GET, POST, dll)
    allow_headers=["*"],  # Mengizinkan semua header
)

# Tambahkan router dari modul
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(pelanggan_router, prefix="/pelanggan", tags=["Pelanggan"])
app.include_router(kendaraan_router, prefix="/kendaraan", tags=["Kendaraan"])
app.include_router(wisata_router, prefix="/wisata", tags=["Wisata"])
app.include_router(transaksi_router, prefix="/transaksi", tags=["Transaksi"])

