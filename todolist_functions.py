from pymongo import MongoClient

def Connect_Mongo(collection_name):
    mongoClient = MongoClient("mongodb://localhost:27017")    # mongodb 접속
    database = mongoClient["local"]   # database 연결
    return database[collection_name]        # collection 작업

# 데이터 입력 function
def Data_insert(collection, data):
    # 데이터 입력 전 초기화
    collection.delete_many({})
    collection.delete_many({})
    # 데이터 입력
    collection.insert_many(data)           # hint - insert_one -> insert_many

# 사용자 이름 입력 function
def User_name(collection):
    #사용자 이름 입력 후 db 저장
    user_name = input("Input Your Name: ")
    print("")
    result_participants = collection.insert_one({"user_name" : user_name})
    inserted_participants_id = result_participants.inserted_id

    # 사용자 id를 return
    return inserted_participants_id

# 업무 보고 입력 function
def Todos(user_id, collection1, collection2):
    print("ToDo List 중 하나 선택 하세요 !")

    # todos_list 컬렉션의 내용 중 'title'만 print
    result_todo = collection1.find({})           # hint -  user_id -> collection1
    count = 1
    for i in result_todo:
        print("{}. {}".format(count, i["title"]), end=", ")           # hint - {} 하나 삭제, end=", "로 변경
        count+= 1           # hint - 3 -> 1
    print("")

    # todo중 하나 입력
    user_input = int(input("Title 번호: "))-1           # hint - int() 캐스팅
    # Status 입력
    user_status = input("Status: ")           # hint - int() 삭제

    # 사용자가 입력한 번호에 해당하는 title과 그 title id를 찾음
    result_todo_title = collection1.find().skip(user_input).limit(1)
    for j in result_todo_title:
        inserted_todo = j['title']
        inserted_todo_id = j['_id']
        
    # user_id, 사용자가 입력한 title과 그 title id, 사용자가 입력한 status를 collection2에 담기
    collection2.insert_one({"user_id" : user_id, "user_todo_id" : inserted_todo_id, "todo_title" : inserted_todo, "user_status" : user_status})

# 종료 여부 입력 function
def End(collection, collection1, collection2):           # hint - collection 추가
    user_end = 'q'           # hint - 'x'->'q'
    while True:
        # c 입력 시 Todos() 다시 실행
        if user_end == "c":
            print("")
            Todos(user_id, collection1, collection2)
        # q 입력 시 User_name() 실행 후 Todos() 다시 실행
        elif user_end == "q":
            print("")
            print("------------------------")
            user_id = User_name(collection)
            Todos(user_id, collection1, collection2)
        # x 입력 시 프로그램 종료
        else:
            break

        print("c, q, x 중 하나를 입력하세요.")
        user_end = input("진행 여부: ")

    print("------------------------")
    print("프로그램이 종료되었습니다.")

if __name__ =="__main__":
    def Connect_Mongo(collection_name):
        mongoClient = MongoClient("mongodb://mongodb:27017")    # mongodb 접속
        database = mongoClient["local"]   # database 연결
        return database[collection_name]        # collection 작업
    todo_list = [
    {"title": "주간 보고서 작성", "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."},
    {"title": "이메일 확인 및 응답", "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."},
    {"title": "회의 준비", "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."},
    {"title": "프로젝트 계획서 수정", "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."},
    {"title": "팀 멤버와의 1:1 면담", "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."},
  ] 
    def Data_insert(collection, data):
        # 데이터 입력 전 초기화
        collection.delete_many({})
        collection.delete_many({})
        # 데이터 입력
        collection.insert_many(data)           # hint - insert_one -> insert_many
    collection_todos = Connect_Mongo("todos_list") 
    Data_insert(collection=collection_todos, data=todo_list)