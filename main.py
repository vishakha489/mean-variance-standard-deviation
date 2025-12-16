from mean_var_std import calculate

def print_results(results):
    """
    Pretty-print the results dictionary
    """
    for key, value in results.items():
        print(f"\n{key.upper()}:")
        print(f"Rows: {value[1]}")
        print(f"Columns: {value[0]}")
        print(f"Flattened: {value[2]}")

# Test different types of input
test_cases = [
    [0,1,2,3,4,5,6,7,8],        # Normal sequential numbers
    [1,1,1,1,1,1,1,1,1],        # All same numbers
    [2,5,3,8,7,1,4,6,0],        # Random numbers
    [1,2,3,4,5],                # Invalid input (less than 9 numbers)
]

for i, test in enumerate(test_cases):
    print(f"\n=== TEST CASE {i+1} ===")
    try:
        results = calculate(test)
        print_results(results)
    except ValueError as ve:
        print(f"Error: {ve}")

