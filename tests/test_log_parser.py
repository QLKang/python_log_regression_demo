from src.log_parser import (
    parse_errors, 
    word_frequency, 
    count_lines,
    count_by_level,
    top_n_words,
    save_word_freq_to_csv
)
from src.log_generator import generate_test_log
import os
import csv

# 自动生成测试日志
@pytest.fixture
def auto_log_file(tmp_path):
    file_path = tmp_path / "auto.log"
    generate_test_log(file_path, num_lines=20)
    return file_path

# -----------------------------
# 基础功能测试
# -----------------------------
def test_parse_errors(auto_log_file):
    test_file = "tests/test_sample.log"
    # 写入文件
    with open(test_file, 'w') as f:
        f.write("INFO Start\nERROR Something went wrong\nINFO Done\n")

    # 确保文件写入完成后再读取   
    errors = parse_errors(test_file)  # 文件写入已完成
    assert len(errors) == 1
    assert errors[0] == "ERROR Something went wrong"

def test_word_frequency():
    test_file = "tests/test_sample.log"
    with open(test_file, 'w') as f:
        f.write("INFO Start\nERROR Something went wrong\nINFO Done\n")
    
    freq = word_frequency(test_file)
    assert freq["Start"] == 1
    assert freq["Something"] == 1
    assert freq["went"] == 1
    assert freq["wrong"] == 1
    assert freq["Done"] == 1

def test_count_lines():
    test_file = "tests/test_sample.log"
    with open(test_file, 'w') as f:
        f.write("Line1\nLine2\nLine3\n")
    
    assert count_lines(test_file) == 3
    # os.remove(test_file)