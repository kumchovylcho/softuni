class Trip:
    DESTINATION_PRICES_PER_PERSON = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}

    def __init__(self, budget: float, travelers_number: int, is_family: bool):
        self.budget = budget
        self.travelers = travelers_number
        self.is_family = is_family
        self.booked_destinations_paid_amounts = {}

    @property
    def travelers(self):
        return self._travelers

    @travelers.setter
    def travelers(self, value):
        if value < 1:
            raise ValueError('At least one traveler is required!')
        self._travelers = value

    @property
    def is_family(self):
        return self._is_family

    @is_family.setter
    def is_family(self, value):
        if value and self.travelers < 2:
            self._is_family = False
        else:
            self._is_family = value

    def book_a_trip(self, destination: str):
        if destination not in self.DESTINATION_PRICES_PER_PERSON:
            return 'This destination is not in our offers, please choose a new one!'

        required_price = self.DESTINATION_PRICES_PER_PERSON[destination] * self.travelers
        if self.is_family:
            required_price *= 0.9
        if self.budget < required_price:
            return 'Your budget is not enough!'

        self.booked_destinations_paid_amounts[destination] = required_price
        self.budget -= required_price
        return f'Successfully booked destination {destination}! Your budget left is {self.budget:.2f}'

    def booking_status(self):
        if not self.booked_destinations_paid_amounts:
            return f'No bookings yet. Budget: {self.budget:.2f}'
        result = []
        sorted_bookings = sorted(self.booked_destinations_paid_amounts.items())
        for booked_destination, paid_amount in sorted_bookings:
            result.append(f"""Booked Destination: {booked_destination}
Paid Amount: {paid_amount:.2f}""")
        result.append(f"""Number of Travelers: {self.travelers}
Budget Left: {self.budget:.2f}""")
        return '\n'.join(result)


