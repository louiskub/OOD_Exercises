# รับ input 1 บรรทัด โดย แต่ละลำดับ จะมีอักษรกำกับไว้และตามด้วยจำนวนครั้งที่ต้องทำตามตัวอักษรนั้น E คือ การ enqueue และ D คือการ dequeue แต่หากเป็นตัวอักษรอื่นให้นับเป็น error input

# ต้องบอกว่า มีการ dequeue ที่ไม่เกิดผลกี่ครั้งตามลำดับ และแต่ละครั้งที่มีการเกิดขึ้นใน Queue มีการเปลี่ยนแปลงอย่างไรตามขั้นตอน



texts = input('input : ').split(',')
q = []
err_input = 0
err_deq = 0
deq_add = 0
for text in texts:
    print(f"Step : {text}")
    if text[0] not in 'DE' or text[1] not in '0123456789':
        err_input += 1
        print(f"{q}")

    elif text[0] == 'D':
        for k in range(int(text[1])):
            if len(q) == 0:
                err_deq += 1
            else :
                q.pop(0)
        print(f"Dequeue : {q}")
    elif text[0] == 'E':
        # print(text)
        for k in range (deq_add, deq_add + int(text[1:])):
            q.append('*'+ str(deq_add))
            deq_add += 1

        print(f"Enqueue : {q}")
    
    print(f"Error Dequeue : {err_deq}")
    print(f"Error input : {err_input}")
    print("--------------------")
            # j+=1
        # print(text, j)

# print(q, err_deq, err_input)
