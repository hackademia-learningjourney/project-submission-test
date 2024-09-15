# name of the project: student_finalprediction_prediction_model:
group name: geeks

**group member**:
sudarshan giri
aaysusha shrestha 
manoj oli 
trishandra jung kocher


### Tech Stack Used
- **Libraries:**
  - `pandas`: For data manipulation and analysis.
  - `numpy`: For numerical operations.
  - `scikit-learn (sklearn)`: For machine learning.
  - `joblib`: For saving and loading machine learning models.
  - `tensorflow`: For deep learning models and neural network implementations (if used).
  - `matplotlib`: For data visualization.
  
- **Framework:**
  - **Django**: As the web framework for handling backend logic, routing, and integration with the machine learning model.

- **Functionalities:**
  - Data preprocessing, model training, evaluation, and visualization.
  - Serving predictions and results via a Django-powered web application.


This Django web application predicts student performance based on their attendance, absenteeism, and early dismissal rates using a pre-trained linear regression model.


**Project Overview**:
This project provides a web interface for users to input their attendance, absenteeism, and early dismissal days to receive a predicted performance score. The prediction is based on a pre-trained linear regression model.

**Setup**:
**Clone the Repository**:
git clone https://github.com/yourusername/student-performance-prediction.git

**Navigate to the Project Directory**:
cd student-performance-prediction

**Create a Virtual Environment (Optional but Recommended)**:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**Install Dependencies**:
Create a requirements.txt file with the following contents:
django
pandas
joblib

**Then install the dependencies:**
pip install -r requirements.txt

**Run Migrations:**
python manage.py migrate

**Run the Development Server:**
python manage.py runserver

**Usage:**
**Access the Application:**
Open your web browser and go to http://localhost:8000/ to access the main page of the web app.
![image](https://github.com/user-attachments/assets/0075dd92-f836-4347-9d27-f6dc8f140be6)

**Submit Data:**
Enter the total attended days, total absent days, and total released/early dismissal days in the form provided on the homepage and submit it.
![image](https://github.com/user-attachments/assets/14372bc2-71f5-49dd-a4d9-25cd56f0632d)


**View Results**:
After submission, you will be redirected to a results page displaying the predicted performance and a performance category message.
![image](https://github.com/user-attachments/assets/abcf5f1d-cc4a-40ff-8888-8234b351cf49)



**How It Works**:

**Model Loading**:
The application loads a pre-trained linear regression model using joblib from a file named projectmodel.sav.

**Predicting Performance**:
The predict_performance function calculates the attendance, absent, and release rates, prepares the input data, and uses the model to predict the student’s performance score.

**Handling Requests**:
The projectindex view handles form submissions, processes the input data, predicts performance, categorizes it, and renders the result page.
The result view simply renders the results page.

**URLs Configuration**:
"" (root URL) maps to the projectindex view.
"result/" maps to the result view.

**File Structure**:
projectindex.html: The main form where users input their data.
result.html: Displays the prediction results.
views.py: Contains the logic for handling form submissions and predictions.
urls.py: Defines the URL routing for the application.
models.py: (Not used in this example, but typically where you define your Django models).
settings.py: Contains the project settings, including paths and configurations.
