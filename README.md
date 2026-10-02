# 🧮 Parallel Computing Calculator

A Python program that performs basic arithmetic operations using **both sequential and parallel execution**, then compares their execution times. This project demonstrates the concept of **parallel computing** using Python's `multiprocessing` module.

---

## 📌 Features

- ✅ Basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- ✅ Division-by-zero error handling
- ✅ **Sequential execution** using normal function calls
- ✅ **Parallel execution** using `multiprocessing.Process` and `Queue`
- ✅ Execution time measurement using `time.perf_counter()`
- ✅ Side-by-side time comparison between sequential and parallel execution

---

## 🛠️ Requirements

- **Python 3.x**
- No external libraries required
- Uses only built-in modules:
  - `time`
  - `multiprocessing`

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/sameer29515/calculator.git


2. Navigate to folder cd calculator
3. Run the program:
python calculator.py
Sample Output
text
===================================
       PARALLEL COMPUTING CALCULATOR
===================================
Enter first number: 10
Enter second number: 5

Numbers entered: 10.0 and 5.0

========== SEQUENTIAL RESULTS ==========
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0
Sequential Execution Time: 0.0000123 seconds

========== PARALLEL RESULTS ==========
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0
Parallel Execution Time: 0.0452310 seconds

===================================
          TIME COMPARISON
===================================
Sequential Time: 0.0000123 seconds
Parallel Time: 0.0452310 seconds

For this calculation, sequential execution was faster.
