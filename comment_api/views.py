from rest_framework import generics, status
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentChildSerializer, CommentSerializer


class PostCreateListAPI(generics.ListCreateAPIView):    # API create posts and all view
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommetsAPIListView(generics.ListAPIView):    # API all view comments

    serializer_class = CommentChildSerializer
    queryset = Comment.objects.all()


class AddCommetToPostAPI(generics.ListCreateAPIView):   # API create comment to post

    serializer_class = CommentChildSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(parent=self.kwargs['pk'])
        return queryset

    def create(self, request, *args, **kwargs):

        data = request.data

        data['post_id'] = kwargs['pk']
        data['level'] = 0
        data['child'] = []

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentToCommentAPI(generics.ListCreateAPIView):  # API create comment to comment
    serializer_class = CommentSerializer

    def get_queryset(self):
        parent = self.kwargs['pk']
        return Comment.objects.filter(parent=parent)

    def create(self, request, *args, **kwargs):
        parent = Comment.objects.filter(id=kwargs['pk'])
        data = request.data

        for p in parent:
            data['post_id'] = p.post_id_id
            data['level'] = p.level + 1
        data['child'] = []
        data['parent'] = kwargs['pk']

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)