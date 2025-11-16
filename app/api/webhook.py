from fastapi import APIRouter, Request
from app.services.message_handler import process_message
from app.utils.logger import logger

router = APIRouter()


logger.info("🚀 Router Inciado 🚀 ")


@router.post("/webhook")
async def receive_message(request: Request):
    try:
        logger.info("🚨 Webhook chegou! Tentando ler body...")
        body = await request.json()
        logger.info(f"[📬 WEBHOOK RECEBIDO] {body}")
        response = await process_message(body)
        logger.info("✅ Webhook processado com sucesso")
        return response

    except Exception as e:
        logger.error(f"❌ Erro no webhook: {e}")
        return {"status": "error", "message": str(e)}


@router.get("/webhook")
def verify_webhook():
    logger.info("🔎 Verificação GET no /webhook")
    return {"status": "online"}


@router.get("/ping")
def ping():
    return {"pong": True}
