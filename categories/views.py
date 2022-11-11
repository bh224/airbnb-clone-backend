from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Category
from .serializers import CatgegorySerializer

# Create your views here.


@api_view(["GET", "POST"])
def all_categories(request):
    if request.method == "GET":
        all_categoreis = Category.objects.all()
        serializer = CatgegorySerializer(all_categoreis, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CatgegorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            new = CatgegorySerializer(new_category)
            return Response(new.data)
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound
    if request.method == "GET":
        serializer = CatgegorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CatgegorySerializer(
            category,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_catetory = serializer.save()
            return Response(CatgegorySerializer(updated_catetory).data)
        else:
            return Response(serializer.erros)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)