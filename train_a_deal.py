import csv

filename = 'D:\\Federal-Learning\\dataset\\train_a_label.csv'
data = []
zhapian_data = []

def read_write_csv():
    with open(filename) as read_csv:
        csv_reader = csv.reader(read_csv)  # 使用csv.reader读取csvfile中的文件
        # header = next(csv_reader)        # 读取第一行每一列的标题
        for row in csv_reader:  # 将csv 文件中的数据保存到data中
            l = len(row)
            if(row[l - 1] == '0'):
                data.append(row)
        read_csv.close()


    with open("D:\\Federal-Learning\\dataset\\train_a_nozhapian.csv","w", newline='') as write_csv:
        writer = csv.writer(write_csv)
        for row in data:
            writer.writerow(row)

        write_csv.close()

if __name__ == '__main__':
    rw = read_write_csv()