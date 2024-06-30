def print_multiplication_table():
    try:
        number = int(input("Enter a number to see its multiplication table: ").strip())
        for i in range(1, 10):
            product = number * i
            print(f"{number} * {i} = {product}")
    except ValueError:
        print("Please enter a valid number.")
if __name__ == "__main__":
    print_multiplication_table()
