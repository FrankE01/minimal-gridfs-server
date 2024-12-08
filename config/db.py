from mongoengine import connect


class DB:
    def __init__(self):
        connect("gridfs")
