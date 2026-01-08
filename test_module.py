import unittest
import pandas as pd
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class TestMedicalDataVisualizer(unittest.TestCase):

    def test_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig)  # Check the figure is returned

    def test_heat_map(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig)  # Check the figure is returned

    def test_dataframe_columns(self):
        df = pd.read_csv('medical_examination.csv')
        expected_columns = [
            'age', 'height', 'weight', 'gender', 'ap_hi', 'ap_lo',
            'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio'
        ]
        for col in expected_columns:
            self.assertIn(col, df.columns)

if __name__ == "__main__":
    unittest.main()
