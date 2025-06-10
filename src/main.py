from fastapi import FastAPI
from routes.api import router as api_router
from services.webhook_service import handle_webhook
from utils.logger import logger

app = FastAPI(title="WhatsApp Bot API")

# Incluir rotas da API
app.include_router(api_router, prefix="/api")

# Endpoint para webhook
app.post("/webhook")(handle_webhook)

if __name__ == "__main__":
    import uvicorn
    logger.info("Iniciando servidor FastAPI")
    uvicorn.run(app, host="0.0.0.0", port=8000)