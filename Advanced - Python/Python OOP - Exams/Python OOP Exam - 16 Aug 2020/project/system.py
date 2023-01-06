from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_instance = PowerHardware(name, capacity, memory)
        if new_instance not in System._hardware:
            System._hardware.append(new_instance)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_instance = HeavyHardware(name, capacity, memory)
        if new_instance not in System._hardware:
            System._hardware.append(new_instance)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        new_instance = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(new_instance)
        System._software.append(new_instance)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        new_instance = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(new_instance)
        System._software.append(new_instance)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]
        if hardware and software:
            hardware, software = hardware[0], software[0]
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_software_memory_cons = sum([s.memory_consumption for s in System._software])
        total_hardware_memory_cons = sum([h.memory for h in System._hardware])
        total_capacity_software_cons = sum([s.capacity_consumption for s in System._software])
        total_capacity_hardware_cons = sum([h.capacity for h in System._hardware])
        result = f"System Analysis\nHardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {total_software_memory_cons} / {total_hardware_memory_cons}\n" \
                 f"Total Capacity Taken: {total_capacity_software_cons} / {total_capacity_hardware_cons}"
        return result

    @staticmethod
    def system_split():
        result = []
        for item in System._hardware:
            number_of_soft_express_comps = [1 for x in item.software_components if x.software_type == "Express"]
            number_of_soft_light_comps = [1 for x in item.software_components if x.software_type == "Light"]
            memory_soft_comps = sum([x.memory_consumption for x in item.software_components])
            total_capacity_soft_comps = sum([s.capacity_consumption for s in item.software_components])
            check_comps = [s.name for s in item.software_components]
            result.append(f"Hardware Component - {item.name}")
            result.append(f"Express Software Components: {len(number_of_soft_express_comps)}")
            result.append(f"Light Software Components: {len(number_of_soft_light_comps)}")
            result.append(f"Memory Usage: {memory_soft_comps} / {item.memory}")
            result.append(f"Capacity Usage: {total_capacity_soft_comps} / {item.capacity}")
            result.append(f"Type: {item.hardware_type}")
            if not check_comps:
                result.append(f"Software Components: None")
            else:
                result.append(f"Software Components: {', '.join(check_comps)}")
        return '\n'.join(result)



