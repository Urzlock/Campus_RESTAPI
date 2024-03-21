# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from CampusService.models import Campus
# from CampusService.serializers import CampusSerializer

# @csrf_exempt
# def campus_list(request):
#     if request.method == 'GET':
#             campus = Campus.objects.all()
#             serializer = CampusSerializer(campus,many=True)
#             return JsonResponse(serializer.data,safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CampusSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    

# @csrf_exempt
# def campus_detail(request, pk):
#     try:
#         campus = Campus.objects.get(pk=pk) 
#     except:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#          serializer = CampusSerializer(campus)
#          return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#          data = JSONParser().parse(request)
#          serializer = CampusSerializer(campus,data=data)
#          if serializer.is_valid():
#               serializer.save()
#               return JsonResponse(serializer.data)
#          return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#          campus.delete()
#          return HttpResponse(status=204)

from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import CampusSerializer
from .models import Campus
from rest_framework.permissions import IsAuthenticated

class CampusView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serialzer_class =  CampusSerializer
    queryset = Campus.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active=False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)