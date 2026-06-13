# Height Weight Prediction using Linear Regression

A machine learning project that predicts a person's weight based on height using the Linear Regression algorithm. The project demonstrates the complete supervised learning workflow including dataset creation, model training, evaluation, and visualization.

---

## Project Overview

This project uses **Linear Regression** to analyze the relationship between **height** and **weight**.  

A synthetic dataset is generated using NumPy, the model is trained using Scikit-Learn, performance is evaluated using standard regression metrics, and results are visualized using Matplotlib.

The objective is to understand how regression models learn relationships between numerical variables.

---

## Tech Stack

- Python  
- NumPy  
- Matplotlib  
- Scikit-Learn  

---

## Machine Learning Workflow

The project follows a standard supervised machine learning pipeline:

1. Generate synthetic height and weight dataset  
2. Split data into training and testing sets  
3. Train Linear Regression model  
4. Predict weight values on test data  
5. Evaluate model performance  
6. Visualize regression line and actual data points  

---

## Dataset Generation

Synthetic dataset generated using NumPy:

- Heights generated using Normal Distribution  
- Mean Height = 170 cm  
- Standard Deviation = 10  
- Total Samples = 100  

Weight is calculated using:

```python
weight = height × 0.5 + random noise
```

This simulates real-world correlation between height and weight.

---

## Model Used

Algorithm used:

**Linear Regression**

Equation learned by the model:

```text
y = mx + c
```

Where:

- x = Height  
- y = Weight  
- m = Slope (relationship strength)  
- c = Intercept  

---

## Evaluation Metrics

Model performance evaluated using:

### Mean Squared Error (MSE)

Measures average squared prediction error.

### R² Score

Measures how well the model explains variation in data.

Range:

- 1.0 → Perfect prediction  
- 0.8+ → Very good model  
- 0 → Poor model  

---

## Output Visualization

The project visualizes:

- Blue points → Actual data points  
- Red line → Regression line learned by the model  

Example graph:

<img width="959" height="502" alt="Screenshot 2026-06-13 201711" src="https://github.com/user-attachments/assets/28cc297a-eebe-48fe-b106-194db7e0d14d" />


## Key Concepts Demonstrated

- Supervised Learning  
- Regression Analysis  
- Train-Test Split  
- Model Training  
- Prediction  
- Error Evaluation  
- Data Visualization  
- Relationship Modeling  

---


## Project Structure

```text
height-weight-prediction-linear-regression/
│
├── main.py

├── README.md
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/your-username/height-weight-prediction-linear-regression.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
python main.py
```

---

## Author

**Ashutosh Gupta**

GitHub: https://github.com/ashutoshdeepu256-coder

---

## Learning Outcome

This project helped in understanding how machine learning models learn patterns from data, make predictions, and evaluate performance using regression metrics.
