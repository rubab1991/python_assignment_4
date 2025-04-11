def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found the target at index mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

def run_search():
    print("🔍 Binary Search Project")
    try:
        # Get input from user
        raw_input = input("Enter a sorted list of numbers (comma separated): ")
        arr = list(map(int, raw_input.strip().split(",")))
        target = int(input("Enter the number to search for: "))
    except ValueError:
        print("❌ Please enter valid integers.")
        return

    result = binary_search(arr, target)

    if result != -1:
        print(f"✅ Number found at index: {result}")
    else:
        print("❌ Number not found in the list.")

if __name__ == "__main__":
    run_search()
