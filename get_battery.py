import subprocess
output1 = subprocess.check_output(["acpi"])
battery=output1.decode('utf-8')
remaing =battery.split('Battery 1:')[1].split('Discharging')[1].split('%')[0].split(',')[1].split(' ')[1]
int(remaing)
