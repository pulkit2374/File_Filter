import argparse
import os
import time
from datetime import datetime

# Function to filter files by extension
def filter_by_extension(directory, extension):
    return [f for f in os.listdir(directory) if f.endswith(extension)]

# Function to filter files by size
def filter_by_size(directory, size):
    return [f for f in os.listdir(directory) if os.path.getsize(f) >= size]

# Function to filter files by last modified date
def filter_by_date(directory, days):
    current_time = time.time()
    time_threshold = current_time - (days * 86400)  # 86400 seconds = 1 day
    return [f for f in os.listdir(directory) if os.path.getmtime(f) >= time_threshold]

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Filter files based on different criteria.")
    parser.add_argument('--path', type=str, default='.', help="Directory to search for files.")
    parser.add_argument('--extension', type=str, help="Filter files by extension (e.g., .txt).")
    parser.add_argument('--size', type=int, help="Filter files by minimum size (in bytes).")
    parser.add_argument('--date', type=int, help="Filter files modified in the last N days.")
    return parser.parse_args()

# Main function to handle file filtering based on arguments
def main():
    args = parse_arguments()
    
    # Start with the directory specified by user
    directory = args.path

    # Apply filters based on user input
    files = os.listdir(directory)

    if args.extension:
        files = filter_by_extension(directory, args.extension)
    
    if args.size:
        files = filter_by_size(directory, args.size)
    
    if args.date:
        files = filter_by_date(directory, args.date)
    
    # Print filtered files
    print("Filtered files:")
    for file in files:
        print(file)

if __name__ == "__main__":
    main()
