import matplotlib
matplotlib.use('Agg')
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.conf import settings
from .models import HealthLog
from datetime import datetime


model_path = os.path.join(settings.BASE_DIR, 'health_logging', 'model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'health_logging', 'scaler.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)
with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

def plot_glucose():
    health_logs = HealthLog.objects.all()
    image_path = os.path.join(settings.MEDIA_ROOT, 'glucose_graph.png')
    glucose_levels = [log.glucose for log in health_logs]
    timestamps = [str(log.date_created) for log in health_logs]
    fig, ax = plt.subplots()
    ax.plot(timestamps, glucose_levels, marker='o', color='b', label='Glucose Level')
    ax.set_xlabel('Date')  
    ax.set_ylabel('Glucose Level')
    ax.set_title('User Glucose Levels Over Time')
    ax.legend()
    plt.savefig(image_path)
    plt.close(fig)
    image_url = os.path.join(settings.MEDIA_URL, 'glucose_graph.png')
    return image_url

def plot_insulin():
    health_logs = HealthLog.objects.all()
    image_path = os.path.join(settings.MEDIA_ROOT, 'insulin_graph.png')
    insulin_levels = [log.insulin for log in health_logs]
    timestamps = [str(log.date_created) for log in health_logs]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(timestamps, insulin_levels, marker='o', color='b', label='Insulin Levels')
    ax.set_xlabel('Date')
    ax.set_ylabel('Insulin Level')
    ax.set_title('Insulin Levels Over Time')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close(fig)
    image_url = os.path.join(settings.MEDIA_URL, 'insulin_graph.png')
    return image_url

def plot_bmi():
    health_logs = HealthLog.objects.all()
    image_path = os.path.join(settings.MEDIA_ROOT, 'bmi_graph.png')
    bmi_levels = [log.bmi for log in health_logs]
    timestamps = [str(log.date_created) for log in health_logs]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(timestamps, bmi_levels, marker='x', color='g', label='BMI')
    ax.set_xlabel('Date')
    ax.set_ylabel('BMI')
    ax.set_title('BMI Over Time')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close(fig)
    image_url = os.path.join(settings.MEDIA_URL, 'bmi_graph.png')
    return image_url

def plot_diabetes_prediction():
    health_logs = HealthLog.objects.all()
    image_path = os.path.join(settings.MEDIA_ROOT, 'diabetes_prediction_graph.png')
    diabetes_predictions = [log.diabetes_prediction for log in health_logs]
    timestamps = [str(log.date_created) for log in health_logs]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(timestamps, diabetes_predictions, marker='s', color='r', label='Diabetes Prediction')
    ax.set_xlabel('Date')
    ax.set_ylabel('Prediction')
    ax.set_title('Diabetes Prediction Over Time')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close(fig)
    image_url = os.path.join(settings.MEDIA_URL, 'diabetes_prediction_graph.png')
    return image_url

def plot_blood_pressure():
    health_logs = HealthLog.objects.all()
    image_path = os.path.join(settings.MEDIA_ROOT, 'blood_pressure_graph.png')
    blood_pressure_levels = [log.blood_pressure for log in health_logs]
    timestamps = [str(log.date_created) for log in health_logs]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(timestamps, blood_pressure_levels, marker='^', color='purple', label='Blood Pressure')
    ax.set_xlabel('Date')
    ax.set_ylabel('Blood Pressure')
    ax.set_title('Blood Pressure Over Time')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close(fig)
    image_url = os.path.join(settings.MEDIA_URL, 'blood_pressure_graph.png')
    return image_url

def health(request):
    blood_pressure_plot = plot_blood_pressure()
    bmi_plot = plot_bmi()
    glucose_plot = plot_glucose()
    insuline_plot = plot_insulin()
    health= HealthLog.objects.all().last()
    health_logs = HealthLog.objects.all()
    context = {
        'blood_pressure_plot': blood_pressure_plot,
        'bmi_plot': bmi_plot,
        'health_logs':health_logs,
        'glucose_plot': glucose_plot,
        'insuline_plot': insuline_plot,
        'last_health':health
    }

    return render(request, 'health_logging/health.html', context)

def form(request):
    if request.method == 'POST':
        pregnancies = float(request.POST.get('pregnancies'))
        glucose = float(request.POST.get('glucose'))
        blood_pressure = float(request.POST.get('blood pressure'))
        skin_thickness = float(request.POST.get('skin thickness'))
        insulin = float(request.POST.get('insulin'))
        bmi = float(request.POST.get('BMI'))
        diabetes_pedigree_function = float(request.POST.get('diabetes pedigree function'))
        age = int(request.POST.get('age'))
        date = request.POST.get('date')
        date_object = datetime.strptime(date, '%Y-%m-%d')

        
        input_features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, 
        bmi, diabetes_pedigree_function, age]])

        final_features = scaler.transform(input_features)
        prediction = model.predict(final_features)

        if prediction[0] == 1:
            message = 'You likely have diabetes. Visit your doctor as soon as possible!'
            diabetes = 1
        else:
            message = 'You do not have diabetes!'
            diabetes = 2
        print(type(date_object))

        new_log = HealthLog(pregnancies=pregnancies, glucose=glucose, blood_pressure=blood_pressure,
        skin_thickness=skin_thickness, insulin=insulin, bmi=bmi, diabetes_pedigree_function=diabetes_pedigree_function, 
        age=age, diabetes_prediction=prediction[0],date_created=date_object)
        new_log.save()
        


        context = {
            'message': message,
            'glucose': glucose,
            'insulin': insulin,
            'bmi': bmi,
            'age': age,
            'diabetes': diabetes
        }
        return render(request, 'health_logging/form.html', context)
    else:
        return render(request, 'health_logging/form.html')
