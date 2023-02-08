import pandas as pd

chunk_size = 500
batch_no = 1

for chunk in pd.read_csv("C:/Users/kjeanluc/Documents/PosteTravail/FREE INVEST/Broadcast/02 02 2023/03_02_2023.csv", sep=';', encoding="latin-1", chunksize=chunk_size):
    chunk.to_csv("C:/Users/kjeanluc/Documents/PosteTravail/FREE INVEST/Broadcast/02 02 2023/03_02_2023_" + str(batch_no) + ".csv", sep=';', index=False)
    batch_no += 1
