import time
from multiprocessing import Process, Queue


# ===============================
# Calculator Functions
# ===============================

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# ===============================
# Parallel Functions
# ===============================

def calculate_addition(a, b, queue):
    queue.put(("Addition", addition(a, b)))


def calculate_subtraction(a, b, queue):
    queue.put(("Subtraction", subtraction(a, b)))


def calculate_multiplication(a, b, queue):
    queue.put(("Multiplication", multiplication(a, b)))


def calculate_division(a, b, queue):
    queue.put(("Division", division(a, b)))


# ===============================
# Main Program
# ===============================

if __name__ == "__main__":

    print("===================================")
    print("       PARALLEL COMPUTING CALCULATOR")
    print("===================================")

    # Get numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nNumbers entered:", num1, "and", num2)

    # ===============================
    # Sequential Calculation
    # ===============================

    start_time = time.perf_counter()

    add_result = addition(num1, num2)
    sub_result = subtraction(num1, num2)
    mul_result = multiplication(num1, num2)
    div_result = division(num1, num2)

    end_time = time.perf_counter()

    sequential_time = end_time - start_time

    print("\n========== SEQUENTIAL RESULTS ==========")
    print("Addition:", add_result)
    print("Subtraction:", sub_result)
    print("Multiplication:", mul_result)
    print("Division:", div_result)

    print("Sequential Execution Time:",
          sequential_time, "seconds")

    # ===============================
    # Parallel Calculation
    # ===============================

    queue = Queue()

    start_time = time.perf_counter()

    # Create processes
    p1 = Process(
        target=calculate_addition,
        args=(num1, num2, queue)
    )

    p2 = Process(
        target=calculate_subtraction,
        args=(num1, num2, queue)
    )

    p3 = Process(
        target=calculate_multiplication,
        args=(num1, num2, queue)
    )

    p4 = Process(
        target=calculate_division,
        args=(num1, num2, queue)
    )

    # Start processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Wait for processes to finish
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end_time = time.perf_counter()

    parallel_time = end_time - start_time

    # Get results
    results = {}

    for i in range(4):
        operation, result = queue.get()
        results[operation] = result

    # ===============================
    # Display Parallel Results
    # ===============================

    print("\n========== PARALLEL RESULTS ==========")
    print("Addition:", results["Addition"])
    print("Subtraction:", results["Subtraction"])
    print("Multiplication:", results["Multiplication"])
    print("Division:", results["Division"])

    print("Parallel Execution Time:",
          parallel_time, "seconds")

    # ===============================
    # Time Comparison
    # ===============================

    print("\n===================================")
    print("          TIME COMPARISON")
    print("===================================")

    print("Sequential Time:",
          sequential_time, "seconds")

    print("Parallel Time:",
          parallel_time, "seconds")

    if sequential_time < parallel_time:
        print("\nFor this calculation, sequential execution was faster.")

    elif parallel_time < sequential_time:
        print("\nFor this calculation, parallel execution was faster.")

    else:
        print("\nBoth execution times were approximately equal.")