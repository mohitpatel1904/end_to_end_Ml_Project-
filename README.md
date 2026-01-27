# 🎓 Student Performance Indicator

### End-to-End Machine Learning Web Application

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS-orange)
![ML](https://img.shields.io/badge/ML-Scikit--learn-yellow)
![Deploy](https://img.shields.io/badge/Deployment-Render-violet)

A comprehensive Machine Learning application that predicts student math scores based on various demographic and educational factors. This project demonstrates a complete end-to-end ML pipeline, from data ingestion to deployment.

## 🌟 Features

-   **🤖 AI-Powered Predictions:** Uses a trained Random Forest Regressor to predict scores with high accuracy (~85% R2 Score).
-   **🎨 Modern UI:** Beautiful Glassmorphism design with responsive layout and smooth animations.
-   **⚙️ Full ML Pipeline:** Modular code structure for Data Ingestion, Transformation, and Model Training.
-   **🚀 Ready for Deployment:** Configured for seamless deployment on Render (or any cloud platform).

## 🛠️ Tech Stack

-   **Backend:** Python, Flask
-   **Machine Learning:** Scikit-learn, Pandas, NumPy, CatBoost, XGBoost
-   **Frontend:** HTML5, CSS3 (Custom Glassmorphism Design)
-   **Deployment:** Gunicorn, Render
-   **Structure:** Modular programming with custom exception handling and logging.

## 📂 Project Structure

```
├── artifacts/          # Generated models and preprocessors
├── notebook/           # Jupyter notebooks for EDA and experimentation
├── src/                # Source code for the ML pipeline
│   ├── components/     # Data Ingestion, Transformation, Model Trainer
│   ├── pipeline/       # Prediction and Training pipelines
│   ├── utils.py        # Utility functions
│   ├── logger.py       # Custom logging setup
│   └── exception.py    # Custom exception handling
├── templates/          # HTML templates for the web app
├── app.py              # Flask application entry point
├── requirements.txt    # Project dependencies
├── setup.py            # Package setup
└── render.yaml         # Render deployment configuration
```

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mohitpatel1904/end_to_end_Ml_Project-.git
    cd end_to_end_Ml_Project-
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\Activate.ps1

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  **Open in Browser:**
    Go to `http://127.0.0.1:5000` to see the app in action!

## 🧠 Model Training

The model takes into account the following features:
-   Gender
-   Race/Ethnicity
-   Parental Level of Education
-   Lunch Type
-   Test Preparation Course
-   Reading Score
-   Writing Score

The best performing model (Random Forest) was selected after evaluating multiple algorithms including Linear Regression, Decision Trees, XGBoost, and CatBoost.

## ☁️ Deployment

This project is configured for **Render**.

1.  Connect your GitHub repository to Render.
2.  Render will automatically detect `render.yaml` or use the following settings:
    -   **Build Command:** `pip install -r requirements.txt`
    -   **Start Command:** `gunicorn app:app`

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📝 Author

**Mohit Patel**
-   [GitHub Profile](https://github.com/mohitpatel1904)