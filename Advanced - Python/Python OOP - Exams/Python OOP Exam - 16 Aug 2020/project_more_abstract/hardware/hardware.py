from project.software.software import Software


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: [Software] = []

    @property
    def current_capacity(self):
        return sum(s.capacity_consumption for s in self.software_components)

    @property
    def current_memory(self):
        return sum(s.memory_consumption for s in self.software_components)

    @property
    def installed_light_software(self):
        return [x for x in self.software_components if x.software_type == "Light"]

    @property
    def installed_express_software(self):
        return [x for x in self.software_components if x.software_type == "Express"]

    def install(self, software: Software):
        if self.current_capacity + software.capacity_consumption > self.capacity or \
                self.current_memory + software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def get_all_components(self):
        if self.software_components:
            return ', '.join(s.name for s in self.software_components)
        return 'None'
