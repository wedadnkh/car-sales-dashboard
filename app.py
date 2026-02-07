import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vehicle Ads Dashboard", layout="wide")

st.header("Vehicle Ads Dashboard")
st.write("Interactive dashboard for exploring car sales advertisements.")

# Load dataset
df = pd.read_csv("vehicles_us.csv")


df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["odometer"] = pd.to_numeric(df["odometer"], errors="coerce")
df["model_year"] = pd.to_numeric(df["model_year"], errors="coerce")

st.subheader("Dataset Preview")
st.dataframe(df.head(20))


remove_bad = st.checkbox("Remove listings with missing/invalid price and odometer (recommended)")

df_plot = df.copy()


df_plot = df_plot.dropna(subset=["price"])
df_plot = df_plot[df_plot["price"] > 0]

if remove_bad:
    df_plot = df_plot.dropna(subset=["odometer"])
    df_plot = df_plot[df_plot["odometer"] > 0]

# Histogram
st.subheader("Histogram: Price Distribution")
fig_hist = px.histogram(df_plot, x="price", nbins=60, title="Price distribution (price > 0)")
st.plotly_chart(fig_hist, use_container_width=True)

# Scatter plot
st.subheader("Scatter: Price vs Odometer")
df_scatter = df_plot.dropna(subset=["odometer"])
fig_scatter = px.scatter(df_scatter, x="odometer", y="price", hover_data=["model", "condition", "type"],
                         title="Price vs Odometer")
st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("Scatter: Price vs Model Year (colored by condition)")
df_year = df_plot.dropna(subset=["model_year"])
fig_year = px.scatter(df_year, x="model_year", y="price", color="condition",
                      hover_data=["model", "type"], title="Price vs Model Year by Condition")
st.plotly_chart(fig_year, use_container_width=True)
