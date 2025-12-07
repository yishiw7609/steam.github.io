## P8105 Data Science Final Project

👥 **Team Members:**  
Yishi Wang · Yutong Mao · Yiquan Zhou · Tao Wu  

---

## 🌟 Project Overview

This project explores **what drives game popularity on Steam**, using a dataset containing metadata, reviews, and engagement statistics for thousands of games.

We completed the full data science workflow:

- 📥 Data collection & cleaning  
- 📊 Exploratory data analysis (EDA)  
- 🤖 Predictive modeling  
- 🌐 Website creation  
- 🎥 Screencast preparation  

All work was done collaboratively using GitHub and R Markdown.

---

## 🧹 Data Processing

Our data pipeline:

- Cleaned metadata fields and standardized variable formats  
- Extracted **primary genre**, converted owner ranges to numeric midpoints  
- Created new features such as:
  - ⭐ Review Ratio  
  - ⭐ Log-transformed Peak CCU, playtime, and price  
- Filtered invalid or missing rows  

This prepared dataset is used for both EDA and modeling.

---

## 📊 Exploratory Data Analysis

Our EDA investigates multiple dimensions of game popularity:

### Key analyses include:
- 🔍 **Distribution of Peak CCU** (log scale)  
- 🆓 **Free vs Paid** game comparison  
- 💵 **Popularity across price tiers**  
- 👍 **Review Ratio vs Engagement**  
- 🧩 **Genre-level popularity**  
- 🧑‍💻 **Developer productivity & quality analysis**  
- 📈 **Release year trends in popularity**  

Plots were generated using **ggplot2**, with interactivity added through **plotly**.

---

## 🤖 Predictive Modeling

We built models to predict **Peak CCU**, a key measure of game popularity.

### Models implemented:
- ⚪ **Baseline Linear Regression**
- 🟢 **Random Forest Regression** (with 500 trees)

### Why Random Forest?
- Handles nonlinear relationships  
- Robust to extreme values (very common in Steam data)  
- Provides interpretable variable importance metrics  

### Evaluation Metrics:
- **RMSE** (Root Mean Squared Error)  
- **NRMSE** (Normalized RMSE)  

Random Forest consistently outperformed the linear baseline, especially for highly popular games.

---

## 🔑 Key Findings

🎯 **Top predictors of popularity:**

1. **📅 Release Date** — strong recency effect; newer games → more players  
2. **👥 Estimated Owners** — larger owner base → higher peak activity  
3. **⏱️ Average Playtime** — long-play games sustain higher CCU  
4. **⭐ Review Ratio** — sharp popularity increase when ratings exceed ~75%  

🎮 **Genre matters less than expected**  
Genres explain player type, but not total popularity volume.

🔥 **New releases + strong reputation + large player base = high CCU**



