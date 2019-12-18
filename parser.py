import csv

with open(file="input.txt", mode='rt', encoding='UTF8') as fr:
    with open(file="output.csv", mode='w', encoding='utf-8', newline='') as fw:
        wr = csv.writer(fw)
        flag = 0
        line_write = []
        while True:
            line_read = fr.readline()
            if line_read == "":
                break
            line_read = line_read.split()
            if len(line_read) == 0:
                continue
            elif line_read[0] == "average":
                line_write.append(line_read[-1])
            elif line_read[0] == "CPU" or line_read[0] == "ACTIVE":
                line_write.append(line_read[-3])
                line_write.append(line_read[-1])
            elif line_read[0] == "utilization:":
                line_write.append(line_read[-1])
                flag += 1
                if flag == 5:
                    wr.writerow(line_write)
                    flag = 0
                    line_write.clear()



