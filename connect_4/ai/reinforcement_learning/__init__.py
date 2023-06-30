import pandas as pd
import os


if os.path.exists('q_table.csv'):
    q_table = pd.read_csv('q_table.csv')
else:
    q_table = pd.DataFrame(columns=['state', 'action', 'disc', 'quality'])
