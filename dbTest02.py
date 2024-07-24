import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345', db='pydata')

# sql = "INSERT INTO membertbl VALUES ('tiger88','김팔팔','tiger88@abc.com')"
# tiger 회원을 찾아서 회원이름을 김호랑으로 변경하시오
# sql = "UPDATE membertbl SET membername='김호랑' WHERE memberid='tiger'"
# tiger11 회원을 찾아서 레코드를 삭제하시오
sql = "DELETE FROM membertbl WHERE memberid='tiger11'"

cur = conn.cursor()
success = cur.execute(sql)  # sql 실행->성공 1을 반환

if success == 1:
    print("회원 탈퇴 성공!!")
else:
    print("회원 탈퇴 실패!!")

cur.close()
conn.commit()  # insert, update, delete 문을 사용한 경우 반드시 commit 이 호출되야함
conn.close()

