from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    WAITER_TYPES = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter
    }

    CLIENT_TYPES = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient
    }

    def __init__(self):
        self.waiters = []
        self.clients = []

    @staticmethod
    def find_object(value, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute, False) == value:
                return obj

        return None

    def create_object(self, obj_type: str, options: dict):
        if not options["types"].get(obj_type):
            return options["errors"]["recognised"]

        obj = self.find_object(options["search_by"], options["search_attr"], options["collection"])
        if obj:
            return options["errors"]["exists"]

        options["collection"].append(
            options["types"][obj_type](*options["create_attrs"])
        )
        return options["success"]

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        options = {
            "types": self.WAITER_TYPES,
            "errors": {
                "recognised": f"{waiter_type} is not a recognized waiter type.",
                "exists": f"{waiter_name} is already on the staff."
            },
            "search_by": waiter_name,
            "search_attr": "name",
            "collection": self.waiters,
            "create_attrs": [waiter_name, hours_worked],
            "success": f"{waiter_name} is successfully hired as a {waiter_type}."
        }

        return self.create_object(waiter_type, options)

    def admit_client(self, client_type: str, client_name: str):
        options = {
            "types": self.CLIENT_TYPES,
            "errors": {
                "recognised": f"{client_type} is not a recognized client type.",
                "exists": f"{client_name} is already a client."
            },
            "search_by": client_name,
            "search_attr": "name",
            "collection": self.clients,
            "create_attrs": [client_name],
            "success": f"{client_name} is successfully admitted as a {client_type}."
        }

        return self.create_object(client_type, options)

    def process_shifts(self, waiter_name: str):
        waiter = self.find_object(waiter_name, "name", self.waiters)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = self.find_object(client_name, "name", self.clients)
        if not client:
            return f"{client_name} is not a registered client."

        earned_points = client.earning_points(order_amount)
        return f"{client_name} earned {earned_points} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = self.find_object(client_name, "name", self.clients)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        output = [
            "$$ Monthly Report $$",
            f"Total Earnings: ${sum(waiter.calculate_earnings() for waiter in self.waiters):.2f}",
            f"Total Clients Unused Points: {int(sum(client.points for client in self.clients))}",
            f"Total Clients Count: {len(self.clients)}",
            "** Waiter Details **"
        ]

        sorted_waiters = sorted(self.waiters, key=lambda waiter: (-waiter.calculate_earnings()))
        for waiter in sorted_waiters:
            output.append(waiter.__str__())

        return "\n".join(output)
