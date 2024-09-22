import random

# ルービックキューブの6つの面に対応する色を定義（簡略化）
faces = ['U', 'D', 'F', 'B', 'L', 'R']

# ランダムな操作を生成
def generate_random_moves(n=2000):
    moves = []
    for _ in range(n):
        face = random.choice(faces)
        direction = random.choice(["", "'", "2"])  # 何もなし、逆回り、180度回転
        moves.append(face + direction)
    return moves

# キューブの状態を表現するシンプルな関数
def apply_moves(cube, moves):
    # ここではキューブの状態は文字列でシンプルに表現
    for move in moves:
        # 操作を適用する
        cube = f"{cube} -> {move}"
    return cube

# キューブを初期状態に戻すための逆操作を生成
def reverse_moves(moves):
    reversed_moves = []
    for move in moves[::-1]:
        if "'" in move:
            reversed_moves.append(move.replace("'", ""))
        elif "2" in move:
            reversed_moves.append(move)
        else:
            reversed_moves.append(move + "'")
    return reversed_moves

# 暗号化操作
def encrypt(data, key_moves):
    encrypted_data = apply_moves(data, key_moves)
    return encrypted_data

# 復号操作
def decrypt(encrypted_data, key_moves):
    reversed_moves = reverse_moves(key_moves)
    decrypted_data = apply_moves(encrypted_data, reversed_moves)
    return decrypted_data

# 実行例
data = "Initial Cube State"
key_moves = generate_random_moves(5)
print("Key Moves:", key_moves)

# データを暗号化
encrypted = encrypt(data, key_moves)
print("Encrypted:", encrypted)

# データを復号化
decrypted = decrypt(encrypted, key_moves)
print("Decrypted:", decrypted)