Also added a video to show the working

---

# 📊 Messaging Data Analytics & Cybersecurity Threat Detection Tool

A **full-stack data analytics and cybersecurity tool** that analyzes messaging data (WhatsApp chat exports) and detects **potential phishing URLs using Machine Learning**.
This project combines **data preprocessing, visual analytics, and ML-based threat detection** in a single interactive dashboard built with **Streamlit**.

---

## 🚀 Project Overview

This tool takes raw exported chat data and transforms it into meaningful insights such as:

* Message activity trends
* User behavior analytics
* Word usage patterns
* Emoji analysis
* **Phishing URL detection using Logistic Regression**

It is designed to simulate **real-world messaging analytics and security monitoring systems**, similar to tools used in SOC (Security Operations Center) environments.

---

## ✨ Key Features

### 📈 Data Analytics Features

* 📊 **Total Messages, Words, Media, and Links Count**
* 🗓️ **Monthly & Daily Message Timeline Analysis**
* 📅 **Most Active Days & Months**
* 🔥 **Weekly Activity Heatmap (Day vs Time Period)**
* 👥 **Most Active Users in Group Chats**
* ☁️ **Word Cloud Generation**
* 📝 **Most Commonly Used Words**
* 😀 **Emoji Usage Analysis**

---

### 🔐 Cybersecurity & Threat Detection Features

* 🔍 **Automatic URL Extraction from Messages**
* ✅ **URL Validation using Regex**
* 🧠 **Machine Learning-based Phishing Detection**

  * Model: **Logistic Regression**
  * Feature Extraction: **Text Vectorization**
* 🛡️ **Trusted Domain Whitelisting**
* 📊 **Prediction Confidence Scores**
* 🚨 Clear classification of:

  * **Safe URLs**
  * **Phishing URLs**
* 🧾 Interactive display of detected phishing links

---

## 🧠 Machine Learning Details

* **Algorithm Used:** Logistic Regression
* **Why Logistic Regression?**

  * Lightweight & fast
  * Ideal for binary classification (Phishing vs Safe)
  * Produces probability scores (confidence)
* **Model Pipeline:**

  1. URL text preprocessing
  2. Vectorization
  3. Logistic Regression prediction
  4. Confidence score extraction
  5. Rule-based override for trusted domains

---

## 🛠️ Tech Stack

### 👨‍💻 Programming & Libraries

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Regex (re)** – Text parsing & validation

### 📊 Data Visualization

* **Matplotlib**
* **Seaborn**
* **WordCloud**

### 🤖 Machine Learning

* **Scikit-learn**
* **Logistic Regression**
* **Pickle** – Model serialization

### 🌐 Web App & UI

* **Streamlit** – Interactive dashboard

### 🔐 Cybersecurity Tools

* **URLExtract** – URL extraction from text
* **Custom Regex Rules** – URL validation
* **Trusted Domain Whitelisting**

---

## 📂 Project Structure

```
├── main.py                  # Streamlit application
├── helper.py               # Analytics & phishing detection logic
├── preprocessor.py         # Chat preprocessing module
├── phishing.pkl            # Trained ML phishing model
├── vectoriser.pkl          # URL vectorizer
├── stop_hinglish.txt       # Stopwords list
├── README.md               # Project documentation
```

---

## 📌 How It Works

1. Upload exported WhatsApp chat file
2. Chat text is preprocessed into structured data
3. Analytics modules generate visual insights
4. URLs are extracted from messages
5. ML model predicts phishing probability
6. Results are displayed with confidence scores

---

## 🎯 Use Cases

* SOC / Cybersecurity Projects
* Messaging Platform Analytics
* Phishing Detection Systems
* Data Analytics Dashboards
* Resume & Portfolio Projects

---


---


