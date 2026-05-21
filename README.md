# Enterprise Sales Intelligence Dashboard

## 🎯 Project Overview
This project delivers a comprehensive, interactive sales dashboard that integrates static statistical analysis with dynamic data exploration. Built entirely in Python, it utilizes Streamlit to unify Seaborn's rigorous statistical plotting and Plotly's web-based interactivity into a single, cohesive interface. The design adheres to a modern, high-contrast visual aesthetic to ensure data readability and a professional presentation.

## 🛠️ Technical Stack
* **Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Statistical Visualization:** Seaborn, Matplotlib
* **Interactive Visualization:** Plotly Express

## 📊 Features & Chart Types
The dashboard features a 2x2 grid alongside full-width interactive elements, fulfilling the requirement for at least 5 distinct chart types:
1. **Boxplot (Seaborn):** Price distribution across product categories to identify outliers.
2. **Violin Plot (Seaborn):** Probability density of sales volume across demographic age groups.
3. **Correlation Heatmap (Seaborn):** Statistical mapping of relationships between numerical variables (e.g., discount rates vs. revenue).
4. **Line Chart (Plotly):** Interactive, zoomable daily revenue tracking with hover-over data points.
5. **Treemap (Plotly):** Deep-dive hierarchical view of revenue share by product sub-categories.

## 📋 Repository Structure
```text
├── dashboard.py           # Main Streamlit application file
├── dashboard.ipynb        # Jupyter Notebook detailing Day 1-5 EDA and prototypes
├── requirements.txt       # Python dependencies
└── visualizations/        # Directory containing static prototype exports (.png)

##💻 Setup & Installation Instructions
Follow these steps to configure your environment and launch the dashboard locally.

1.**Clone the repository**

'''Bash
git clone <your-repo-url>
cd <your-repo-directory>
2. **Create a virtual environment**

'''Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. **Install dependencies**

'''Bash
pip install -r requirements.txt
4. **Launch the application**

'''Bash
streamlit run dashboard.py