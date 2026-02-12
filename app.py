import streamlit as st
from engines.data_engine import load_search_file, auto_map_columns
from engines.metrics_engine import calculate_metrics
from engines.profit_engine import apply_profit_logic
from engines.clustering_engine import cluster_keywords
from engines.risk_engine import calculate_risk
from engines.bid_engine import smart_bid
from engines.budget_engine import budget_analysis
from engines.campaign_engine import generate_bulk

st.set_page_config(layout="wide")
st.title("🚀 Enterprise Amazon PPC AI")

margin = st.sidebar.slider("Margin %",10,80,40)
base_name = st.sidebar.text_input("Base Campaign Name","Product")

file = st.file_uploader("Upload Search Term Report",type=["csv","xlsx"])

if file:
    df = load_search_file(file)
    df = auto_map_columns(df)
    df = calculate_metrics(df)
    df, breakeven = apply_profit_logic(df, margin)
    df = cluster_keywords(df)
    df = calculate_risk(df)
    df = smart_bid(df)

    hard_waste, scale_pool = budget_analysis(df)

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Spend",round(df["spend"].sum(),2))
    c2.metric("Sales",round(df["sales"].sum(),2))
    c3.metric("Hard Waste",round(hard_waste,2))
    c4.metric("Scale Budget",round(scale_pool,2))

    st.dataframe(df[[
        "search_term","spend","sales","roas",
        "risk_score","suggested_bid","cluster"
    ]].round(2))

    bulk = generate_bulk(df, base_name)
    st.download_button("Download Bulk File",
                       bulk.to_csv(index=False),
                       "bulk_upload.csv")
