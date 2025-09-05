import json
import csv


# 1. 读取JSON文件
file_name = "jobs_250905134124_start_120"

with open(f"{file_name}.json", "r", encoding="utf-8") as jsonfile:
    data = json.load(jsonfile)  # 假设JSON是字典列表格式

for row in data:
    for key, value in row.items():
        if isinstance(value, str):
            row[key] = value.replace("\n", " ")

# 写入CSV文件
with open(f"{file_name}.csv", "w", newline="", encoding="utf-8") as csvfile:
    # 获取字段名（字典的键）
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys(), quoting=csv.QUOTE_ALL)  # 强制所有字段加引号

    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入表头
    writer.writeheader()
    # 写入数据行
    writer.writerows(data)

print(f"CSV文件已生成：{file_name}.csv")

# 1. 读取CSV文件
# with open(f"{file_name}.csv", "r", encoding="utf-8") as csvfile:
#     reader = csv.reader(csvfile)  # 创建读取器对象
#     for row in reader:  # 逐行遍历
#         print(row)  # 每行是一个列表，如 ['Name', 'Age', 'City']

# 2. 读取为字典列表（带表头）
# with open(f"{file_name}.csv", "r", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)  # 第一行作为键
#     data = [row for row in reader]  # 转换为字典列表
#     print(data)  # 输出如 [{'Name': 'Alice', 'Age': '25'}, ...]
