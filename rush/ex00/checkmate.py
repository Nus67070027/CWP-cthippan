def checkmate(board):

    # ตรวจสอบว่าข้อมูลที่รับมาเป็น String หรือไม่
    if not isinstance(board, str):
        print("Error")
        return

    # แยกกระดานออกเป็นแต่ละแถว
    board_rows = board.split("\n")
    board_size = len(board_rows)

    if board_size == 0:
        print("Error")
        return

    # ตรวจสอบว่ากระดานเป็นสี่เหลี่ยมจัตุรัสหรือไม่
    for row in board_rows:
        if len(row) != board_size:
            print("Error")
            return

    # ค้นหาตำแหน่งของ King
    king_row = -1
    king_col = -1
    king_count = 0

    for row in range(board_size):
        for col in range(board_size):
            if board_rows[row][col] == "K":
                king_row = row
                king_col = col
                king_count += 1

    # ต้องมี King เพียง 1 ตัว
    if king_count != 1:
        print("Error")
        return

    # รายชื่อตัวหมากทั้งหมด
    chess_pieces = ["K", "P", "B", "R", "Q"]

    # ตรวจสอบแนวตรง (บน ล่าง ซ้าย ขวา)
    # สำหรับ Rook และ Queen
    straight_directions = [
        (-1, 0),  # บน
        (1, 0),   # ล่าง
        (0, -1),  # ซ้าย
        (0, 1)    # ขวา
    ]

    for row_direction, col_direction in straight_directions:

        current_row = king_row + row_direction
        current_col = king_col + col_direction

        while (
            0 <= current_row < board_size
            and 0 <= current_col < board_size
        ):

            current_piece = board_rows[current_row][current_col]

            # Rook หรือ Queen สามารถกิน King ได้
            if current_piece in ["R", "Q"]:
                print("Success")
                return

            # เจอหมากตัวอื่นบังทาง
            if current_piece in chess_pieces:
                break

            current_row += row_direction
            current_col += col_direction

    # ตรวจสอบแนวทแยง
    # สำหรับ Bishop, Queen และ Pawn
    diagonal_directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for row_direction, col_direction in diagonal_directions:

        current_row = king_row + row_direction
        current_col = king_col + col_direction
        distance = 1

        while (
            0 <= current_row < board_size
            and 0 <= current_col < board_size
        ):

            current_piece = board_rows[current_row][current_col]

            # Bishop หรือ Queen สามารถกิน King ได้
            if current_piece in ["B", "Q"]:
                print("Success")
                return

            # Pawn กินได้เฉพาะแนวทแยงด้านหน้า 1 ช่อง
            if (
                current_piece == "P"
                and row_direction == 1
                and distance == 1
            ):
                print("Success")
                return

            # เจอหมากตัวอื่นบังทาง
            if current_piece in chess_pieces:
                break

            current_row += row_direction
            current_col += col_direction
            distance += 1

    # ถ้าไม่มีตัวไหนกิน King ได้
    print("Fail")