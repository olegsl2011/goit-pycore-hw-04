def total_salary(file_path):
    count = 0
    sum = 0
    try: 
        with open(file_path, "r") as file:
            while True: 
                line = file.readline()
                if not line:
                    break
                sum = sum + int(line.split(",")[1])
                count = count + 1
    except Exception as e:
        print(f"error {e}")
        print(f"check file {file_path}")
        exit(1)
    
    if count != 0: 
        return sum, sum//count
    else:
        return 0, 0


file_path = "text_files/employers_for_salary.txt"
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")