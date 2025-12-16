# pylint: disable=missing-docstring


def sudoku_validator(grid):
    """
Verilen 9x9 Sudoku grid'inin geçerli olup olmadığını kontrol eder.
    """
    def is_valid_unit(unit):
        """Bir listenin içinde 1-9 arası sayıların tam olup olmadığına bakar."""
        return sorted(unit) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Alternatif: return set(unit) == set(range(1, 10))

# --- 2. Satırları (Rows) Kontrol Et ---
    for row in grid:
        if not is_valid_unit(row):
            return False

    # --- 3. Sütunları (Columns) Kontrol Et ---
    # 0'dan 8'e kadar her sütun indeksi için dönüyoruz
    for col_index in range(9):
        column = []
        for row in grid:
            column.append(row[col_index])
        
        if not is_valid_unit(column):
            return False

    # --- 4. 3x3 Kutuları (Boxes) Kontrol Et ---
    # Adım adım 0, 3, 6 diye atlayarak karelerin başlangıç noktalarına gidiyoruz
    for i in range(0, 9, 3): # Satır başlangıcı (0, 3, 6)
        for j in range(0, 9, 3): # Sütun başlangıcı (0, 3, 6)
            
            box = []
            # O başlangıç noktasından itibaren 3x3'lük alanı tarıyoruz
            for x in range(3):
                for y in range(3):
                    val = grid[i + x][j + y]
                    box.append(val)
            
            if not is_valid_unit(box):
                return False

    # Eğer buraya kadar geldiyse her şey doğrudur!
    return True
