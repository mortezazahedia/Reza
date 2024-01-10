# main_script.py
from my_package.calculator import Calculator
import os

def main():
    # Perform addition using the Calculator class
    calc = Calculator()
    result = calc.add(2, 3)

    # Save the result in result.txt
    file_path = os.path.join(os.getcwd(), "result.txt")
    with open(file_path, "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
