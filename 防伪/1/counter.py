# counter.py

# Read the current count from the file
def read_count():
    try:
        with open('count.txt', 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Increment and save the count
def increment_count():
    count = read_count()
    count += 1
    with open('count.txt', 'w') as file:
        file.write(str(count))

# Main program
if __name__ == '__main__':
    increment_count()
