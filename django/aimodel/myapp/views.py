from django.shortcuts import render
import pandas as pd
import joblib
import os
from django.conf import settings


model_path = os.path.join(settings.BASE_DIR, 'myapp', 'templates', 'projectmodel.sav')
model = joblib.load(model_path)


def predict_performance(attendance, absent, release):
    total_days = attendance + absent + release

    attendance_rate = attendance / total_days
    absent_rate = absent / total_days
    release_rate = release / total_days

    input_data = pd.DataFrame({
        'attendance_rate': [attendance_rate],
        'absent_rate': [absent_rate],
        'release_rate': [release_rate]
    })

    predicted_performance = model.predict(input_data)
    return predicted_performance[0]


def projectindex(request):
    if request.method == 'POST':
        try:
        
            attendance = float(request.POST.get('attendance'))
            absent = float(request.POST.get('absent'))
            release = float(request.POST.get('released'))

            
            performance_prediction = predict_performance(attendance, absent, release)
            performance_pred = round(performance_prediction, 2)
            
            def result1(prediction):
                if prediction <= 20:
                    return "The student's performance is very poor"
                elif prediction <= 50:
                    return "The student's performance is poor"
                elif prediction <= 70:
                    return "The student's performance is good"
                elif prediction <= 90:
                    return "The student's performance is very good"
                else:
                    return "The student's performance is excellent"

            result_text = result1(performance_prediction)

            
            return render(request, 'result.html', {'result': (f'{result_text} and final grade will be :{performance_pred}%')})

        except ValueError:
            
            return render(request, 'result.html', {'result': "Please enter valid numbers."})

    
    return render(request, 'projectindex.html')


def result(request):
    return render(request, 'result.html')
