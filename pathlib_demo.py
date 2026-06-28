from pathlib import Path

# 1. 获取当前项目目录
# 提示：使用 Path.cwd()
current_dir = Path.cwd()
print(current_dir)

# 2. 创建一个 notes 文件夹（如果不存在）
# 提示：mkdir(exist_ok=True)
notes_dir = current_dir / "notes"
notes_dir.mkdir(parents= True, exist_ok=True)

# 3. 在 notes 下创建 hello.txt
# 写入一句：
# Hello AI Engineer!
hello_file = notes_dir / "hello.txt"
hello_file.write_text("Hello AI Engineer!", encoding="utf-8")

# 4. 读取 hello.txt 并打印内容
# 提示：read_text()
content = hello_file.read_text()
print(content)

# 5. 打印：
# 文件名
print(hello_file.name)
# 后缀
print(hello_file.suffix)
# 绝对路径
print(hello_file.resolve())