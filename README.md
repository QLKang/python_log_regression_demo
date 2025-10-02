# Python Log Regression Demo

A Python log parser with automated regression tests using `pytest`.
Supports extracting error lines, word frequency analysis, log-level classification, CSV reporting, and automatic test log generation.

---

## 🚀 Features

* 📌 Extract `ERROR` lines from log files
* 📊 Count total lines and word frequency
* ⚠️ Classify log lines by level: `INFO` / `WARNING` / `ERROR`
* 🔝 Output top N frequent words
* 📂 Save word frequency results to CSV
* 📝 Automatically generate test logs for regression
* 🧪 Fully tested using `pytest` (regression loop)

---

## 🗂️ Project Structure

```
python_log_regression_demo/
│
├── logs/
│   └── sample.log           # Sample log file
│
├── src/
│   └── log_parser.py        # Main Python script
│
├── tests/
│   └── test_log_parser.py   # pytest test file
│
└── README.md                # Project description / documentation
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/my-username/python_log_regression_demo.git
cd python_log_regression_demo
```

(Optional) Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main script:

```bash
python3 src/log_parser.py
```

Run tests:

```bash
python3 -m pytest -v
```

---

## 📄 License

This project is for learning purposes.




用 Python 3 运行 pytest 模块，并显示详细测试结果。

ring@Kungs-MacBook-Pro python_log_regression_demo % python3 -m pytest -v
===================================== test session starts =====================================
platform darwin -- Python 3.13.0, pytest-8.4.2, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.13/bin/python3
cachedir: .pytest_cache
rootdir: /Users/ring/Documents/GitHub/python_log_regression_demo
collected 3 items                                                                             

tests/test_log_parser.py::test_parse_errors PASSED                                      [ 33%]
tests/test_log_parser.py::test_word_frequency PASSED                                    [ 66%]
tests/test_log_parser.py::test_count_lines PASSED                                       [100%]

====================================== 3 passed in 0.01s ======================================
ring@Kungs-MacBook-Pro python_log_regression_demo % 
