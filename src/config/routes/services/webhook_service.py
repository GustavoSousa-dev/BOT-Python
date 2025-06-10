import httpx
from fastapi import Request
from config.config import config
from utils.logger import logger
from models.message import Message

async def handle_webhook(request: Request):
    """Processa payloads do webhook (usado pelo FastAPI)."""
    try:
        payload = await request.json()
        message = Message(**payload)
        logger.info(f"Evento recebido: {message.type} de {message.from_phone}")
        return {"status": "received"}
    except Exception as e:
        logger.error(f"Erro ao processar webhook: {str(e)}")
        return {"status": "error"}

async def notify_webhook(payload: dict):
    """Envia eventos recebidos para o webhook configurado."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(config.WEBHOOK_URL, json=payload)
            response.raise_for_status()
            logger.info(f"Webhook notificado: {payload}")
        except Exception as e:
            logger.error(f"Erro ao notificar webhook: {str(e)}")