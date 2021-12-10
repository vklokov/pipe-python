from .entity import Entity


class Deal(Entity):
    GET_ENTITY = '/v1/deals'
    GET_FIELDS = '/v1/dealFields'

    fields = None
