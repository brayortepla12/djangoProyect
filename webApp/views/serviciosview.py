from django.shortcuts import render
from serviciosApp import models as modelsServicios

def serviciosView(request):

    servicios = modelsServicios.misServicios.objects.all().order_by('id')
    return render(request,"servicios.html",{'servicios':servicios})

