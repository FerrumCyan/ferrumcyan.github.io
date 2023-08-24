from flask import Flask

app = Flask(__name__)

def read_count():
    try:
        with open('count.txt', 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def increment_count():
    count = read_count()
    count += 1
    with open('count.txt', 'w') as file:
        file.write(str(count))
    return count

@app.route('/count')
def get_count():
    count = increment_count()
    return str(count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
