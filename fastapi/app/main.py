from fastapi import FastAPI
from app.core.database import Base, engine
from app.modules.admin.controller import router as admin_router
from app.modules.pelanggan.controller import router as pelanggan_router
from app.modules.kendaraan.controller import router as kendaraan_router
from app.modules.wisata.controller import router as wisata_router
from app.modules.transaksi.controller import router as transaksi_router

# Buat tabel database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ayo Lulus Deden!!! Pasti Bisa!!!")

# Tambahkan router dari modul
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(pelanggan_router, prefix="/admin", tags=["Pelanggan"])
app.include_router(kendaraan_router, prefix="/admin", tags=["Kendaraan"])
app.include_router(wisata_router, prefix="/admin", tags=["Wisata"])
app.include_router(transaksi_router, prefix="/admin", tags=["Transaksi"])

