from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from app.chapters.models import Chapter, ChapterRegister
from .serializers import ChapterSerializer, ChapterRegisterSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class SearchChapter(generics.ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        """
        This view should return a list of all the chapters
        """

        query = self.kwargs['chapter_name']
        # query = self.request.chapter.get('chapter_name')
        return Chapter.objects.filter(name__contains=query)
    


class ChapterRegisterViewSet(viewsets.ModelViewSet):
    queryset = ChapterRegister.objects.all()
    serializer_class = ChapterRegisterSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)