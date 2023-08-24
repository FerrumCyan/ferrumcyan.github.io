#!/usr/bin/env python3
import cgi
import os

count_file = "visit_count.txt"  # 存储访问次数的文件名

def get_count():
    try:
        with open(count_file, "r") as file:
            count = file.read()
            return int(count) if count.strip().isdigit() else 0
    except FileNotFoundError:
        return 0

def update_count():
    count = get_count() + 1
    with open(count_file, "w") as file:
        file.write(str(count))
    return count

form = cgi.FieldStorage()
action = form.getvalue("action", "")

print("Content-type: text/plain\n")

if action == "get":
    print(get_count())
elif action == "update":
    new_count = update_count()
    print(new_count)
