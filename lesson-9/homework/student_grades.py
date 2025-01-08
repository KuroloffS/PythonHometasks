import csv

# Read data from grades.csv
def read_grades(file_name):
    grades = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append({
                'Name': row['Name'],
                'Subject': row['Subject'],
                'Grade': float(row['Grade'])
            })
    return grades

# Calculate average grades for each subject
def calculate_average_grades(grades):
    subject_totals = {}
    subject_counts = {}

    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']

        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0

        subject_totals[subject] += grade
        subject_counts[subject] += 1

    averages = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}
    return averages

# Write average grades to average_grades.csv
def write_averages(file_name, averages):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, avg])

# Main execution
def main():
    input_file = 'grades.csv'
    output_file = 'average_grades.csv'

    # Read grades
    grades = read_grades(input_file)

    # Calculate averages
    averages = calculate_average_grades(grades)

    # Write averages to a new file
    write_averages(output_file, averages)

if __name__ == "__main__":
    main()
