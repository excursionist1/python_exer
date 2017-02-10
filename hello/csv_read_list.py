    import csv
    import pprint

    def main():
        file_name = './baseballdatabank-master/core/AllstarFull.csv'

    try:
        with open(file_name,'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            allstar_dict = list(reader)

    except FileNotFoundError as f:
        print('파일이 없거나 이름이 잘못되었습니다.')
    except Exception as err:
        print('알수없는 오류', err)


    pprint.pprint(allstar_dict)

main()