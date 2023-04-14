import re
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, response, status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
    IsAuthenticated,
    IsAdminUser,
)

from app.opportunities.models import Opportunity, OpportunityRegister, Department
from .serializers import (
    OpportunitySerializer,
    OpportunityRegisterSerializer,
    DepartmentSerializer,
)


class UserWriteOpportunityPermission(BasePermission):
    """
    Permits only Opportunity authors to edit its specs
    """

    message = "Editing an opportunity is restricted to the creator only"

    def has_object_permission(
            self, request, view, obj
    ) -> bool:  # checks if current user posted the opportunity or the request method is applied
        return request.method in SAFE_METHODS or request.user == obj.posted_by


class OpportunityViewSet(viewsets.ModelViewSet):
    serializer_class = OpportunitySerializer
    # permission_classes =[IsAuthenticatedOrReadOnly]  # TODO: Uncomment me in production
    # TODO: Uncomment me in production
    # permission_classes = (
    #     IsAuthenticated,
    #     IsAdminUser,
    # )

    def get_queryset(self, **kwargs):
        query_set = Opportunity.objects.all()
        #  search and filter opportunities
        self.search_fields = [
            "title",
            "description",
            "posted_on",
            "application_deadline",
        ]  # based on these fields
        self.filter_backends = (filters.SearchFilter,)
        return query_set

    # def get_object(self, queryset=None, **kwargs):
    #     # self.permission_classes =[UserWriteOpportunityPermission]  # TODO: Uncomment me in production
    #     return get_object_or_404(Opportunity, id=self.kwargs.get("pk"))

    # overide create and update to check for possible html tags or entities injected
    def create(self, request, *args, **kwargs):
        try:
            form_data: dict = dict(request.data)
            for key in form_data:
                if not key == "csrfmiddlewaretoken":
                    self.strip_html("".join(form_data.get(key)), sub=False)
            return super().create(request, *args, **kwargs)
        except ValueError as e:
            return response.Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            form_data = dict(request.data)
            for key in form_data:
                if not key == "csrfmiddlewaretoken":
                    self.strip_html("".join(form_data.get(key)), sub=False)
            return super().update(request, *args, **kwargs)
        except ValueError as e:
            return response.Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)

    def strip_html(self, text: str, sub=True) -> str:
        """
        checks for html tags and either strips them or raises a value error depending on the sub param value

        :param text {str} - the string data to be searched against
        :param sub? {bool} - an optional flag that decides whether the tags are stripped or not
        :returns {str | ValueError}
        """

        if sub:
            return re.sub(
                r"%3C.*?%3E", "", re.sub(r"<.*?>", "", text)
            )  # strip tags off
        if re.search(r"%3C.*?%3E", text) or re.search(r"<.*?>", text):
            raise ValueError(
                "HTML tags and entities are not allowed"
            )  # raise value error if tags are found
        return text


class OpportunityRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = OpportunityRegisterSerializer
    queryset = OpportunityRegister.objects.all()
    # permission_classes =[IsAuthenticatedOrReadOnly]  # TODO: Uncomment me in production
    # TODO: Uncomment me in production
    # permission_classes = (
    #     IsAuthenticated,
    #     IsAdminUser,
    # )

    def get_queryset(self, **kwargs):
        query_set = OpportunityRegister.objects.all()
        #  search and filter opportunities
        self.search_fields = ["user", "Opportunity"]  # based on these fields
        self.filter_backends = (filters.SearchFilter,)
        return query_set

    def get_object(self, queryset=None, **kwargs):
        # self.permission_classes =[UserWriteOpportunityPermission]  # TODO: Uncomment me in production
        return get_object_or_404(OpportunityRegister, id=self.kwargs.get("pk"))

    # overide create and update to check for possible html tags or entities injected
    # def create(self, request, *args, **kwargs):
    #     try:
    #         form_data: dict = dict(request.data)
    #         for key in form_data:
    #             if not key == "csrfmiddlewaretoken":
    #                 self.strip_html("".join(form_data.get(key)), sub=False)
    #         return super().create(request, *args, **kwargs)
    #     except ValueError as e:
    #         return response.Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            form_data = dict(request.data)
            for key in form_data:
                if not key == "csrfmiddlewaretoken":
                    self.strip_html("".join(form_data.get(key)), sub=False)
            return super().update(request, *args, **kwargs)
        except ValueError as e:
            return response.Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)

    def strip_html(self, text: str, sub=True) -> str:
        """
        checks for html tags and either strips them or raises a value error depending on the sub param value

        :param text {str} - the string data to be searched against
        :param sub? {bool} - an optional flag that decides whether the tags are stripped or not
        :returns {str | ValueError}
        """

        if sub:
            return re.sub(
                r"%3C.*?%3E", "", re.sub(r"<.*?>", "", text)
            )  # strip tags off
        if re.search(r"%3C.*?%3E", text) or re.search(r"<.*?>", text):
            raise ValueError(
                "HTML tags and entities are not allowed"
            )  # raise value error if tags are found
        return text


class OpportunityDetail(RetrieveUpdateDestroyAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    # permission_classes = [UserWriteOpportunityPermission] #TODO: Uncomment me in production


class DepartmentList(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # TODO: Uncomment me in production
    # permission_classes = (
    #     IsAuthenticated,
    #     IsAdminUser,
    # )

# class DepartmentDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
#     permission_classes = (
#         IsAuthenticated,
#         IsAdminUser,
#     )
