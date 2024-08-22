# Target guided ordinal encoding...

import pandas as pd

df = pd.DataFrame({
    "city":["New York","London","Paris","Tokyo","New York","Paris"],
    "price":[200,150,300,250,180,320]
})

# print(df.head())

# calculate the mean price for each city..

mean_price = df.groupby("city")["price"].mean().to_dict()

# replace each city with mean price...

df["city_encoded"] = df["city"].map(mean_price)

# print(df)