from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    def __init__(self):
        self.users: [User] = []
        self.vehicles: [BaseVehicle] = []
        self.routes: [Route] = []

    @staticmethod
    def find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    @staticmethod
    def find_attribute(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return getattr(obj, attribute)

    @property
    def car_types(self):
        return {
            "PassengerCar": PassengerCar,
            "CargoVan": CargoVan,
        }

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.find_object(driving_license_number, "driving_license_number", self.users)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"


    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.car_types:
            return f"Vehicle type {vehicle_type} is inaccessible."

        car = self.find_object(license_plate_number, "license_plate_number", self.vehicles)

        if car:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.car_types[vehicle_type](brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."


    def allow_route(self, start_point: str, end_point: str, length: float):
        route = []

        for item, attr in ((start_point, "start_point"), (end_point, "end_point"), (length, "length")):
            result = self.find_attribute(item, attr, self.routes)

            route.append(result)

        if len(route) == 3:
            for attr, arg_attr in zip(route, (start_point, end_point, length)):
                if attr == arg_attr:
                    continue

                break

            else:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."


        for r in self.routes:
            if r.start_point == start_point and \
                r.end_point == end_point and \
                r.length < length:

                return f"{start_point}/{end_point} shorter route had already been added to our platform."


        for r in self.routes:
            if r.start_point == start_point and \
                r.end_point == end_point and \
                r.length > length:

                r.is_locked = True


        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = self.find_object(driving_license_number, "driving_license_number", self.users)
        car = self.find_object(license_plate_number, "license_plate_number", self.vehicles)
        road = self.find_object(route_id, "route_id", self.routes)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if car.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if road.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        car.drive(road.length)

        if is_accident_happened:
            car.is_damaged = True
            user.decrease_rating()

        elif not is_accident_happened:
            user.increase_rating()


        return car.__str__()

    def repair_vehicles(self, count: int):
        damaged_cars = [c for c in self.vehicles if c.is_damaged]

        sorted_cars = sorted(damaged_cars, key=lambda c: (c.brand, c.model))[:count]

        for car in sorted_cars:
            car.recharge()
            car.change_status()

        return f"{len(sorted_cars)} vehicles were successfully repaired!"

    def users_report(self):
        output = ["*** E-Drive-Rent ***",]

        arrange_users_descending = sorted(self.users, key=lambda u: -u.rating)

        for user in arrange_users_descending:
            output.append(user.__str__())

        return '\n'.join(output)


app = ManagingApp()
print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())





