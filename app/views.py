from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    brand_list = VehicleBrand.objects.all()
    return render(request, "index.html", {'brand_list': brand_list})


def all_json_models(request, brand):
    current_brand = VehicleBrand.objects.get(pk=brand)
    models = VehicleModel.objects.all().filter(brand=current_brand)
    json_models = serializers.serialize("json", models)
    return HttpResponse(json_models, mimetype="application/javascript")









    dsdfsdfdsdssdffffffffffsdddsdsfdswfdsfsdfsdf

