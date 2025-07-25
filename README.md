# 🏠 House Price Prediction (London)

A Django-based web application that predicts house prices in London using a trained machine learning model. The user provides input through a web form, and the app returns the predicted property price based on those features.

---

## 🚀 Features

- Clean and responsive web interface
- House price prediction using a trained ML model
- Based on London housing market data
- HTML templates for `home` and `predict` pages
- Static assets (e.g. images) for UI enhancement

---

## 🗂️ Project Structure

```
.
├── db.sqlite3                  # Default SQLite database
├── HousePred/                 # Django project core
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── manage.py                  # Django management script
├── README.md                  # You're reading it!
├── static/                    # Static files (images, CSS, JS)
│   ├── image.jpg
│   └── img1.jpg
└── templates/                 # HTML templates
    ├── home.html
    └── predict.html
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```

### 2. Create and activate a virtual environment

```bash
conda create -n housepred-env python=3.10
conda activate housepred-env
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, you can manually install Django:
```bash
pip install django
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

Now visit: `http://127.0.0.1:8000/`

---

## 🧠 ML Model

> Note: The model code and `.pkl` file are not shown in the structure above. If the model is trained externally (e.g., in Jupyter), ensure it's loaded in `views.py` using `joblib` or `pickle`.

Example:
```python
import joblib
model = joblib.load('path_to_model.pkl')
```

---

## 📸 Screenshots

*(Add UI screenshots of the home page and prediction results if available)*

---

## 📄 License

MIT License. Feel free to fork, modify, and use!

---

## 🙋‍♀️ Acknowledgments

- Dataset source: [e.g., Kaggle, UK government open data]
- Django documentation: https://docs.djangoproject.com/

