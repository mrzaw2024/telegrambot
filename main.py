import os, time, requests, logging

TRON_API = "https://apilist.tronscan.org/api/block/latest"
TOKEN    = os.environ["TELEGRAM_TOKEN"]
CHAT_ID  = os.environ["CHAT_ID"]

last_block_hash = ""

logging.basicConfig(level=logging.INFO)

while True:
    try:
        res = requests.get(TRON_API).json()
        block_num = res["number"]
        block_hash = res["hash"]

        if block_hash != last_block_hash:
            msg = f"🔗 New Tron block\n\n• Block #: `{block_num}`\n• Hash   : `{block_hash}`"
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}
            )
            logging.info(f"Posted Block #{block_num}")
            last_block_hash = block_hash

    except Exception as e:
        logging.warning(f"Error: {e}")

    time.sleep(10)  # Check every 10 
