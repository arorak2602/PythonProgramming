# LogFileAnalyzer

print("Welcome to log file analyzer")

logFile = input("Enter the log file name or path:\n")

totalLines = 0
infoCount = 0
warningCount = 0
errorCount = 0

try:
    # Open and read file line by line
    with open(logFile, "r") as file:
        for line in file:
            totalLines += 1
            line = line.upper()  # make search case-insensitive

            # Count log levels
            if "INFO" in line:
                infoCount += 1
            elif "WARNING" in line:
                warningCount += 1
            elif "ERROR" in line:
                errorCount += 1

except FileNotFoundError:
    print("Error: The file was not found!")
    exit()

print("Analysis completed!")
print("\n---------------\n")

print(f"Total lines analyzed: {totalLines}")
print(f"INFO count: {infoCount}")
print(f"WARNING count: {warningCount}")
print(f"ERROR count: {errorCount}")

# Determine most frequent log type
if totalLines > 0:
    maxType = max(infoCount, warningCount, errorCount)

    if maxType == infoCount:
        print("Most frequent log type: INFO")
    elif maxType == warningCount:
        print("Most frequent log type: WARNING")
    else:
        print("Most frequent log type: ERROR")