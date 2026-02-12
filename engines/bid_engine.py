def smart_bid(df):
    def calc(row):
        if row["risk_score"]<30 and row["roas"]>1:
            return row["cpc"]*1.2
        if row["risk_score"]>70:
            return row["cpc"]*0.8
        return row["cpc"]
    df["suggested_bid"] = df.apply(calc,axis=1)
    return df
