def main():
    while True:
        time = input("What time is it? ").strip()
        try:
            
            meal_time = convert(time)
            if 7.0 <= meal_time <= 8.0:
                print("breakfast time")
            elif 12.0 <= meal_time <= 13.0:
                print("lunch time")
            elif 18.0 <= meal_time <= 19.0:
                print("dinner time")
            
            break

        except ValueError:
            print("Invalid user input. Please enter time in the format HH:MM (e.g., 7:30).")
            continue
        
    
           



def convert(time):
    if ":" not in time:
        raise ValueError("Missing ':' in time")
    
    try:
        hr, min = time.split(":")
        hr = int(hr)
        min = round(int(min) / 60, 1)
        return float(hr + min)
    except ValueError:
        return f"Incorrect user input!"
    
if __name__ == "__main__":
    main()


def convert(time):
    if ":" not in time:
        raise ValueError("Missing ':' in time")
    
    try:
        hr, min = time.split(":")
        hr = int(hr)
        min = round(int(min) / 60, 1)
        return float(hr + min)
    except ValueError:
        return f"Incorrect user input!"
    
if __name__ == "__main__":
    main()