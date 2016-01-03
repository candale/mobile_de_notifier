import sys
import inspect

import car_scraping.db.models as models


def create_tables():
    model_classes = []

    # Get all classes that inherit from BaseModel class
    for name, obj in inspect.getmembers(sys.modules[models.__name__]):
        if inspect.isclass(obj) and issubclass(obj, models.BaseModel):
            if obj.table_exists() is False:
                model_classes.append(obj)

    # Connect and create database tables
    models.db.connect()
    models.db.create_tables(model_classes)
