import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

df = pd.read_csv('product_asos.csv', on_bad_lines='skip')

df.head()
