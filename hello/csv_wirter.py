import csv

with open('test.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['a', 'b', 'c', 'd'])
    csv_writer.writerow(['a', 'b', 'h', 'c'])

print('finish')