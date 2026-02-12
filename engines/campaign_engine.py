import pandas as pd

def generate_bulk(df, base_name):
    exact_campaign = f"Exact | {base_name}"
    rows = []

    rows.append({
        "Record Type":"Campaign",
        "Campaign":exact_campaign,
        "Campaign Daily Budget":500,
        "State":"enabled"
    })

    rows.append({
        "Record Type":"Ad Group",
        "Campaign":exact_campaign,
        "Ad Group":"Main",
        "State":"enabled"
    })

    for _,row in df.iterrows():
        if row["roas"]>1:
            rows.append({
                "Record Type":"Keyword",
                "Campaign":exact_campaign,
                "Ad Group":"Main",
                "Keyword Text":row["search_term"],
                "Match Type":"Exact",
                "Bid":row["suggested_bid"],
                "State":"enabled"
            })

    return pd.DataFrame(rows)
