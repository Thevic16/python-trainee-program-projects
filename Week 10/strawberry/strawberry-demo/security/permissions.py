import typing
# from myauth import authenticate_header, authenticate_query_param

from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry.permission import BasePermission
from strawberry.types import Info


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request: typing.Union[Request, WebSocket] = info.context["request"]

        '''
        if "Authorization" in request.headers:
            return authenticate_header(request)

        if "auth" in request.query_params:
            return authenticate_query_params(request)
        '''

        return False
