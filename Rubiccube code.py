import numpy as np
import random

# 四元数クラスと回転操作は先ほどのコードを使用

class RubiksCube:
    def __init__(self):
        # 初期状態を定義
        self.state = {
            'U': np.array([['W']*3]*3),  # 上面 (White)
            'D': np.array([['Y']*3]*3),  # 下面 (Yellow)
            'F': np.array([['G']*3]*3),  # 前面 (Green)
            'B': np.array([['B']*3]*3),  # 背面 (Blue)
            'L': np.array([['O']*3]*3),  # 左面 (Orange)
            'R': np.array([['R']*3]*3)   # 右面 (Red)
        }
        self.move_history = []

    def rotate_face(self, face, clockwise=True):
        # 四元数で回転操作を行う
        axis_map = {
            'U': [0, 0, 1],
            'D': [0, 0, -1],
            'F': [0, 1, 0],
            'B': [0, -1, 0],
            'L': [-1, 0, 0],
            'R': [1, 0, 0]
        }
        
        axis = axis_map[face]
        angle = 90 if clockwise else -90
        q = quaternion_from_axis_angle(axis, angle)

        # 回転させる面の色を更新
        self.state[face] = np.rot90(self.state[face], -1 if clockwise else 1)
        # 操作を記録
        self.move_history.append((face, clockwise))

    def scramble(self, moves=20):
        faces = list(self.state.keys())
        for _ in range(moves):
            face = random.choice(faces)
            clockwise = random.choice([True, False])
            self.rotate_face(face, clockwise)

    def reset_to_initial(self):
        while self.move_history:
            face, clockwise = self.move_history.pop()
            # 逆の操作を適用
            self.rotate_face(face, not clockwise)

    def print_cube(self):
        # キューブの状態を表示
        for face, grid in self.state.items():
            print(f"{face} face:")
            print(grid)
            print()

# ルービックキューブのインスタンスを生成
cube = RubiksCube()

# ランダムな回転を適用してシャッフル
cube.scramble(moves=10)
print("Scrambled Cube:")
cube.print_cube()

# ランダム状態から初期状態に戻す
cube.reset_to_initial()
print("Restored Cube:")
cube.print_cube()