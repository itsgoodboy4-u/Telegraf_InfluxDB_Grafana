import random
import time
import csv

file_path = 'test5.csv'

def append_random_integers():
    while True:
        # Generate 6 random integers
        random_integers = [random.randint(0, 500) for _ in range(6)]
        
        # Append the integers to the CSV file
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(random_integers)
        
        # Wait for 5 seconds before next iteration
        time.sleep(5)

# Run the function
append_random_integers()
