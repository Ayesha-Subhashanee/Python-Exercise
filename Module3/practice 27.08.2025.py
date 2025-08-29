gender = input("Patient gender M/F: ")
hemoglobin = int(input("patient hemoglobin value: "))

if (gender == "N" and hemoglobin < 117) and (gender == "M" and hemoglobin < 134):
    print("Low hemoglobin")
elif (gender == "N" and hemoglobin == 175) and (gender == "M" and hemoglobin > 195):
    print("High hemoglobin")
else:
    print("Normal hemoglobin")