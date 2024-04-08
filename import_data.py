import pandas as pd
from constants import RECIPES

df = pd.read_csv(RECIPES)

for i, row in df.iterrows():
    payload = {
        
    }