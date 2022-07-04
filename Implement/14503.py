import sys

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
DIRTY = 0
WALL = 1
CLEAN = 2
'''
방향
  0
3   1
  2
'''
class Robot:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def forward(self):
        if self.d == NORTH:
            self.y -= 1
        elif self.d == EAST:
            self.x += 1
        elif self.d == SOUTH:
            self.y += 1
        elif self.d== WEST:
            self.x -= 1

    def backward(self):
        if self.d == NORTH:
            self.y += 1
        elif self.d == EAST:
            self.x -= 1
        elif self.d == SOUTH:
            self.y -= 1
        elif self.d == WEST:
            self.x += 1

    def left_rotate(self):
        if self.d == NORTH:
            self.d = WEST
        elif self.d == WEST:
            self.d = SOUTH
        elif self.d == SOUTH:
            self.d = EAST
        elif self.d == EAST:
            self.d = NORTH

    def right_rotate(self):
        if self.d == NORTH:
            self.d = EAST
        elif self.d == EAST:
            self.d = SOUTH
        elif self.d == SOUTH:
            self.d = WEST
        elif self.d == WEST:
            self.d = NORTH

    def front(self):
        if self.d == NORTH:
            return self.x, self.y-1
        elif self.d == EAST:
            return self.x+1, self.y
        elif self.d == SOUTH:
            return self.x, self.y+1
        elif self.d == WEST:
            return self.x-1, self.y

    def back(self):
        if self.d == NORTH:
            return self.x, self.y+1
        elif self.d == EAST:
            return self.x-1, self.y
        elif self.d == SOUTH:
            return self.x, self.y-1
        elif self.d == WEST:
            return self.x+1, self.y


n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

house = []
robot = Robot(c, r, d)

# house 입력
for _ in range(n):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    house.append(tmp_list)

result = 0
while True:
    # 현재 위치 청소: 1
    if house[robot.y][robot.x] == DIRTY:

        house[robot.y][robot.x] = CLEAN
        result += 1

    # 현재 위치에서 다음을 반복
    cnt = 0
    for i in range(4):
        # 현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면
        robot.left_rotate()
        x, y = robot.front()
        if house[y][x] == DIRTY:
            robot.forward()
            break
        else:
            cnt += 1

    if cnt == 4:
        x, y = robot.back()
        if house[y][x] == WALL:
            break
        else:
            robot.backward()

print(result)
