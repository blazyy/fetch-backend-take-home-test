import os
import sys
import pandas as pd

FILENAME = 'transactions.csv'

if len(sys.argv) == 1:
    print('Points not found. Example of usage: python3 mycode.py 5000')
    exit()

if not os.path.isfile(FILENAME):
    print(f'File {FILENAME} not found. Exiting.')
    exit()

points = int(sys.argv[1])
df = pd.read_csv(FILENAME   )
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values('timestamp').reset_index(drop=True)

payer_points = df.groupby('payer', sort=False).sum(numeric_only=True).to_dict()['points']

for i in range(df.shape[0]):
    row = df.iloc[i]
    if row.points > 0:
        amount_to_decrement = min(points, row.points)
        payer_points[row.payer] -= amount_to_decrement
        points -= amount_to_decrement
    else:
        points += abs(row.points)
        payer_points[row.payer] += abs(row.points)

print(payer_points)