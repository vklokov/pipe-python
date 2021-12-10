from .client import Client
from .fields import serialize_fields


class Entity(object):
    @classmethod
    def find(klass, id: int):
        return klass(Client.get(f"{klass.GET_ENTITY}/{id}"))

    def __init__(self, source: dict):
        self.source = source

        if (self.__class__.fields):
            self.fields = self.__class__.fields
        else:
            self.__class__.fields = self.fetch_fields()
            self.fields = self.__class__.fields

        self.assign_attributes()

    def assign_attributes(self):
        from pipe import custom_fields as custom

        try:
            custom_fields = custom.get(self.class_name())
        except:
            custom_fields = {}

        attributes = serialize_fields(
            self.source,
            self.__class__.fields,
            custom_fields
        )
        print(attributes)
        for attr in attributes:
            self.__dict__[attr] = attributes[attr]

    def fetch_fields(self):
        if (self.__class__.fields):
            return self.__class__.fields
        else:
            return Client.get(self.__class__.GET_FIELDS)

    def class_name(self):
        return self.__class__.__name__.lower()
