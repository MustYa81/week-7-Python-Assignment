# week-7-Python-Assignment

# Iris Dataset Analysis

This project performs a comprehensive analysis of the famous Iris dataset using Python. The analysis includes data cleaning, statistical summary, group analysis, and multiple visualizations.

## 📁 Dataset

- **Source:** [Iris Dataset from UCI Repository](https://archive.ics.uci.edu/ml/datasets/iris)
- **Format:** CSV
- **Features:**
  - Sepal length (cm)
  - Sepal width (cm)
  - Petal length (cm)
  - Petal width (cm)
  - Species (Setosa, Versicolor, Virginica)

## 📊 Tasks Performed

### 1. Data Loading and Exploration
- Loaded dataset using `pandas`
- Inspected dataset structure using `.head()`, `.info()`, and `.isnull()`
- Cleaned missing values (none in this dataset)

### 2. Statistical Analysis
- Computed descriptive statistics using `.describe()`
- Grouped by species to analyze average petal/sepal sizes

### 3. Data Visualization

#### ✅ Line Chart
- Simulated time-series of petal length over 150 days

#### ✅ Bar Chart
- Comparison of average petal length across species

#### ✅ Histogram
- Distribution of sepal width

#### ✅ Scatter Plot
- Relationship between sepal length and petal length (color-coded by species)

## 📦 Libraries Used
- pandas
- numpy
- matplotlib
- seaborn

## 📌 Key Insights
- Virginica flowers have the largest petals and sepals.
- Setosa species is clearly separable based on petal length/width.
- Petal dimensions are more effective for classification than sepal dimensions.

## 🚀 Getting Started

To run this project:

```bash
git clone https://github.com/yourusername/iris-analysis.git
cd iris-analysis
pip install -r requirements.txt
python iris_analysis.py


### 🧐 Insights from the Analysis:

1. **Basic Statistics (`.describe()`):**

   * The average sepal length across all flowers is about **5.84 cm**.
   * Petal lengths range from **1.0 cm to 6.9 cm**, with a **standard deviation** of **1.76 cm**, showing high variability.

2. **Grouped Mean by Species:**

   * **Setosa** species tend to have:

     * The **shortest petals and sepals**.
   * **Versicolor** is intermediate in size.
   * **Virginica** has the **largest petal and sepal dimensions**, especially **petal length (mean \~5.55 cm)**.

| Species    | Sepal Length | Sepal Width | Petal Length | Petal Width |
| ---------- | ------------ | ----------- | ------------ | ----------- |
| Setosa     | \~5.01       | \~3.42      | \~1.46       | \~0.25      |
| Versicolor | \~5.94       | \~2.77      | \~4.26       | \~1.33      |
| Virginica  | \~6.59       | \~2.97      | \~5.55       | \~2.03      |

---

### 📌 Interesting Findings:

* Petal length and width are **good discriminators** between the species—Setosa is clearly separable from the others.
* Virginica tends to have **consistently larger features**, which could be useful for classification or predictive modeling.

### 📊 Summary of Each Chart:

1. **Line Chart** – Shows how **petal length changes over time** (simulated). Useful for trend analysis.
2. **Bar Chart** – Compares **average petal length per species**. Shows clear variation across classes.
3. **Histogram** – Displays the **distribution of sepal width**. Helps understand the data's spread and skew.
4. **Scatter Plot** – Reveals the **relationship between sepal length and petal length**, with clear species separation.
