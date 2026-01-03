# 📊 Instagram Reach Analysis using Python

## 📌 Overview

Instagram plays a critical role in digital presence, content visibility, and audience growth. This project performs a **data-driven analysis of Instagram post reach**, focusing on how different engagement metrics and traffic sources contribute to overall impressions.

The analysis combines **exploratory data analysis (EDA)**, **visual analytics**, and **relationship modeling** to understand content performance and audience behavior using real Instagram reach data.

---

## 🎯 Objectives

- Analyze the distribution of Instagram impressions across different sources
- Understand the role of engagement metrics (likes, comments, shares, saves)
- Study relationships between impressions and user actions
- Identify which factors most strongly influence reach
- Provide actionable insights for content optimization

---

## 📂 Dataset Description

- **Dataset name:** `Instagram_reach_data.csv`
- **Data type:** Post-level Instagram analytics

### Key Variables

| Column | Description |
|------|-------------|
| Impressions | Total number of views |
| From Home | Impressions from home feed |
| From Hashtags | Impressions via hashtags |
| From Explore | Impressions via explore page |
| From Other | Other sources |
| Likes | Number of likes |
| Comments | Number of comments |
| Shares | Number of shares |
| Saves | Number of saves |
| Profile Visits | Profile visits from the post |
| Follows | New follows |
| Caption | Post caption text |
| Hashtags | Hashtags used |

---

## 🛠 Tools & Technologies

- **Language:** Python  
- **Libraries:**
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn
  - Plotly
  - WordCloud
  - scikit-learn

- **Techniques:**
  - Exploratory Data Analysis (EDA)
  - Distribution analysis
  - Correlation analysis
  - Visual analytics
  - Conversion rate analysis

---

## 📁 Repository Structure

```
instagram-reach-analysis/
│
├── data/
│ └── Instagram_reach_data.csv
│
├── notebooks/
│ ├── Insta_reach_analysis.ipynb
│ └── source_code.ipynb
│
├── scripts/
│ └── html.py
│
├── results/
│ ├── Insta_reach_analysis.html
│ └── Insta_reach_analysis.pdf
│
├── LICENSE
└── README.md
```

---

## 📊 Analysis Highlights
📌 Source-wise Reach Distribution

Home Feed: ~44% (most consistent source)

Hashtags: ~34% (balanced and scalable)

Explore: ~19% (high variance, viral potential)

Others: ~3% (minimal impact)

---

## 📈 Engagement Insights

Likes show a strong positive correlation with impressions

Shares have a moderate positive effect and act as virality indicators

Comments show weak or negative correlation with reach

Saves, follows, and profile visits strongly influence impressions

---

## 🔄 Conversion Metrics

Profile visit → follow conversion rate ≈ 41%

Above typical industry benchmarks

Indicates strong content relevance and audience targeting

---

## 🧠 Key Insights

Home feed provides stability, while Explore drives rare but massive reach

Likes and shares are more reliable reach drivers than comments

Hashtag strategy significantly affects discoverability

High impressions do not necessarily translate to higher comments

Conversion metrics provide deeper insight than raw engagement counts

---

## 📜 License

This project is licensed under the MIT License.
See the LICENSE
 file for details.

---

## 📌 Notes

This project is intended for educational and portfolio purposes.

Code prioritizes clarity, reproducibility, and interpretability.

Possible future extensions include:

Time-series analysis of reach

Predictive modeling for impressions

Content recommendation insights

Dashboard deployment using Streamlit or Dash

🧾 Author

Mr Rup
GitHub: https://github.com/Mr-Rup

---
