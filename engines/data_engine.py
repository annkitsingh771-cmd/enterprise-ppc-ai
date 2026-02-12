import pandas as pd

def load_search_file(file):
    df = pd.read_excel(file) if file.name.endswith("xlsx") else pd.read_csv(file)
    df.columns = df.columns.str.lower().str.strip()
    return df

def auto_map_columns(df):
    def find(keys):
        for k in keys:
            for c in df.columns:
                if k in c:
                    return c
        return None

    mapping = {
        "search_term": find(["search term"]),
        "campaign": find(["campaign"]),
        "ad_group": find(["ad group"]),
        "spend": find(["spend"]),
        "sales": find(["total sales","sales"]),
        "orders": find(["orders"]),
        "clicks": find(["clicks"]),
        "impressions": find(["impressions"]),
        "sku": find(["sku"])
    }

    for key,val in mapping.items():
        df[key] = df[val] if val else 0

    return df.fillna(0)
