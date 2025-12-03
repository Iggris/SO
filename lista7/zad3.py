import glob

total_vmsize = 0
total_vmrss = 0

for path in glob.glob("/proc/[0-9]*/status"):
    vmsize = 0
    vmrss = 0
    try:
        with open(path) as f:
            for line in f:
                if line.startswith("VmSize:"):
                    vmsize = int(line.split()[1])
                elif line.startswith("VmRSS:"):
                    vmrss = int(line.split()[1])
    except FileNotFoundError:
        continue

    total_vmsize += vmsize
    total_vmrss += vmrss

print("Suma VmSize: {} kB".format(total_vmsize))
print("Suma VmRSS : {} kB".format(total_vmrss))
