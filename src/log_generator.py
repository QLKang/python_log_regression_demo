import random
import datetime

def generate_test_log(log_file, num_lines=50):
    """Generate a random log file for testing"""
    levels = ["INFO", "WARNING", "ERROR"]
    messages = [
        "System started",
        "Connection lost",
        "Low memory",
        "Something went wrong",
        "Operation completed",
        "User login successful",
        "File not found",
        "Network timeout"
    ]
    with open(log_file, 'w') as f:
        for _ in range(num_lines):
            lvl = random.choice(levels)
            msg = random.choice(messages)
            f.write(f"{lvl} {msg}\n")

def generate_log(file_path, num_lines=100):
    """自动生成测试日志文件"""
    levels = ["INFO", "WARNING", "ERROR"]
    messages = [
        "System started successfully",
        "Connection established",
        "Low memory warning",
        "Disk space running low",
        "An error occurred in module X",
        "User login failed",
        "Configuration loaded"
    ]
    
    with open(file_path, "w") as f:
        for _ in range(num_lines):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            level = random.choice(levels)
            message = random.choice(messages)
            f.write(f"{timestamp} - {level} - {message}\n")

if __name__ == "__main__":
    # Example: create a test log before running pytest
    generate_test_log("tests/auto_generated.log", 30)
    print("✅ Auto-generated test log: tests/auto_generated.log")
