from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json


def index(request):
    return HttpResponse("Hello, world. SIM running")


def createLicence(request):
    if request.method == "POST":
        body = json.loads(request.body.decode('UTF-8'))
        new = DrivingLicence(document=body["document"], documentTypeId=DocumentType.objects.get(pk=body["documentTypeId"]), runt_registry=body["documentTypeId"], exam=body["exam"])
        try:
            new.save()
            return JsonResponse({"licenseID": new.id})
        except Exception:
            return JsonResponse({"error": new.check})

