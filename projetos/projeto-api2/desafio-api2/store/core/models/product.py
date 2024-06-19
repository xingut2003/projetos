from mongoengine import Document, StringField, FloatField, DateTimeField
from datetime import datetime

class Product(Document):
    name: StringField(required=True, unique=True)
    description: StringField(required=True)
    price: FloatField(required=True)
    created_at: DateTimeField(default=datetime.now)
    updated_at: DateTimeField(default=datetime.now)

    meta = {'collection': 'products'}