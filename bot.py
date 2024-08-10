import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import os
from plugins.config import Config
from pyrogram import Client as Ntbots
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def main():
    logger.info("Starting bot initialization")
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
        logger.info(f"Created download location directory at {Config.DOWNLOAD_LOCATION}")

    plugins = dict(root="plugins")
    ntbots = Ntbots(
        "URL UPLOADER BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins)

    logger.info("Running bot")
    logger.info("🎉 I AM ALIVE 🎉 ")
    ntbots.run()

if __name__ == "__main__":
    logger.info("Bot script started")
    try:
        main()
    except Exception as e:
        logger.error("An error occurred:", exc_info=True)

