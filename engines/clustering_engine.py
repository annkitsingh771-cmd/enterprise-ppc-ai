def cluster_keywords(df):
    df["cluster"] = df["search_term"].astype(str).apply(
        lambda x:" ".join(x.lower().split()[:2])
    )
    return df
