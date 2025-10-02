from collections import Counter
import re
import csv
import random

def parse_errors(log_file):
    """Extract lines containing 'ERROR' from the log file"""
    errors = []
    with open(log_file, 'r') as f:
        for line in f:
            # print ("----test line---", line)
            if "ERROR" in line:
                errors.append(line.strip())
    return errors

def word_frequency(log_file):
    """Count the occurence of each word in the log file"""
    words = []
    with open(log_file, 'r') as f:
        for line in f:
            # print("---line:", line)
            # Remove only the first column (log level) and optional spaces
            # Remove timestamp; only count the message part
            msg = re.sub(r"^\S+\s*", "", line).strip()
            # print("---msg:",msg)
            words.extend(msg.split())
            # print("---words:", words)
    return Counter(words)
    
def count_lines(log_file):
    """Count the total number of lines in the log file"""
    with open(log_file, 'r') as f:
        return sum(1 for _ in f)
    
def count_by_level(log_file):
    """Count number of INFO / WARNING / ERROR lines"""
    levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    with open(log_file, 'r') as f:
        for line in f:
            for lvl in levels.keys():
                if line.startswith(lvl):
                    levels[lvl] += 1
    return levels

def top_n_words(log_file, n=5):
    freq = word_frequency(log_file)
    return freq.most_common(n)

def save_word_freq_to_csv(log_file, output_csv):
    freq = word_frequency(log_file)
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Word", "Count"])
        for word, count in freq.items():
            writer.writerow([word, count])

if __name__ == "__main__":
    file_path = "../logs/sample.log"
    print(f"Total lines: {count_lines(file_path)}")
    errors = parse_errors(file_path)
    print("Errors:", errors)
    print("Error lines:")
    for e in errors:
        print(e)

    freq = word_frequency(file_path)
    print("Word frequencies:")
    for word, count in freq.items():
       print(f"{word}: {count}")
    print("Top 5 words:", top_n_words(file_path, 5))

    output_csv = "../logs/word_count.csv"  # Path to save the CSV
    #Call the function
    save_word_freq_to_csv(file_path, output_csv)
    print(f"Word frequency CSV saved to: {output_csv}")


