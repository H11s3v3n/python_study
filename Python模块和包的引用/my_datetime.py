from datetime import datetime

def days_until(date_str):
    """计算从今天到指定日期的天数"""
    target_date = datetime.strptime(date_str, "%Y-%m-%d")
    today = datetime.today()
    delta = target_date - today
    return delta.days

# 示例
print(days_until("2025-09-10"))  # 输出剩余天数
