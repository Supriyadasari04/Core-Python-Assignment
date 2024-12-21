def display_available_seats(total_seats, booked_seats):
    available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return available_seats

def book_seat(seat, booked_seats, total_seats):
    if seat in booked_seats:
        return False  
    if seat < 1 or seat > total_seats:
        return False  
    booked_seats.append(seat)
    return True

def cancel_seat(seat, booked_seats):
    if seat in booked_seats:
        booked_seats.remove(seat)
        return True
    return False  
total_seats = 10
booked_seats = [2, 5, 7]
book_seat_number = 3
cancel_seat_number = 5

if book_seat(book_seat_number, booked_seats, total_seats):
    print(f"Seat {book_seat_number} successfully booked.")
else:
    print(f"Failed to book seat {book_seat_number}. It may be already booked or out of range.")

if cancel_seat(cancel_seat_number, booked_seats):
    print(f"Seat {cancel_seat_number} successfully canceled.")
else:
    print(f"Failed to cancel seat {cancel_seat_number}. It may not have been booked yet.")

available_seats = display_available_seats(total_seats, booked_seats)
print("Available seats:", available_seats)