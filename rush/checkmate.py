"""ไฟล์หลักสำหรับตรวจจับการ Checkmate"""

def checkmate(board):
    # ตรวจว่าค่าที่ส่งมาจาก main.py (board) เป็น String มั้ย ถ้าไม่ใช่จะ Error
    if not isinstance(board, str):
        print("Error")
        return

    # แยก String ที่รับมาเป็นแต่ละแถวเก็บไว้ใน lines
    lines = board.split('\n')
    n = len(lines)
    if n == 0:
        print("Error")
        return
    
    # ตรวจว่ากระดานใน main.py เป็นสี่เหลี่ยมจัตุรัสมั้ย ถ้าไม่ใช่จะ Error
    for line in lines:
        if len(line) != n:
            print("Error")
            return

    # ค้นหาตำแหน่งของ King (K) (kr = King Row, kc = King Column)
    kr, kc = -1, -1
    k_count = 0
    for r in range(n):
        for c in range(n):
            if lines[r][c] == 'K':
                kr = r
                kc = c
                k_count += 1

    # ต้องมี King แค่ 1 ตัวเท่านั้นบนกระดาน ถ้าไม่ใช่จะ Error
    if k_count != 1:
        print("Error")
        return

    # รายชื่อตัวหมากทั้งหมด
    pieces = ['K', 'P', 'B', 'R', 'Q']

    # ตรวจสอบแนวตรงทางซ้าย, ขวา, บน, ล่าง สำหรับ Rook และ Queen (r = Row, c = Column, p = pieces)
    for row_step, col_step in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = kr + row_step, kc + col_step
        while 0 <= r < n and 0 <= c < n:
            p = lines[r][c]
            if p in ['R', 'Q']:
                print("Success")
                return
            if p in pieces:  # ถ้าเจอหมากตัวอื่นที่กินแนวตรงไม่ได้จะถือว่าโดนบังทาง
                break
            # ถ้าเป็นตัวอักษรอื่นจะถือว่าเป็นช่องว่าง ให้ข้ามไปเช็คช่องต่อไป
            r += row_step
            c += col_step

    # ตรวจสอบแนวทแยง 4 มุม สำหรับ Bishop, Queen และ Pawn
    for row_step, col_step in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = kr + row_step, kc + col_step
        step = 1
        while 0 <= r < n and 0 <= c < n:
            p = lines[r][c]
            if p in ['B', 'Q']:
                print("Success")
                return
            # Pawn กินได้เฉพาะแนวทแยงมุมด้านหน้า 1 ช่องเท่านั้น (row_step == 1 คือ Pawn อยู่แถวด้านล่างของ K แล้วมองขึ้นมากิน)
            if p == 'P' and row_step == 1 and step == 1:
                print("Success")
                return
            if p in pieces: # ถ้าเจอหมากตัวอื่นที่กินแนวทแยงไม่ได้จะถือว่าโดนบังทาง
                break
            # ขยับพิกัดการมองไปตามก้าวที่กำหนด
            r += row_step
            c += col_step
            step += 1
            
    # ถ้ารอดจากรัศมีการกินทั้งหมดแสดงว่า K ปลอดภัยโดยจะขึ้นว่า Fail
    print("Fail")
