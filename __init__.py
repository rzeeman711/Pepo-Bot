import logging

import config
import basic

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s -> %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

basic.bot.run(config.cfg["discord"]["token"])