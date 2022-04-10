#파이썬 dictionary을 이용한 json 파일 다루기

#내가 원하는 데이터 딕셔너리 형태로 만들기
info = {
    'Korean_Dish' : {
        "김치" : '1',
        "삼겹살" : '2',
        "된장찌개" : '3'
    }
    ,
    'Japanese_Dish' : {
        "초밥" : '4',
        "사시미" : '5',
        "나베" : '6'
    }
}
print(info)

import json

#2.dictionary 자료 저장 및 읽기

#_data.json 파일에 딕셔너리 형태로 info 저장
with open("testdata.json", 'w') as f:
    json.dump(info, f, indent='\t')
    
#저장 된 _data.json 파일을 읽어오기.
with open('testdata.json', 'r') as f:
    data = json.load(f)
    
#json.dumps 이용해서 data를 들여쓰기 4칸, 한글로 표현되도록 출력




#dictionary 데이터 추가 및 반영 (update)
print(json.dumps(data, indent=4,ensure_ascii=False))

Europian = {
    'Europian_Dish' : {
        "파스타" : 7,
        "스테이크" : 8,
        "스튜" : 9
    }
}

data.update(Europian)
print(json.dumps(data, indent =4 , ensure_ascii=False))


#Update 된 json파일 저장 및 읽어오기 

with open("testdata.json",'w',encoding='utf-8') as f:
    json.dump(data,f,indent='\t')
    
with open("testdata.json",'r',encoding='utf-8') as f:
    f= f.read()
    my_data = json.loads(f)

print(json.dumps(my_data,indent=4,ensure_ascii=False))