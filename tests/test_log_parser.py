import pytest
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
    errors = parse_errors(auto_log_file)
    # 至少返回一个列表
    assert isinstance(errors, list)

def test_word_frequency(auto_log_file):
    freq = word_frequency(auto_log_file)
    # 至少包含某个单词
    assert isinstance(freq, dict) or hasattr(freq, "most_common")

def test_count_lines(auto_log_file):
    assert count_lines(auto_log_file) == 20

# -----------------------------
# 扩展功能测试
# -----------------------------
def test_count_by_level(auto_log_file):
    levels = count_by_level(auto_log_file)
    assert isinstance(levels, dict)
    assert "INFO" in levels
    assert "WARNING" in levels
    assert "ERROR" in levels
    # 每个值应该是整数且 >=0
    for v in levels.values():
        assert isinstance(v, int) and v >= 0

def test_top_n_words(auto_log_file):
    top_words = top_n_words(auto_log_file, n=3)
    # 返回列表长度 <=3
    assert isinstance(top_words, list)
    assert len(top_words) <= 3
    # 每个元素是元组 (word, count)
    for item in top_words:
        assert isinstance(item, tuple) and len(item) == 2

def test_save_word_freq_to_csv(auto_log_file, tmp_path):
    output_csv = tmp_path / "freq.csv"
    save_word_freq_to_csv(auto_log_file, output_csv)
    # 文件生成
    assert os.path.exists(output_csv)
    # 内容检查
    with open(output_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        assert rows[0] == ["Word", "Count"]  # CSV 表头
        assert len(rows) > 1  # 至少有一条单词记录
