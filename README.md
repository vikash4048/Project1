# 💻 Laptop Price Predictor

![Python]
![Scikit-learn]
![Streamlit]
![License]

## 📍 Overview

**Laptop Price Predictor** is a machine learning web application that helps estimate the price of a laptop based on its specifications. It’s designed for buyers, sellers, and tech enthusiasts who want a quick and accurate price prediction using real-world data.

🚀 Built with:
- **Python**
- **Scikit-learn** for regression modeling
- **Streamlit** for the web interface
- **Pandas** and **NumPy** for data manipulation

---

## 📦 Features

- 🔍 Predicts laptop prices based on key specifications
- 🎛️ User-friendly Streamlit UI
- 📊 Trained with real laptop data (includes preprocessing & feature engineering)
- 🔐 Model serialized using `pickle` for easy deployment

---

## ⚙️ How It Works

### 📥 Input Parameters
- Brand (e.g., Dell, HP, Apple)
- Type (Ultrabook, Notebook, Gaming)
- Processor (e.g., i5, i7, Ryzen)
- RAM Size
- Storage (SSD/HDD)
- GPU Type
- Screen Size and Features (Touchscreen, IPS Panel, Resolution)

### 🔁 Processing
- One-hot encoding for categorical variables
- Derived features (e.g., PPI = Pixels Per Inch)
- Prediction using trained **Random Forest** regression model

### 📤 Output
- An estimated price based on user input

---

## 🛠️ Tech Stack

| Component        | Tech Used            |
|------------------|----------------------|
| Language         | Python 3             |
| Libraries        | Pandas, NumPy, Sklearn |
| Web App          | Streamlit            |
| Model Persistence| Pickle               |

---

## 🚀 Getting Started

### 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/vikash4048/laptop-price-predictor.git
cd laptop-price-predictor
