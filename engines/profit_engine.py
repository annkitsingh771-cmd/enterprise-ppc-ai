import numpy as np

def apply_profit_logic(df, margin):
    break_even_roas = 1/(margin/100)
    df["profit_status"] = np.where(df["roas"]>=break_even_roas,"Profitable","Loss Risk")
    return df, break_even_roas
