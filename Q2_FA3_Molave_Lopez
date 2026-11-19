# CS2 Q2 FA3 - Data Analyzer Mini-App
# Ronn Gabriel Olazo Lopez

students = ["Ana", "Ben", "Carla", "David", "Ella", "Frank"]
scores = [88, 75, 92, 81, 95, 67]

def display():
    print("\n=== Scores ===")
    for i in range(len(scores)):
        print(f"{i}: {students[i]} - {scores[i]}")

def search():
    name = input("Enter student name: ")
    for i in range(len(students)):
        if students[i].lower() == name.lower():
            print(f"Found: {students[i]} scored {scores[i]} at index {i}")
            return
    print("Not found.")

def average():
    print(f"\nTotal: {sum(scores)}")
    print(f"Average: {sum(scores)/len(scores):.2f}")
    print(f"Highest: {max(scores)} | Lowest: {min(scores)}")

def update():
    display()
    idx = int(input("Enter index to update: "))
    if 0 <= idx < len(scores):
        new = int(input(f"Enter new score for {students[idx]}: "))
        scores[idx] = new
        print(f"Updated {students[idx]} to {new}")
    else:
        print("Invalid index.")

def main():
    print("=== Student Score Analyzer ===")
    while True:
        print("\n1. Display Scores\n2. Search Score\n3. Compute Average\n4. Update Score\n5. Display Updated\n6. Exit")
        c = input("Enter your choice: ")
        if c == "1": display()
        elif c == "2": search()
        elif c == "3": average()
        elif c == "4": update()
        elif c == "5":
            print("\n=== Updated Scores ===")
            display()
            average()
        elif c == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()
