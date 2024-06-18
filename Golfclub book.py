class GolfClubBooking:
    def __init__(self):
        self.available_slots = 10  # Assuming the club has 10 slots available initially
        self.bookings = {}  # Dictionary to store participant details

    def book_slot(self, name, email, phone_number):
        if self.available_slots > 0:
            self.bookings[name] = {'email': email, 'phone_number': phone_number}
            self.available_slots -= 1
            return f"Slot booked successfully for {name}."
        else:
            return "Sorry, no slots available."

    def display_bookings(self):
        print("Current Bookings:")
        for name, details in self.bookings.items():
            print(f"{name}: Email - {details['email']}, Phone Number - {details['phone_number']}")

booking_system = GolfClubBooking()
print(booking_system.book_slot("Noah dapash", "noahdapash@gmail.com","0797645060"))

booking_system.display_bookings()
