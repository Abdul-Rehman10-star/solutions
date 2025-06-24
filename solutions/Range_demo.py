# # for i in range(5):
# #     print(i)
# for i in range(5, 8):
#     print(i)
# for i in range(5, -12, -2):
#     print(i)

# for i in range(5):
#     for j in range(5):
#         print(i, j)
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()