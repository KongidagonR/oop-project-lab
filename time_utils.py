OVERTIME_THRESHOLD = "17:00"
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

def work_hours(start, end, break_minutes=60):
    """คำนวณชั่วโมงทำงานสุทธิ หักพักกลางวัน"""
    total = time_diff(start, end)
    net = total - break_minutes
    return minutes_to_hhmm(net)

def is_late(actual_start, scheduled_start="08:30"):
    """เช็คว่ามาสายไหม"""
    return hhmm_to_minutes(actual_start) > hhmm_to_minutes(scheduled_start)

def overtime_minutes(end_time):
    """คำนวณนาที OT (ถ้าออกหลัง 17:00)"""
    threshold = hhmm_to_minutes(OVERTIME_THRESHOLD)
    actual_end = hhmm_to_minutes(end_time)
    if actual_end <= threshold:
        return 0
    return actual_end - threshold

def overtime_pay(end_time, hourly_rate=100):
    """คำนวณค่า OT (คิดเป็นรายชั่วโมง)"""
    ot_mins = overtime_minutes(end_time)
    return (ot_mins / 60) * hourly_rate * 1.5  # OT = 1.5x

# ทดสอบ
print(overtime_minutes("19:00"))           # 120
print(overtime_pay("19:00", 100))          # 300.0
print(overtime_pay("17:00", 100))          # 0.0

# ทดสอบ
print(work_hours("08:00", "17:00"))       # 08:00
print(is_late("08:45"))                   # True
print(is_late("08:00"))                   # False

# ทดสอบ
print(minutes_to_hhmm(150))          # 02:30
print(hhmm_to_minutes("08:30"))      # 510
print(time_diff("08:00", "17:00"))   # 540