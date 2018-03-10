

def keyboard():
    base = '''
    <?php
    echo \'
        {
            "type": "buttons",
            "buttons": [%s]
        }\';
    ?>
    '''
    print("\n    / 버튼 설정하기 /\n")
    print(" 사용자가 채팅방에 들어왔을 때, \n    하단에 보여질 버튼의 문구를 입력해주세요.")
    print(" * 끝내려면 빈칸으로 남겨두고 엔터를 쳐주세요.", end="\n\n")
    
    _Ubutts = []
    
    while True:
    	inp = input("  > ")
    	
    	if inp: _Ubutts.append(inp)
    	else: break
    
    print("{}개의 값을 입력받았습니다.".format(len(_Ubutts)))
    print(", ".join(_Ubutts))
    
    base = base % ( ", ".join(_Ubutts) )
    
    f = open("keyboard.php",'w', encoding="UTF-8")\
        .write(base)


print("kakaotalk chatbot maker by python")
print("이 스크립트는 php를 이용합니다. 숙지하시길\n")

print("1.버튼 생성하기")
print("2.메시지 설정하기")

cho = input("선택 >> ")

if cho == "1":
    keyboard()

