from django.shortcuts import render


import firebase_admin
from firebase_admin import credentials, firestore
import os
from . import models

data = os.path.abspath(os.path.dirname(__file__)) + "/sage-striker-331403-firebase-adminsdk-vc6ox-c0eed9cc43.json"

cred = credentials.Certificate(data)

firebase_admin.initialize_app(cred)
def configure(request):
    if request.user.is_authenticated:
        print(request.user)
    x = "hello"
    number = ""
    user = str(request.user)
    try:
        number = models.Number.objects.get(user=user).number

    except:
        data = {"number": False}
        return render(request, "texter/motivate_form.html", data)
    db = firestore.client()
    doc_ref = db.collection(u'numbers').document(user)
    data = doc_ref.get().to_dict()
    print(data)
    data["number"] = True
    data["number_val"] = number

    return render(request, "texter/motivate_form.html", data)
# Create your views here.

def activate(request):

    newSetting = (request.POST["status"] == "True")
    db = firestore.client()
    print(newSetting)
    number = models.Number.objects.get(user=str(request.user)).number
    user = str(request.user)

    doc_ref = db.collection(u'numbers').document(user)
    doc_ref.set({
        u'phone-number': number,
        u'active': newSetting
    })
    doc_ref = db.collection(u'numbers').document(user)
    data = doc_ref.get().to_dict()

    data["number"] = True
    data["number_val"] = number


    return render(request, "texter/motivate_form.html", data)

def register(request):
    db = firestore.client()

    user = str(request.user)
    number = str(request.POST["number"])
    b = models.Number(user=user, number=number)
    b.save()
    doc_ref = db.collection(u'numbers').document(user)
    doc_ref.set({
        u'phone-number': number,
        u'active': False
    })
    data = doc_ref.get().to_dict()
    data["number"] = True
    data["number_val"] = number
    return render(request, "texter/motivate_form.html", data)

def chat(request):
    return render(request, "texter/chatbot.html")