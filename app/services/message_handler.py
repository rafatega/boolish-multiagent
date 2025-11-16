import time
from app.utils.logger import logger

from app.models.receive_message import WebhookMessage


async def process_message(body: dict) -> dict:
    start_time = time.monotonic()

    # Recebe a cria objeto com informações do webhook.
    webhook = WebhookMessage(**body)

    elapsed = time.monotonic() - start_time

    logger.info(
        f"[⏱️ Tempo de execução total, BOT*{webhook.fromMe}*]: {elapsed:.3f} segundos")
    return {"status": "success", "processed_in_seconds": elapsed}
