# Medical Data Visualizer

This project visualizes and analyzes medical examination data using **Python**, **Pandas**, **Matplotlib**, and **Seaborn**. The dataset contains information about patients’ body measurements, blood tests, lifestyle habits, and the presence of cardiovascular disease.  

The goal is to explore relationships between cardiac disease, body metrics, blood markers, and lifestyle choices.

---

## **Dataset**

The dataset file is named: `medical_examination.csv`

**Columns and Description:**

| Feature                     | Variable Type        | Column Name  | Value Type / Notes |
|------------------------------|-------------------|-------------|------------------|
| Age                          | Objective Feature  | age         | int (days)       |
| Height                       | Objective Feature  | height      | int (cm)         |
| Weight                       | Objective Feature  | weight      | float (kg)       |
| Gender                       | Objective Feature  | gender      | categorical code |
| Systolic blood pressure      | Examination Feature| ap_hi       | int              |
| Diastolic blood pressure     | Examination Feature| ap_lo       | int              |
| Cholesterol                  | Examination Feature| cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose                      | Examination Feature| gluc        | 1: normal, 2: above normal, 3: well above normal |
| Smoking                      | Subjective Feature | smoke       | binary (0/1)     |
| Alcohol intake               | Subjective Feature | alco        | binary (0/1)     |
| Physical activity            | Subjective Feature | active      | binary (0/1)     |
| Presence of cardiovascular disease | Target Variable | cardio      | binary (0/1)     |

---

## **Project Features**

1. **Categorical Plot**
   - Visualizes counts of good and bad outcomes for:
     - `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `overweight`
   - Split by patients with `cardio=0` and `cardio=1`.

2. **Overweight Column**
   - Calculates BMI and marks patients as overweight (`1`) or not (`0`).

3. **Normalized Data**
   - Values for cholesterol and glucose are normalized:
     - `0` → good
     - `1` → bad

4. **Heat Map**
   - Visualizes correlations between features.
   - Cleans data by removing incorrect values:
     - diastolic > systolic
     - heights and weights outside 2.5–97.5 percentile range

---

## **Installation**

Make sure you have Python installed. Then install the required libraries:

```bash
pip install pandas matplotlib seaborn numpy
```
## Usage

1. Generate the dataset:

```bash
python generate_medical_dataset.py
```

## Run the main program to visualize data:

```bash
python main.py
```

## File Structure

```bash
medical_data_visualizer_project/
│
├── medical_data_visualizer.py   # Contains draw_cat_plot and draw_heat_map functions
├── main.py                      # Script to run and test the visualizations
├── generate_medical_dataset.py  # Script to generate synthetic medical dataset
├── medical_examination.csv      # Dataset file
├── README.md                    # Project documentation
└── test_module.py               # Unit tests
```
