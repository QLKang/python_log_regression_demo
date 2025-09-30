from collections import Counter

def count_lines(file_path):
    """Count the total number of lines in the file"""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return len(lines)

def count_words(file_path):
    """Count the frequency of each word in the file"""
    with open(file_path, 'r') as f:
        words = []
        for line in f:
            # Strip leading and trailing spaces, the split into words
            words.extend(line.strip().split())
        return Counter(words)
    

if __name__ == "__main__":
    file_path = "sample.txt"

    # Count total lines
    total_lines = count_lines(file_path)
    print(f"Total lines: {total_lines}")

    # Count the word frequencies:
    word_counts = count_words(file_path)
    print("Word frequencies:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")