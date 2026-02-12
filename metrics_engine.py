import numpy as np

def calculate_metrics(df):
    df["cpc"] = np.where(df["clicks"]>0, df["spend"]/df["clicks"],0)
    df["ctr"] = np.where(df["impressions"]>0, df["clicks"]/df["impressions"]*100,0)
    df["cvr"] = np.where(df["clicks"]>0, df["orders"]/df["clicks"]*100,0)
    df["roas"] = np.where(df["spend"]>0, df["sales"]/df["spend"],0)
    df["acos"] = np.where(df["sales"]>0, df["spend"]/df["sales"]*100,0)
    return df
