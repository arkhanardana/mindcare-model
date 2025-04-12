import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

def generate_data(n=500):
    data = []
    for _ in range(n):
        age = random.randint(15, 50)
        sleep_hours = round(random.uniform(3, 9), 1)
        work_hours = round(random.uniform(2, 12), 1)
        feels_anxious = random.randint(0, 1)
        has_support = random.randint(0, 1)
        eats_well = random.randint(0, 1)
        physical_activity = random.randint(0, 1)
        uses_social_media_hours = round(random.uniform(0, 8), 1)
        has_sleep_disorder = random.randint(0, 1)
        satisfaction_level = random.randint(1, 10)

        if feels_anxious and not has_support and has_sleep_disorder and sleep_hours < 5 and satisfaction_level <= 3:
            status = "Depression"
        elif feels_anxious and not has_support and (sleep_hours < 5 or work_hours > 10):
            status = "Anxiety Disorder"
        elif feels_anxious or sleep_hours < 6 or work_hours > 10:
            status = "Chronic Stress"
        elif feels_anxious or sleep_hours < 6:
            status = "Mild Stress"
        else:
            status = "Healthy"

        data.append([
            age, sleep_hours, work_hours, feels_anxious, has_support, eats_well,
            physical_activity, uses_social_media_hours, has_sleep_disorder, satisfaction_level, status
        ])

    return pd.DataFrame(data, columns=[
        "age", "sleep_hours", "work_hours", "feels_anxious", "has_support", "eats_well",
        "physical_activity", "uses_social_media_hours", "has_sleep_disorder", "satisfaction_level", "mental_status"
    ])

# 1. Generate Data
df = generate_data()
df.to_csv("mental_health_advanced.csv", index=False)

# 2. Train Model
X = df.drop("mental_status", axis=1)
y = df["mental_status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# 3. Save model
with open("mental_model_advanced.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model berhasil dibuat dan disimpan sebagai 'mental_model_advanced.pkl'")
