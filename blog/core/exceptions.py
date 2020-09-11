from fastapi import HTTPException, status


class BadRequestHTTPException(HTTPException):
    def __init__(
        self, status_code=status.HTTP_400_BAD_REQUEST, detail="请求参数有误", headers=None
    ):
        super().__init__(status_code, detail, headers)


class UnauthorizedHTTPException(HTTPException):
    def __init__(
        self, status_code=status.HTTP_401_UNAUTHORIZED, detail="请求需要用户验证", headers=None
    ):
        super().__init__(status_code, detail, headers)


class ForbiddenHTTPException(HTTPException):
    def __init__(
        self, status_code=status.HTTP_403_FORBIDDEN, detail="请求被拒绝", headers=None
    ):
        super().__init__(status_code, detail, headers)


class CoreNotFoundHTTPException(HTTPException):
    def __init__(
        self, status_code=status.HTTP_404_NOT_FOUND, detail="请求资源不存在", headers=None
    ):
        super().__init__(status_code, detail, headers)


class MethodNotAllowedHTTPException(HTTPException):
    def __init__(
        self,
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        detail="请求方法不能被用于请求相应的资源",
        headers=None,
    ):
        super().__init__(status_code, detail, headers)


class CoreNotAcceptableHTTPException(HTTPException):
    def __init__(
        self,
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail="请求返回的数据类型无法满足",
        headers=None,
    ):
        super().__init__(status_code, detail, headers)


class RequestTimeoutHTTPException(HTTPException):
    def __init__(
        self, status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="请求超时", headers=None
    ):
        super().__init__(status_code, detail, headers)


class UnsupportedMediaTypeHTTPException(HTTPException):
    def __init__(
        self,
        status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        detail="不支持该提交文件类型",
        headers=None,
    ):
        super().__init__(status_code, detail, headers)


class UnprocessableEntityHTTPException(HTTPException):
    def __init__(
        self,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail="内容有误，无法相应",
        headers=None,
    ):
        super().__init__(status_code, detail, headers)
