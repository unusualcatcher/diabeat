# DiaBeat

DiaBeat is a cutting-edge platform designed to empower individuals in managing and understanding their diabetes risk. The platform allows users to log their health markers, such as blood glucose levels, BMI etc. in a user-friendly digital space. These entries can be visualized through intuitive graphs, providing valuable insights into trends over time. DiaBeat also features a robust prediction tool powered by advanced machine learning algorithms, enabling users to assess their risk for diabetes and take proactive steps toward a healthier lifestyle.

## Features

- **Health Marker Logging**: Users can securely log health markers such as blood glucose levels, BMI, and physical activity.
- **Graphical Visualizations**: View trends in health markers over time through dynamic and intuitive graphs.
- **Diabetes Prediction**: Leverages advanced machine learning algorithms to assess diabetes risk.

## Getting Started

To get started with DiaBeat, follow the instructions below.

### Prerequisites

1. **Python**: Ensure you have Python 3.8+ installed. You can download it from [here](https://www.python.org/downloads/).

### Installation

1. **Download the ZIP file**: 
   - Download the project ZIP file from the GitHub repository and extract it to your desired location.

2. **Navigate to the directory with the project directory**:
 ```
 cd path/to/extracted-folder
```
4. **Create a virtual environment**:
   ```
   python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate cd dia_beat/
   ```

4. **Install the required packages**:
```
pip install -r requirements.txt
```
5. **Run the project**:
Go to the directory containing the manage.py file (root project directory)
```
python manage.py runserver
```
The website can be accessed at:
```
http://localhost:8000
```

### Acknowledgements
The Machine Learning model in this project was trained using the data set provided by kaggle. It is avaible at: https://www.kaggle.com/datasets/mathchi/diabetes-data-set
