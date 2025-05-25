from django.shortcuts import render, redirect

from . forms import  UserRegisterForm,Patient_info_Form
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import joblib
from .models import UserPredictModel,Patient_info

from tensorflow import keras
from PIL import Image, ImageOps
from . import forms


def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("data passed")
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')



def report(request):
    return render(request,'report.html')
    




    
import pyttsx3
    
def Deploy_10(request): 
    print("HI")
    if request.method == "POST":
        form = forms.UserPredictForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance

        result1 = UserPredictModel.objects.latest('id')
        models = keras.models.load_model('APP/keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("media/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['Cyst','Normal','Stone','Tumor']
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        if a == 'Cyst':
            a = 'THE KIDNEY DISEASE TYPE OF CYST AFFECTED'
            engine = pyttsx3.init()
            engine.say(a)
            engine.runAndWait()
            
        elif a == 'Normal':
            a = 'NORMAL'
            engine = pyttsx3.init()
            engine.say(a)
            engine.runAndWait()
            
        elif a == 'Stone':
            a = 'THE KIDNEY DISEASE TYPE OF A STONE AFFECTED'
            engine = pyttsx3.init()
            engine.say(a)
            engine.runAndWait()
            
        elif a == 'Tumor':
            a = 'THE KIDNEY DISEASE TYPE OF A TUMOR AFFECTED'
            engine = pyttsx3.init()
            engine.say(a)
            engine.runAndWait()
            
        else:
            a = 'WRONG INPUT'

        data = UserPredictModel.objects.latest('id')
        data.label = a
        data.save()

        
        return render(request, 'result.html',{'form':form,'obj':obj,'predict':a})
    else:
        form = forms.UserPredictForm()
    return render(request, '10_Deploy.html',{'form':form})

Model1 = joblib.load('APP/KIDNEY1.pkl')  

def Deploy_9(request):
    if request.method == 'POST':
        form = Patient_info_Form(request.POST)
        if form.is_valid():
            # Extract cleaned data from form
            Bp = form.cleaned_data['Bp']
            Sg = form.cleaned_data['Sg']
            Al = form.cleaned_data['Al']
            Su = form.cleaned_data['Su']
            Rbc = form.cleaned_data['Rbc']
            Bu = form.cleaned_data['Bu']
            Sc = form.cleaned_data['Sc']
            Sod = form.cleaned_data['Sod']
            Pot = form.cleaned_data['Pot']
            Hemo = form.cleaned_data['Hemo']
            Wbcc = form.cleaned_data['Wbcc']
            Rbcc = form.cleaned_data['Rbcc']
            Htn = form.cleaned_data['Htn']
            
            # Prepare features for prediction
            features = np.array([[Bp, Sg, Al, Su, Rbc, Bu, Sc, Sod, Pot, Hemo, Wbcc, Rbcc, Htn]])
        
            print(features)   
            # Predict using the loaded model
            prediction = Model1.predict(features)
            prediction = prediction[0]
            print(prediction)   
    
            
            if prediction == 0:
                a="This conditions is No Kidney Disease predict"
            elif prediction == 1:
                a="This conditions is Kidney Disease predict"
    
            
            # Save data to database
            instance = form.save(commit=False)
            instance.Class = a
            instance.save()
            
            # Render output page with prediction result
            return render(request, '5_Teamates.html', {'prediction_text': a})
    else:
        form = Patient_info_Form()
    
    return render(request, '9_Deploy.html', {'form': form})





def res(request):
    
    return render(request,'result.html')








def Logout(request):
    logout(request)
    return redirect('Login_3')






from .models import Patient_info

def patient_list(request):
    patients = Patient_info.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def database(request):
    models = UserPredictModel.objects.all()
    return render(request, 'img_database.html', {'models':models})

def matrix(request):
    return render(request,'matrix.html')