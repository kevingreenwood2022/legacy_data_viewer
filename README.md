# Legacy Data Viewer

**Legacy Data Viewer** is a web-based tool designed to parse and visualize legacy COBOL-style reports formatted as fixed-width `.txt` files. It helps modernize how users interact with mainframe-generated outputs by converting unstructured line-based data into an interactive, searchable HTML table.

![screenshot](assets/img/legacy-data-screenshot.png)

---

## 🔍 Features

- Upload `.txt` files with fixed-width transaction records
- Automatically parses each line into structured fields:
  - Account Number
  - Date
  - Description
  - Amount
  - Status
- Displays results in a clean, sortable Bootstrap table
- Highlights usability and maintainability in full-stack design
- Includes modular Python parsing logic (`parser.py`)

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Bootstrap 5, JavaScript
- **Parsing:** Fixed-width field parsing in plain Python
- **Optional:** Can be extended with CSV export or pagination

---

## 📂 Project Structure
legacy_data_viewer/
├── app.py # Flask application
├── parser.py # Legacy report parsing logic
├── templates/
│ ├── base.html
│ ├── index.html
│ └── result.html
├── static/
│ └── style.css
├── uploads/ # Uploaded .txt files (excluded via .gitignore)
└── sample_10000_transactions.txt # Sample data for testing

---

## 📄 Sample Input Format

1234567890 2024-12-01Payment Received 000345.00 POSTED
2345678901 2024-12-02Subscription Renewal 000099.99 COMPLETE

---

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/kevingreenwood2022/legacy_data_viewer.git
   cd legacy_data_viewer

2. **Install dependencies**
   pip instlal flask

3. **Run the app**
   python app.py

4. **Visit: http://localhost:5000**
   Upload a .txt file and see it parsed live!

📌 Future Enhancements
  CSV download/export
  Pagination for large datasets
  Highlighting for anomalies or totals
  Upload history tracking

Developed by Kevin Greenwood
