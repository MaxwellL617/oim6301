import bmi

result = bmi.compute_bmi(70,1.75)
print(f"Computed BMI: {result: .2f}")

people = [
    {"name": "Alice", "weight_kg": 70, "height_m": 1.75},
    {"name": "Bob", "weight_kg": 85, "height_m": 1.80},
    {"name": "Carla", "weight_kg": 60, "height_m": 1.65},
]


for i in range(len(people)):
    result = bmi.compute_bmi(people[i]['weight_kg'],people[i]['height_m'])
    print(f"Computed BMI for {people[i]['name']}: {result: .2f}")
    