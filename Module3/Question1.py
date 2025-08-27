length = float(input("Enter the length of the zander in centimeters: "))

if length < 42:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    missing_cm = 42 - length
    print(f"The fish was {missing_cm:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")