import time

def digital_clock():
    print("🕒 Digital Clock - Press Ctrl+C to stop\n")
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print("Time:", current_time, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

def stopwatch():
    print("⏱️ Stopwatch - Press Enter to start/stop and Ctrl+C to reset\n")
    input("Press Enter to start...")
    start_time = time.time()
    try:
        while True:
            elapsed_time = round(time.time() - start_time, 2)
            print("Elapsed Time:", elapsed_time, "seconds", end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")

print("Choose an option:")
print("1. Digital Clock")
print("2. Stopwatch")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    digital_clock()
elif choice == "2":
    stopwatch()
else:
    print("Invalid choice.")
