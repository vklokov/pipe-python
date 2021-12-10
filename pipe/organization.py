from .entity import Entity


class Organization(Entity):
    GET_ENTITY = '/v1/organizations'
    GET_FIELDS = '/v1/organizationFields'

    fields = None
