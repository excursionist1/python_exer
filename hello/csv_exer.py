import csv


list = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
]

new_list = []
for item in list:
    del item[3]
    new_list.append(item)

def main():
    file_name = './baseballdatabank-master/core/park.csv'


    with open('file_name', 'w', encoding='utf-8') as read_file:
        csv_reader = csv.reader(read_file)
        park_list = list(csv_reader)

    new_list = remove_col(['state'])

    with open('file_name', + '.new.csv', 'w', encoding='utf-8', newline='') as write_file:
        csv_writer = csv.writer(write_file)
        for list in new_list:
            csv_writer.writerow(list)


if __name__ == '__main__':
    main()
