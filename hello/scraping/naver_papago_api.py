from scraping.translate_papago import translate_with_papago


def main():
    text_list = []

    with open('sub.txt','r') as sub_file:
        text_list = sub_file.readlines()
    with open('sub.txt'+'.translated', 'w') as translated_file:
        for line in text_list:
            translated = translate_with_papago(line)
            translated_file.write(line)
            translated_file.write(translated + '\n')

    print(len(text_list), '라인이 번역 완료 되었습니다.')


if __name__ == '__main__':
    main()



