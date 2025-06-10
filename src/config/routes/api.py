from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.whatsapp_service import WhatsAppService
from utils.logger import logger

router = APIRouter()

class MessageRequest(BaseModel):
    phone: str
    message: str

class MediaRequest(BaseModel):
    phone: str
    media_url: str
    type: str  # image, audio, video, document

class PollRequest(BaseModel):
    phone: str
    question: str
    options: list[str]

@router.get("/qr-code")
async def get_qr_code():
    try:
        whatsapp_service = WhatsAppService()
        response = await whatsapp_service.get_qr_code()
        return response
    except Exception as e:
        logger.error(f"Erro ao obter QR code: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter QR code")

@router.post("/send-message")
async def send_message(request: MessageRequest):
    try:
        whatsapp_service = WhatsAppService()
        response = await whatsapp_service.send_message(request.phone, request.message)
        return response
    except Exception as e:
        logger.error(f"Erro ao enviar mensagem: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao enviar mensagem")

@router.post("/send-media")
async def send_media(request: MediaRequest):
    try:
        whatsapp_service = WhatsAppService()
        response = await whatsapp_service.send_media(request.phone, request.media_url, request.type)
        return response
    except Exception as e:
        logger.error(f"Erro ao enviar mídia: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao enviar mídia")

@router.post("/send-poll")
async def send_poll(request: PollRequest):
    try:
        whatsapp_service = WhatsAppService()
        response = await whatsapp_service.send_poll(request.phone, request.question, request.options)
        return response
    except Exception as e:
        logger.error(f"Erro ao enviar enquete: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao enviar enquete")

@router.get("/group-contacts/{group_id}")
async def get_group_contacts(group_id: str):
    try:
        whatsapp_service = WhatsAppService()
        contacts = await whatsapp_service.get_group_contacts(group_id)
        return contacts
    except Exception as e:
        logger.error(f"Erro ao obter contatos do grupo: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter contatos do grupo")

@router.get("/profile-picture/{phone}")
async def get_profile_picture(phone: str):
    try:
        whatsapp_service = WhatsAppService()
        picture = await whatsapp_service.get_profile_picture(phone)
        return picture
    except Exception as e:
        logger.error(f"Erro ao obter foto de perfil: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter foto de perfil")