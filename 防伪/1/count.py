count_file = "visit_count.txt"  # 存储访问次数的文件名

# 读取访问次数
def get_count():
    try:
        with open(count_file, "r") as file:
            count = file.read()
            return int(count) if count.strip().isdigit() else 0
    except FileNotFoundError:
        return 0

# 更新访问次数
def update_count():
    count = get_count() + 1
    with open(count_file, "w") as file:
        file.write(str(count))
    return count

# 响应访问请求
if __name__ == "__main__":
    import cgi

    form = cgi.FieldStorage()
    action = form.getvalue("action", "")

    if action == "get":
        print("Content-type: text/plain\n")
        print(get_count())
    elif action == "update":
        new_count = update_count()
        print("Content-type: text/plain\n")
        print(new_count)
