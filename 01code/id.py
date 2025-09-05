import hashlib
import time

company = "Netflix"
role = "Machine Learning Engineer (L4) - Content Production & Promotion"

# 结合公司名、岗位名和时间戳生成哈希ID
data = f"{company}_{role}".encode('utf-8')
unique_id = hashlib.sha256(data).hexdigest()
print("SHA256 Hash ID:", unique_id)