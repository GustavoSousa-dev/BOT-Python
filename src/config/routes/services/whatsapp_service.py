import httpx
from config.config import config
from utils.logger import logger

class WhatsAppService:
    def __init__(self):
        self.base_url = config.WHAPI_BASE_URL
        self.token = config.WHAPI_TOKEN
        self.headers = {"Authorization": f"Bearer {self.token}"}

    async def send_message(self, phone: str, message: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/messages/text",
                    json={"to": phone, "body": message},
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Erro ao enviar mensagem: {str(e)}")
                raise

    async def send_media(self, phone: str, media_url: str, media_type: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/messages/{media_type}",
                    json={"to": phone, "media": media_url},
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Erro ao enviar mídia: {str(e)}")
                raise

    async def send_poll(self, phone: str, question: str, options: list):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/messages/poll",
                    json={"to": phone, "question": question, "options": options},
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Erro ao enviar enquete: {str(e)}")
                raise

    async def get_group_contacts(self, group_id: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/groups/{group_id}/participants",
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Erro ao obter contatos do grupo: {str(e)}")
                raise

    async def get_profile_picture(self, phone: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/contacts/{phone}/avatar",
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Erro ao obter foto de perfil: {str(e)}")
                raise