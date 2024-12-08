from fastapi import APIRouter, UploadFile, responses
from config.db import DB
from schemas.file import File

router = APIRouter()
conn = DB()


@router.post("/upload")
async def upload_file(file: UploadFile):

    new_file = File(name=file.filename)

    new_file.data.put(file.file, content_type=file.content_type)
    new_file.save()
    return {"filename": new_file.name}


@router.get("/download/{file_name}")
async def download_file(file_name: str):
    try:
        file: File = File.objects(name=file_name).first()

        def stream(file: File):
            chunk_size = 1024 * 64
            while chunk := file.data.read(chunk_size):
                yield chunk

        return responses.StreamingResponse(
            stream(file),
            media_type=file.data.content_type or "application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename="{file.name}"'},
        )

    except Exception as e:
        return responses.JSONResponse(content={"error": str(e)})
