from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from app1.models import User



class MyAuth(BaseAuthentication):
    def authenticate(self, request):

        auth = request.META.get('HTTP_AUTHORIZATION', None)
        print(auth)

        if auth is None:
            return None


        auth_list = auth.split()

        if not (len(auth_list) == 2 and auth_list[0].lower() == "auth"):
            raise exceptions.AuthenticationFailed("认证信息有误，认证失败")

        if auth_list[1] != "abc.marry.123":
            raise exceptions.AuthenticationFailed("用户信息校验失败")

        user = User.objects.filter(username="yhj").first()

        if not user:
            raise exceptions.AuthenticationFailed("用户不存在")
        print(user)
        return (user, None)
