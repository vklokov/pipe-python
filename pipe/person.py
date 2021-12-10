from .entity import Entity


class Person(Entity):
    GET_ENTITY = '/v1/persons'
    GET_FIELDS = '/v1/personFields'

    fields = None
