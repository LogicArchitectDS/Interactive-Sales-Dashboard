import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

# --- Configuration & Modern Innovator Theme ---
st.set_page_config(page_title="Interactive Sales Dashboard", layout="wide")

BG_COLOR = "#121212"
TEXT_COLOR = "#EAEAEA"
ACCENT_BLUE = "#3366FF"
HIGHLIGHT_GREEN = "#1DB954"
ACCENT_PURPLE = "#8A2BE2"
ACCENT_ORANGE = "#FF9F1C"

# Force Seaborn/Matplotlib into the dark modern theme
plt.style.use("dark_background")
plt.rcParams.update(
    {
        "figure.facecolor": BG_COLOR,
        "axes.facecolor": BG_COLOR,
        "text.color": TEXT_COLOR,
        "axes.labelcolor": TEXT_COLOR,
        "xtick.color": TEXT_COLOR,
        "ytick.color": TEXT_COLOR,
        "axes.edgecolor": "#333333",
    }
)
sns.set_palette([ACCENT_BLUE, HIGHLIGHT_GREEN, ACCENT_PURPLE])


# --- Data Generation ---
@st.cache_data
def load_data():
    np.random.seed(42)
    categories = ["Electronics", "Software", "Hardware", "Services"]
    data = {
        "Date": pd.date_range(start="2025-01-01", periods=365),
        "Category": np.random.choice(categories, 365),
        "Price": np.random.normal(150, 40, 365),
        "Units_Sold": np.random.randint(1, 100, 365),
        "Customer_Age": np.random.normal(35, 10, 365),
        "Discount": np.random.uniform(0, 0.3, 365),
    }
    df = pd.DataFrame(data)
    df["Revenue"] = df["Price"] * df["Units_Sold"] * (1 - df["Discount"])
    
    # Adding realistic subcategories to make the Treemap hierarchical and visually rich
    subcategories = {
        "Electronics": ["Smart Devices", "Wearables", "Accessories"],
        "Software": ["Cloud SaaS", "Enterprise License", "Cybersecurity"],
        "Hardware": ["Servers & Storage", "Workstations", "Networking Gear"],
        "Services": ["Consulting", "Managed Services", "System Integration"]
    }
    # Deterministically assign subcategories based on random choice
    sub_rng = np.random.RandomState(42)
    df["Subcategory"] = df.apply(lambda row: sub_rng.choice(subcategories[row["Category"]]), axis=1)
    return df


df = load_data()

st.markdown(
    f"<h1 style='text-align: center; color: {TEXT_COLOR};'>Enterprise Sales Intelligence</h1>",
    unsafe_allow_html=True,
)

# --- 2x2 Subplot Grid via Streamlit Columns ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Price Distribution (Seaborn Boxplot)")
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="Category", y="Price", data=df, ax=ax1, width=0.5, linewidth=1.5)
    ax1.set_title("Price Distribution by Category", color=TEXT_COLOR)
    st.pyplot(fig1)

with col2:
    st.subheader("2. Customer Demographics (Seaborn Violin Plot)")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.violinplot(x="Category", y="Customer_Age", data=df, ax=ax2, inner="quartile")
    ax2.set_title("Age Distribution per Category", color=TEXT_COLOR)
    st.pyplot(fig2)

col3, col4 = st.columns(2)

with col3:
    st.subheader("3. Feature Correlation (Seaborn Heatmap)")
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    corr = df[["Price", "Units_Sold", "Customer_Age", "Discount", "Revenue"]].corr()
    # Customizing heatmap colors to match the theme
    sns.heatmap(
        corr,
        annot=True,
        cmap=sns.dark_palette(ACCENT_BLUE, as_cmap=True),
        ax=ax3,
        cbar_kws={"label": "Correlation Coefficient"},
    )
    st.pyplot(fig3)

with col4:
    st.subheader("4. Revenue Over Time (Plotly Interactive)")
    daily_rev = df.groupby("Date")["Revenue"].sum().reset_index()
    fig4 = px.line(
        daily_rev, x="Date", y="Revenue", title="Daily Revenue Trend (Zoomable)"
    )
    fig4.update_traces(line_color=HIGHLIGHT_GREEN, line_width=3)
    fig4.update_layout(
        plot_bgcolor=BG_COLOR, paper_bgcolor=BG_COLOR, font_color=TEXT_COLOR
    )
    st.plotly_chart(fig4, use_container_width=True)

# --- Full Width Interactive Plotly Chart ---
st.subheader("5. Revenue Composition (Plotly Treemap)")
fig5 = px.treemap(
    df,
    path=["Category", "Subcategory"],
    values="Revenue",
    color="Category",
    color_discrete_map={
        "Hardware": ACCENT_BLUE,
        "Services": HIGHLIGHT_GREEN,
        "Software": ACCENT_PURPLE,
        "Electronics": ACCENT_ORANGE,
    },
    title="Revenue Share by Product Category & Subcategory",
    height=450,
)

fig5.update_traces(
    texttemplate="<b>%{label}</b><br>$%{value:,.0f}",
    hovertemplate="<b>%{label}</b><br>Revenue: $%{value:,.2f}<br>Share: %{percentRoot:.1%}<extra></extra>"
)

fig5.update_layout(
    plot_bgcolor=BG_COLOR,
    paper_bgcolor=BG_COLOR,
    font_color=TEXT_COLOR,
    margin=dict(t=50, l=10, r=10, b=10),
)
st.plotly_chart(fig5, use_container_width=True)
