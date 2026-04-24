from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.ocr_service import extract_text_from_image
from app.services.extractor import extract_data

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR
    text = extract_text_from_image(file_path)

    # NLP + Regex
    extracted_data = extract_data(text)

    return {
        "filename": file.filename,
        "raw_text": text,
        "extracted_data": extracted_data
    }