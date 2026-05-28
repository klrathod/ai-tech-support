from fastapi import APIRouter, File, UploadFile

from backend.api.controllers.upload_controller import upload_controller

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    return await upload_controller.upload_document(
        filename=file.filename,
        content=content.decode(),
    )
