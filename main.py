import bluetooth

devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(devices)))

for addr, name in devices:
    print("  {} - {}".format(addr, name))
