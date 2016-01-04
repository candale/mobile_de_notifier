import logging
import logging.config

import car_scraping.settings as settings
from car_scraping.db.create_tables import create_tables

# Setup logging
logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)

# Make sure tables are created
create_tables()
