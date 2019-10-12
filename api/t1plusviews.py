from django.shortcuts import render
from django.http import JsonResponse 
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.db.utils import IntegrityError 
import time 
import json
import binascii

# Create your views here.
def index(request):
    return render(request,"index.html")   
