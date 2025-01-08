import json
import csv

# Load tasks from JSON file
def load_tasks(file_name):
    with open(file_name, mode='r') as file:
        return json.load(file)

# Save tasks to JSON file
def save_tasks(file_name, tasks):
    with open(file_name, mode='w') as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    print("ID | Task Name         | Completed | Priority")
    print("---|-------------------|-----------|---------")
    for task in tasks:
        print(f"{task['id']:>2} | {task['task']:<17} | {task['completed']:<9} | {task['priority']:<7}")

# Calculate statistics
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

# Convert JSON data to CSV
def convert_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

# Main execution
def main():
    json_file = 'tasks.json'
    csv_file = 'tasks.csv'

    # Load tasks
    tasks = load_tasks(json_file)

    # Display tasks
    display_tasks(tasks)

    # Calculate and display stats
    calculate_stats(tasks)

    # Modify a task example (mark task 1 as completed)
    tasks[0]['completed'] = True

    # Save updated tasks back to JSON file
    save_tasks(json_file, tasks)

    # Convert tasks to CSV
    convert_to_csv(json_file, csv_file)

if __name__ == "__main__":
    main()
