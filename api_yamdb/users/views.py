from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from users.serializers import SignUpSerializer, TokenSerializer, UserSerializer
from users.services import send_code
from api.permissions import IsAdmin, IsSuperUser, PermissionClassMixin


@api_view(['POST'])
@permission_classes([AllowAny])
def get_confirmation_code(request):
    username = request.data.get('username')
    email = request.data.get('email')
    is_registered = User.objects.filter(username=username, email=email)
    if is_registered.exists():
        user = get_object_or_404(User, username=username, email=email)
        send_code(user)
        return Response(
            {'message': 'Пользователь с таким именем/email уже существует'},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            return Response(
                {'message': 'Пользователь с таким именем/mail уже существует'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.create_user(username=username, email=email)
        send_code(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_jwt_token(request):
    username = request.data.get('username')
    serializer = TokenSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(
        user,
        serializer.validated_data['confirmation_code']
    ):
        refresh = RefreshToken.for_user(user)
        return Response(
            {'access': str(refresh.access_token)},
            status=status.HTTP_200_OK
        )
    return Response(
        {'message': 'Неверный код подтверждения'},
        status=status.HTTP_400_BAD_REQUEST
    )


class UserViewSet(PermissionClassMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
        (IsAdmin | IsSuperUser)
    ]
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)

    @action(
        detail=False,
        methods=['get', 'patch'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(role=user.role, partial=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
