months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}
attackers_ips = []
all_ips = dict()
ip_time = 0
file = open("log.txt", "r")

while True:
    record_string = file.readline()
    if not record_string:
        break
    remote_addr = record_string.split(' ')[0]
    if not remote_addr in all_ips.keys():
        all_ips[remote_addr] = [0, 0, 0, 0, 0, 0]
file.close()
file = open("log.txt", "r")
while True:
    leap = False
    record_string = file.readline()
    if not record_string:
        break
    remote_addr = record_string.split(' ')[0]
    if "GET" in record_string or "POST" in record_string:
        date = record_string.split(' ')[3].split('[')[1].split(':')[0].split('/')
        if int(date[2]) % 4 == 0:
            months["Feb"] = 29
            leap = True
        time = record_string.split(' ')[3].split('[')[1].split(':')
        time.pop(0)
        if not leap:
            ip_time = int(time[2]) + int(time[1])*60 + int(time[0])*60*24 + int(date[2])*31536000 + months[date[1]]*24*60*60 + int(date[0])*24*60*60
        else:
            ip_time = int(time[2]) + int(time[1])*60 + int(time[0])*60*24 + int(date[2])*31622400 + months[date[1]]*24*60*60 + int(date[0])*24*60*60
        if ip_time < all_ips[remote_addr][1] or all_ips[remote_addr][1] == 0:
            all_ips[remote_addr][1] = ip_time
        if ip_time > all_ips[remote_addr][2] or all_ips[remote_addr][2] == 0:
            all_ips[remote_addr][2] = ip_time
        status = record_string.split('"')[2].split(' ')[1]
        if status[0] == "4" or status[0] == "5":
            all_ips[remote_addr][4] += 1
        all_ips[remote_addr][0] += 1
    elif (not "GET" in record_string or "POST" in record_string) and not remote_addr in attackers_ips:
        attackers_ips.append(remote_addr)
file.close()
for ip, values in all_ips.items():
    if values[1] != values[2]:
        values[3] = values[0] / (values[2] - values[1])
    if values[4] > 0 and values[1] != values[2]:
        values[5] = values[4] / (values[2] - values[1])
    if values[3] > 2 and not ip in attackers_ips:
        attackers_ips.append(ip)
    if values[5] > 1 and not ip in attackers_ips:
        attackers_ips.append(ip)
file2 = open("output.txt", "w")
attackers_ips = [x for x in attackers_ips if x != '\n']
for i in attackers_ips:
    file2.write(i + '\n')
file = open("log.txt", "r")
while True:
    record_string = file.readline()
    if not record_string:
        break
    remote_addr = record_string.split(' ')[0]
    if remote_addr in attackers_ips:
        file2.write(record_string)
file.close()
file2.close()