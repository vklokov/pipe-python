import requests


class PipedriveResponseError(Exception):
    pass


class Client:
    @classmethod
    def get(klass, route, params: dict = None) -> dict:
        url = klass.build_url(route, params)
        resp = requests.get(url)
        source = resp.json()

        if (source.get('success') == False):
            raise PipedriveResponseError(source.get('error'))

        return source.get('data')

    @staticmethod
    def build_url(route: str, params: dict = None) -> str:
        from pipe import api_base, api_key

        return f"{api_base}{route}?api_token={api_key}{Client.params_to_query(params)}"

    @staticmethod
    def params_to_query(params: dict = None) -> str:
        if (not params):
            return ""

        query = ""

        for key in params:
            query += f"&{key}={params.get(key)}"

        return query
