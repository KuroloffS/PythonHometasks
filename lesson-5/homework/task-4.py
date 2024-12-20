universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students = [university[1] for university in universities]
    tuition_fees = [university[2] for university in universities]
    return students, tuition_fees

def mean(values):
    return sum(values) / len(values)

def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:  # Even number of elements
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:  # Odd number of elements
        return sorted_values[mid]

students, tuition_fees = enrollment_stats(universities)
total_students = sum(students)
total_tuition = sum(tuition_fees)
student_mean = mean(students)
student_median = median(students)
tuition_mean = mean(tuition_fees)
tuition_median = median(tuition_fees)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print()
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("******************************")