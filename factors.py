import sys

# Function to factorize a number
def factorize(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            p = i
            q = n // i
            print(f"{n}={p}*{q}")
            return
    # If no factors found, it's a prime number
    print(f"{n}={n}*1")

def main(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                number = int(line.strip())
                if number <= 1:
                    print(f"Invalid input: {number} is not a valid natural number greater than 1.")
                else:
                    factorize(number)
    except FileNotFoundError:
        print(f"Error: Unable to open file {filename}")
    except ValueError:
        print(f"Invalid input: {line.strip()} is not a valid natural number.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
    else:
        main(sys.argv[1])

