# โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด

# ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ

# *** Election ***
# Enter a number of voter(s) : 10
# 6 8 13 9 8 1 16 19 4 20
# 8 


print("*** Election ***")

input("Enter a number of voter(s) : ")
lst = [int(i) for i in input().split(' ')]
candidate = [0] * 21
answer = [0]
for item in lst:
    if item > 0 and item <=20:
        candidate[item] += 1

max = 0
for i in range(1, 21) :
    if candidate[i] > max:
        answer = [i]
        max = candidate[i]
    elif candidate[i] == max:
        answer.append(i)

if max == 0:
    print("*** No Candidate Wins ***")
else :
    for item in answer:
        print(item, end=" ")
