import logging
import logging.config

import car_scraping.settings as settings

# Setup logging
logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)
