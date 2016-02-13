import logging
import logging.config

import cars_scraper.settings as settings

# Setup logging
logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)
