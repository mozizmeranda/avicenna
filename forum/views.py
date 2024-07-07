from rest_framework import viewsets, generics
from .serializer import DiseasePostSerializer, CommentsSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import DiseasePost, Comment
from rest_framework.exceptions import ValidationError
import jwt
# Create your views here.


class DiseasePostView(viewsets.ModelViewSet):
    queryset = DiseasePost.objects.all()
    serializer_class = DiseasePostSerializer

    def post(self, request):
        # token = request.headers.get('jwt')
        # payload = jwt.decode(token, 'secret', options={"verify_signature": False})
        # user_id = payload['id']
        serializer = DiseasePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DiseasePostEditView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = DiseasePostSerializer

    def get_queryset(self):
        post = DiseasePost.objects.filter(pk=self.kwargs.get('pk'))
        return post

    def patch(self, request, *args, **kwargs):
        payload = jwt.decode(request.headers.get('jwt'), 'secret', options={"verify_signature": False})
        post = DiseasePost.objects.filter(pk=self.kwargs['pk'], poster=payload['id'])

        if not payload:
            raise ValidationError("Where is the TOKEN???")

        if not post.exists():
            raise ValidationError({"Error": "This isn't your post"})

        return self.partial_update(request, *args, **kwargs)


class CommentsView(generics.ListCreateAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

    def get_queryset(self):
        post = DiseasePost.objects.filter(pk=self.kwargs.get("pk"))
        return post

    # def post(self, request, *args, **kwargs):
    #     token = request.headers.get("jwt")
    #     user_id = jwt.decode(token, 'secret', options={"verify_signature": False})
    #     user = User.objects.filter(id=user_id)
    #
    #     if not user.exists():
    #         raise ValidationError("User should be registered !!")
    #
    #     post = DiseasePost.objects.filter(pk=self.kwargs.get("pk"))
    #     serializer = CommentsSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data)

    # def post(self, serializer, *args, **kwargs):
    #     token = self.request.headers.get("jwt")
    #     user_id = jwt.decode(token, 'secret', options={"verify_signature": False})
    #     user = User.objects.filter(id=user_id['id'])
    #
    #     if not user.exists():
    #         raise ValidationError("User should be registered !!")
    #     obj = User()
    #     # obj.save(commentator=user_id, post=self.kwargs.get('pk'), **kwargs)
    #     serializer.save(commentator=user_id, post=self.kwargs.get('pk'), **kwargs)
    #     return Response({"message": "success"})
