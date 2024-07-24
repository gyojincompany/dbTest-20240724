import pymysql  # mysql과 python을 연동시켜주는 라이브러리

# 파이썬과 mysql 서버 간의 커넥션 생성
# 1) 계정 : root(관리자 계정)
# 2) 비밀번호 : 12345
# 3) mysql이 설치된 컴퓨터의 ip 주소(본인 컴퓨터 localhost)
#  - 192.168.0.100(교수용 ip 주소)
# 4) 스키마 이름(데이터베이스 이름) - testdb

conn = pymysql.connect(host='localhost', user='root', password='12345', db='sakila')
# python과 mysql connection 생성

sql = 'SELECT * FROM film'  # 커넥션이 생성된 db에 실행할 sql문 생성

cur = conn.cursor()
cur.execute(sql)  # 커넥션이 생성된 db의 스키마에 지정된 sql문이 실행됨
records = cur.fetchall()  # sql문에서 실행된 결과를 받아옴(tuple 구조로 반환됨)

# print(records)
print(records[0])  # 레코드 1행
print(records[0][1])  # 1행 레코드의 영화 제목(title)

for record in records:
    print(record[1])


# 커넥션의 사용이 종료된 후에는 반드시 닫아줄 것!
# cursor 먼저 닫은 후에 conn을 닫아 줌
cur.close()
conn.close()