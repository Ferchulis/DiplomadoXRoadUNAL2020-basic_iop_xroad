from django.db import models


class DocumentType(models.Model):
    name = models.TextField(max_length=255)
    code = models.TextField(max_length=255)


class DrivingLicence(models.Model):
    document = models.TextField()
    documentTypeId = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    runt_registry = models.TextField()
    exam = models.BooleanField()
