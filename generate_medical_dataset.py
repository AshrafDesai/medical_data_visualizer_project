import pandas as pd
import numpy as np

# For reproducibility
np.random.seed(42)

# Number of patients
n_patients = 500  # you can increase this to 1000 or more

# Generate data
df = pd.DataFrame({
    'age': np.random.randint(18*365, 65*365, size=n_patients),  # age in days (18 to 65 years)
    'height': np.random.randint(150, 200, size=n_patients),     # height in cm
    'weight': np.random.uniform(50, 120, size=n_patients),      # weight in kg
    'gender': np.random.randint(1, 3, size=n_patients),         # 1: female, 2: male
    'ap_hi': np.random.randint(90, 180, size=n_patients),       # systolic blood pressure
    'ap_lo': np.random.randint(60, 120, size=n_patients),       # diastolic blood pressure
    'cholesterol': np.random.randint(1, 4, size=n_patients),    # 1: normal, 2: above normal, 3: well above normal
    'gluc': np.random.randint(1, 4, size=n_patients),           # 1: normal, 2: above normal, 3: well above normal
    'smoke': np.random.randint(0, 2, size=n_patients),          # 0: no, 1: yes
    'alco': np.random.randint(0, 2, size=n_patients),           # 0: no, 1: yes
    'active': np.random.randint(0, 2, size=n_patients),         # 0: no, 1: yes
    'cardio': np.random.randint(0, 2, size=n_patients)          # 0: no, 1: yes
})

# Ensure diastolic <= systolic
df['ap_lo'] = np.minimum(df['ap_lo'], df['ap_hi'])

# Save to CSV
df.to_csv('medical_examination.csv', index=False)
print("Dataset saved as medical_examination.csv")
