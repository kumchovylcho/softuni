from collections import deque


def main(_packages, _couriers):
    total_delivered_weight = 0

    while _packages and _couriers:
        package = _packages.pop()
        courier = _couriers.popleft()

        if courier >= package:
            if courier > package:
                courier -= package * 2
                if courier > 0:
                    _couriers.append(courier)
            total_delivered_weight += package
        elif courier < package:
            total_delivered_weight += courier
            _packages.append(package - courier)


    print(f"Total weight: {total_delivered_weight} kg")
    if not _packages and not _couriers:
        print(f"Congratulations, all packages were delivered successfully by the couriers today.")
    elif _packages and not _couriers:
        print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(x) for x in _packages)}")
    elif _couriers and not _packages:
        print(f"Couriers are still on duty: {', '.join(str(x) for x in _couriers)} but there are no more packages to deliver.")



packages_weights = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())
main(packages_weights, couriers)
