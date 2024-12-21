def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10
    total_fare = base_fare + (distance_fare * distance)
    return total_fare

def calculate_total_fares(trips):
    total_fare = 0
    for i, trip in enumerate(trips):
        fare = calculate_fare(trip)
        total_fare += fare
        print(f"Trip {i + 1}: ${fare}")
    return total_fare
trips = [5, 10, 3]  
total_fare = calculate_total_fares(trips)
print(f"Total Fare: ${total_fare}")