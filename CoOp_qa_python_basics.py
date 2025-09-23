# Python for QA Engineers - Crash Course

# 1. VARIABLES (Test Data Storage)
username = "test_user"
password = "Test123!"
expected_result = "Login successful"
test_passed = True

print(f"Testing with user: {username}")
print(f"Expected: {expected_result}")
print(f"Test passed: {test_passed}")

# 2. LISTS (Test Suites)
test_cases = ["login_valid", "login_invalid", "password_reset", "logout"]
results = ["PASS", "FAIL", "PASS", "PASS"]

print(f"\nTotal test cases: {len(test_cases)}")
print(f"First test: {test_cases[0]} - {results[0]}")

# 3. LOOPS (Running Multiple Tests)
print("\n--- Test Results Summary ---")
for i in range(len(test_cases)):
    status = "✅" if results[i] == "PASS" else "❌"
    print(f"{status} {test_cases[i]}: {results[i]}")

# 4. DICTIONARIES (Structured Test Data)
test_data = {
    "valid_user": {"username": "admin", "password": "pass123"},
    "invalid_user": {"username": "wrong", "password": "bad"},
    "empty_fields": {"username": "", "password": ""}
}

print("\n--- Test Data Sets ---")
for test_name, data in test_data.items():
    print(f"{test_name}: {data['username']} / {data['password']}")

# 5. FUNCTIONS (Reusable Test Actions)
def validate_login(username, password):
    """Simulate login validation - like a reusable test step"""
    valid_users = {"admin": "pass123", "tester": "test456"}
    
    if username in valid_users and valid_users[username] == password:
        return "PASS"
    else:
        return "FAIL"

def calculate_pass_rate(results):
    """Calculate test suite success rate"""
    total_tests = len(results)
    passed_tests = results.count("PASS")
    pass_rate = (passed_tests / total_tests) * 100
    return round(pass_rate, 1)

# Test the functions
print("\n--- Function Testing ---")
login_result = validate_login("admin", "pass123")
print(f"Login test: {login_result}")

suite_results = ["PASS", "FAIL", "PASS", "PASS", "FAIL"]
pass_rate = calculate_pass_rate(suite_results)
print(f"Test suite pass rate: {pass_rate}%")