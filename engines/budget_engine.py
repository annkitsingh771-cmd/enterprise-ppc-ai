def budget_analysis(df):
    hard_waste = df[(df["orders"]==0)&(df["spend"]>0)]["spend"].sum()
    scale_pool = df[df["roas"]>1]["spend"].sum()
    return hard_waste, scale_pool
