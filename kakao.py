

def keyboard():
    base = '''
    <?php
    echo \'
        {
            "type": "buttons",
            "buttons": []
        }\';
    ?>
    '''
    print("\n버튼 설정하기\n")
    count = input("추가할 버튼 개수를 입력하세요 >> ")
    count = int(count)
    button = [input("%s 번째 버튼이름 설정 >> " % (n+1)) for n in range(count)]
    print("\n")

    f = open("keyboard.php",'w')


print("kakaotalk chatbot maker by python")
print("이 스크립트는 php를 이용합니다. 숙지하시길\n")

print("1.버튼 생성하기")
print("2.메시지 설정하기")

cho = input("선택 >> ")

if cho == "1":
    keyboard()

'''
<?php
echo '
    {
        "type": "buttons",
        "buttons": ["사용법","급식"]
    }';
?>
'''
