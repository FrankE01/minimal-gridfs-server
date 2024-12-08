from uuid import uuid4
from mongoengine import Document, FileField, StringField


class File(Document):
    name = StringField(default=uuid4)
    data = FileField()
    meta = {"collection": "files"}
