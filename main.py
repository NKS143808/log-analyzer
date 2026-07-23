from collections import Counter

print("=" * 40)
print("       LOG ANALYZER")
print("=" * 40)

filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    counter = Counter()

    for line in lines:
        if "ERROR" in line.upper():
            counter["Errors"] += 1
        elif "WARNING" in line.upper():
            counter["Warnings"] += 1
        elif "INFO" in line.upper():
            counter["Info"] += 1

    print("\nLog Summary")
    print("-" * 30)
    print(f"Errors   : {counter['Errors']}")
    print(f"Warnings : {counter['Warnings']}")
    print(f"Info     : {counter['Info']}")

except FileNotFoundError:
    print("Log file not found.")
