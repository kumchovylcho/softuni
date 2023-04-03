from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_object(hardware_name, "name", System._hardware)

        if not hardware:
            return "Hardware does not exist"

        create_express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(create_express_software)
        System._software.append(create_express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_object(hardware_name, "name", System._hardware)

        if not hardware:
            return "Hardware does not exist"

        create_light_software = LightSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(create_light_software)
        System._software.append(create_light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_object(hardware_name, "name", System._hardware)
        software = System.find_object(software_name, "name", System._software)

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory_consumption_all_software = sum(s.memory_consumption for s in System._software)
        total_memory_all_hardware = sum(h.memory for h in System._hardware)

        total_capacity_consumption_all_software = sum(s.capacity_consumption for s in System._software)
        total_capacity_of_all_hardware = sum(h.capacity for h in System._hardware)

        output = ["System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {total_memory_consumption_all_software} / {total_memory_all_hardware}",
                  f"Total Capacity Taken: {total_capacity_consumption_all_software} / {total_capacity_of_all_hardware}"
        ]

        return '\n'.join(output)

    @staticmethod
    def system_split():
        output = []

        for hardware in System._hardware:
            output.append(f"Hardware Component - {hardware.name}")
            output.append(f"Express Software Components: {len(hardware.installed_express_software)}")
            output.append(f"Light Software Components: {len(hardware.installed_light_software)}")
            output.append(f"Memory Usage: {hardware.current_memory} / {hardware.memory}")
            output.append(f"Capacity Usage: {hardware.current_capacity} / {hardware.capacity}")
            output.append(f"Type: {hardware.hardware_type}")
            output.append(f"Software Components: {hardware.get_all_components()}")

        return '\n'.join(output)
