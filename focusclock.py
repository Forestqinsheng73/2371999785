import time

def concentration_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    print("专注倒计时开始！")
    
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        print("剩余时间：{:02d}:{:02d}".format(remaining_seconds // 60, remaining_seconds % 60))
        time.sleep(1)
    
    print("时间到！专注时间结束。")

# 设置专注时长为25分钟
concentration_timer(25)
