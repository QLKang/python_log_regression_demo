import os
from src.log_generator import generate_log
from src.log_parser import count_lines, parse_errors, word_frequency, save_word_freq_to_csv

# 1. 定义日志路径
log_file = "logs/sample.log"
output_csv = "logs/word_count.csv"

# 2. 自动生成日志文件
print("=== Step 1: Generating log file ===")
generate_log(log_file, num_lines=20)
print(f"Log file generated at {log_file}")

# 3. 调用 log_parser.py 分析日志
print("\n=== Step 2: Parsing log file ===")
print(f"Total lines: {count_lines(log_file)}")

errors = parse_errors(log_file)
print(f"Found {len(errors)} ERROR logs")

freq = word_frequency(log_file)
print("Top 5 frequent words:")
for word, count in list(freq.items())[:5]:
    print(f"{word}: {count}")

# 4. 保存单词频率到 CSV
print("\n=== Step 3: Saving word frequency to CSV ===")
save_word_freq_to_csv(log_file, output_csv)
print(f"Word frequency saved to {output_csv}")
