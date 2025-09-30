# python_log_regression_demo

python_log_regression_demo/
│
├── logs/
│   └── sample.log          # Sample log file
│
├── src/
│   └── log_parser.py       # Main Python script
│
├── tests/
│   └── test_log_parser.py  # pytest test file
│
└── README.md               # Project description / documentation






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
