class RowReader:
    def fileRead(self,filepath):
        textfile = open('gpio_in.cfg', encoding='utf-8-sig')
        data = []
        for line in textfile:
            row_data = line.strip("\n").split(';')
            data.append(row_data)
        s=1
        with open("Output.txt", "w+", encoding='utf-8-sig') as text_file:
            for x in range(len(data)):
                if data[x][0] == '':
                    text_file.write(';')
                    text_file.write(data[x][1])
                    text_file.write('\n')
                elif len(data[x]) == 1 and data[x][0].startswith(('\t')):
                    text_file.write('\n')
                elif len(data[x]) == 1 or (len(data[x]) == 2 and data[x][1] == ''):
                    r=str(s)
                    name = ('Name#' + r + '=' + str(data[x][0]) + '\n')
                    unit = ('UNIT#'+ r + '=' + str(0) + '\n')
                    bit = ('BIT#' + r + '=' + str(0) + '\n')
                    inv = ('INV#' + r + '=' + str(0) + '\n')
                    text_file.write(name)
                    text_file.write(unit)
                    text_file.write(bit)
                    text_file.write(inv)
                    s+=1
                elif len(data[x]) == 3:
                    b = int(data[x][1])
                    e = int((b/10)%10)
                    a, c = data[x][0],  data[x][2]
                    r = str(s)
                    name1 = ('Name#'+ r + '=' + str(a) + '\n')
                    unit1 = ('UNIT#' + r + '=' + str(e) + '\n')
                    bit1 = ('BIT#' + r + '=' + str(c) + '\n')
                    inv1 = ('INV#' + r + '=' + str(0) + '\n')
                    text_file.write(name1)
                    text_file.write(unit1)
                    text_file.write(bit1)
                    text_file.write(inv1)
                    s+=1
file = RowReader()
file.fileRead("gpio_in.cfg")