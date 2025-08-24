talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_bullets = talents * 20 * 32 + pounds * 32 + lots
total_grams = total_bullets * 13.3

kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

print("The weight in modern units:")
remaining_grams_truncated = int(remaining_grams * 100) / 100
print(f"{kilograms} kilograms and {remaining_grams_truncated:.2f} grams.")