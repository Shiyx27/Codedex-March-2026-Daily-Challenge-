def blood_moon(time):
    
    h, m = map(int, time.split(':'))
    total_mins = h * 60 + m
    results = []
    
    for _ in range(3):
        total_mins += 168
       
        current_cycle = total_mins % 1440
        new_h = current_cycle // 60
        new_m = current_cycle % 60
        
        results.append(f"{new_h:02d}:{new_m:02d}")
        
    return results
