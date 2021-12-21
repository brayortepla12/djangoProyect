from django.shortcuts import render
from serviciosApp.models.modelservicios import misServicios

def serviciosView(request):

    servicios = misServicios.objects.all().order_by('id')
    return render(request,"servicios.html",{'servicios':servicios})

