import numpy as np

def calculate_risk(df):
    avg_roas = df["roas"].mean()
    avg_cpc = df["cpc"].mean()

    def risk(row):
        score = 0
        if row["cpc"] > avg_cpc: score+=30
        if row["roas"] < avg_roas: score+=30
        if row["orders"]==0 and row["spend"]>avg_cpc*5: score+=40
        return min(score,100)

    df["risk_score"] = df.apply(risk,axis=1)
    return df
