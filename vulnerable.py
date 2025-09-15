import os
import pickle
import subprocess

# Vulnerability 1: Command Injection
def run_command(user_input):
    os.system("ping -c 1 " + user_input)

# Vulnerability 2: Unsafe eval()
def evaluate_expression(expr):
    return eval(expr)

# Vulnerability 3: Insecure Deserialization
def load_data(pickled_data):
    return pickle.loads(pickled_data)

# Vulnerability 4: Hardcoded Credentials
def connect_to_db():
    username = "admin"
    password = "P@ssw0rd123"
    print(f"Connecting to DB with user {username}")

# Vulnerability 5: Subprocess with shell=True
def run_subprocess(user_input):
    subprocess.call(f"ls {user_input}", shell=True)

# Testing the functions
if __name__ == "__main__":
    user_input = input("Enter host to ping: ")
    run_command(user_input)

    expr = input("Enter math expression: ")
    print(evaluate_expression(expr))

    data = input("Enter pickled data: ").encode()
    print(load_data(data))

    connect_to_db()

    user_input = input("Enter directory to list: ")
    run_subprocess(user_input)
