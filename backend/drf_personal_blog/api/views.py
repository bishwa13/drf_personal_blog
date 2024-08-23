
import json
from django.forms.models import model_to_dict # To automate django view linking it with django models
# from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"]) # DRF API VIEW
def api_home (request, *args, ** kwargs):

  data = request.data

  instance = Product.objects.all().order_by("?").first()
  data ={}
  if instance:
    #data = model_to_dict(instances, fields=['id','title','price'])
    data = ProductSerializer(instance).data
  return Response(data)



