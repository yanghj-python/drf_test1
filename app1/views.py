from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from app1.authentications import MyAuth
from app1.throttle import SendMessageRate
from app1.models import User
from utils.response import APIResponse


class TestAPIView(APIView):
    authentication_classes = [MyAuth]

    def get(self, request, *args, **kwargs):
        # user = User.objects.first()
        # # 根据用户获取对应的角色
        # print(user.groups.first())
        # # 根据用户获取用户对应的权限
        # print(user.user_permissions.first().name)

        # 获取角色
        group = Group.objects.first()
        print(group)
        # 通过角色获取对应的权限
        print(group.permissions.first().name)
        # 根据角色获取对应的用户
        print(group.user_set.first().username)

        # 获取权限
        # permission = Permission.objects.filter(pk=9).first()
        # print(permission.name)
        # # 根据权限获取用户
        # print(permission.user_set.first().username)
        # # 根据权限获取角色
        # per = Permission.objects.filter(pk=13).first()
        # print(per.group_set.first().name)

        return APIResponse("OK")


class TestPermissionAPIView(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return APIResponse("登录访问成功")


class UserLoginOrReadOnly(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")


class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")
