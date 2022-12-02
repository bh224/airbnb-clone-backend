from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Category
from .serializers import CatgegorySerializer

# Create your views here.

class Categories(APIView):
    def get(self, request):
        kind = request.query_params.dict()["kind"]
        all_categoreis = Category.objects.filter(kind=kind)
        serializer = CatgegorySerializer(all_categoreis, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CatgegorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            new = CatgegorySerializer(new_category)
            return Response(new.data)
        else:
            return Response(serializer.errors)

class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound
        return category

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CatgegorySerializer(category)
        print(serializer)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
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

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)
        

