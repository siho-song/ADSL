import json


#_data.json 파일에 딕셔너리 형태로 info 저장
with open("testdata.json", 'w') as f:
    json.dump(info, f, indent='\t')
    
#저장 된 _data.json 파일을 읽어오기.
with open('testdata.json', 'r') as f:
    data = json.load(f)
    
#json.dumps 이용해서 data를 들여쓰기 4칸, 한글로 표현되도록 출력

print(json.dumps(data, indent=4,ensure_ascii=False))
