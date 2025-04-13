# 🧠 Mental Health Prediction API

API ini dibuat menggunakan **Flask** dan **RandomForestClassifier**, yang berfungsi untuk memprediksi status kesehatan mental seseorang berdasarkan beberapa data personal.

## 📌 Fitur yang Digunakan untuk Prediksi

- `age`
- `sleep_hours`
- `work_hours`
- `feels_anxious` (Yes/No)
- `has_support` (Yes/No)
- `eats_well` (Yes/No)
- `physical_activity` (Yes/No)
- `uses_social_media_hours`
- `has_sleep_disorder` (Yes/No)
- `satisfaction_level` (1–10)

Model akan memprediksi salah satu dari status berikut:

- Healthy
- Mild Stress
- Chronic Stress
- Anxiety Disorder
- Depression

---

## 🚀 Cara Menjalankan Proyek

### 1. Clone repo & masuk ke foldernya

```bash
git clone https://github.com/arkhanardana/mindcare-model.git
cd mindcare-model
```

### 2. Install dependencies

```bash
pip install pandas scikit-learn flask flask-cors
```

### 3. Training model

```bash
python train_model.py
```

### 4. Jalankan app

```bash
python app.py
```
