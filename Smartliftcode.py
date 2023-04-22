import random

# Timetable data
timetable = {
    "Monday": {"09:00-12:00": 3, "12:00-15:00": 6, "15:00-18:00": 9},
    "Tuesday": {"09:00-12:00": 2, "12:00-15:00": 5, "15:00-18:00": 8},
    "Wednesday": {"09:00-12:00": 4, "12:00-15:00": 7, "15:00-18:00": 10},
    "Thursday": {"09:00-12:00": 2, "12:00-15:00": 5, "15:00-18:00": 8},
    "Friday": {"09:00-12:00": 3, "12:00-15:00": 6, "15:00-18:00": 9},
}

# Lift data
lifts = {
    "Lift1": random.randint(1, 14),
    "Lift2": random.randint(1, 14),
    "Lift3": random.randint(1, 14),
}


# Function to determine the available floors based on crowd density
def available_floors(crowd_density):
    if crowd_density == "low":
        return [i for i in range(1, 15)]
    elif crowd_density == "medium":
        return [i for i in range(2, 15, 2)]
    elif crowd_density == "high":
        return [i for i in range(2, 15, 2) if i % 4 == 0]


# Function to determine the lift nearest to the current floor
def nearest_lift(current_floor):
    lift_distances = {lift: abs(current_floor - lifts[lift]) for lift in lifts}
    nearest_lift = min(lift_distances, key=lift_distances.get)
    return nearest_lift


# Main program
crowd_density = input("Enter crowd density (low/medium/high): ")
current_floor = int(input("Enter current floor: "))
destination_floor = timetable[input("Enter day: ")][
    input("Enter time slot (hh:mm-hh:mm): ")
]
available_floors_list = available_floors(crowd_density)

if (
    current_floor in available_floors_list
    and int(destination_floor) in available_floors_list
):
    nearest_lift = nearest_lift(current_floor)
    print(f"Go to {nearest_lift} for lift.")
    print(
        f"Take {nearest_lift} to floor {destination_floor}. Current Lift Location is floor {lifts[nearest_lift]}"
    )
else:
    nearest_lift = nearest_lift(current_floor)
    print(f"Go to {nearest_lift} for lift.")
    print(
        f"You have to take {nearest_lift} to floor {destination_floor-1} and then take stairs to reach at floor {destination_floor}. Current Lift Location is floor {lifts[nearest_lift]}"
    )
