# # This is a sample Python script.
#     # loss = (WX + b -y)**2
#     totalError = 0
#     for i in range(0,len(points)):
#         x = points[i,0]
#         y = points[i,1]
#         totalError += (y - (w * x + b)) ** 2
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# # Time:6：28
# # author:Li
#
# def compute_error_for_line_given_points(b,w,points):
#     return totalError / float(len(points))
#
# def step_gradient(b_current,w_current,points,learningRate):
#     # 下降：L对w、L对b求偏导数
#     b_gradient = 0
#     w_gradient = 0
#     N = float(len(points))
#     for i in range(len(points)):
#         x = points[i,0]
#         y = points[i,1]
#         b_gradient += -(2/N) * (y - ((w_current * x) + b_current))
#         w_gradient += -(2/N) * x * (y - ((w_current * x) + b_current))
#     new_b = b_current - (learningRate * b_gradient)
#     new_m = w_current - (learningRate * w_gradient)
#     return [new_b,new_m]
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
import torch
# 也可以是 device = torch.device('cuda:0')
import torch
print(torch.__version__)
print(torch.cuda.is_available())

