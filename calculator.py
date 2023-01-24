while True:
    try:
        target_number = int(input("Enter the number for the times table (or 0 to exit): "))
        if target_number == 0:
            break
        elif target_number > 10:
            print("Number must be less than or equal to 10.")
            continue
        range_start = int(input("Enter the minimum calculation range: "))
        range_end = int(input("Enter the maximum calculation range: "))
        if range_start > range_end:
            print("That wouldn't make sense, you need to have the minimum LESS than the maximum, silly")
            continue
        for i in range(range_start, range_end+1):
            result = target_number * i
            print(f"{target_number} x {i} = {result}")
    except ValueError:
        print("Input must be an integer, not a decimal, or a phrase.")