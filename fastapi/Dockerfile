# Gunakan base image Python
FROM python:3.10-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Copy seluruh aplikasi ke container
COPY ./app /app
COPY ./requirements.txt /app

# Install dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Ekspos port aplikasi (untuk komunikasi internal dengan Nginx)
EXPOSE 8000

# Jalankan aplikasi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
