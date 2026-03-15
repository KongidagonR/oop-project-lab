# time_utils.py - Basic time utilities

def minutes_to_hhmm(minutes):
    """แปลงนาทีเป็น HH:MM"""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

def hhmm_to_minutes(time_str):
    """แปลง HH:MM เป็นนาที"""
    hours, mins = map(int, time_str.split(":"))
    return hours * 60 + mins

def time_diff(start, end):
    """คำนวณผลต่างของเวลา (นาที) จาก HH:MM สองค่า"""
    return hhmm_to_minutes(end) - hhmm_to_minutes(start)

# ทดสอบ
print(minutes_to_hhmm(150))          # 02:30
print(hhmm_to_minutes("08:30"))      # 510
print(time_diff("08:00", "17:00"))   # 540