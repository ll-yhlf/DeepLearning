import torch

u = torch.tensor([3.0,-4.0])
print(torch.abs(u).sum())
# print(torch.norm(u)) #平方和，再开方


# #矩阵乘法!!!!
# x=torch.arange(12).reshape((4,3))
# y=torch.arange(3)
# print(x)
# print(y)
# print(x.shape,y.shape,torch.mv(x,y)) #torch.mv()只适用于二维乘一维
#
# b=torch.arange(15).reshape((5,3))
# c=torch.arange(12).reshape((3,4))
# print(b.shape,c.shape,torch.mm(b,c))


# a = torch.arange(20).reshape((4,5))
# a_sum_axis0 = a.sum(axis=0,keepdims=True)
# axis=0,按照第0维度进行求和操作
# keepdims：保存现有维度
# a_sum_axis1 = a.sum(axis=1,keepdims=True)
# print(a,a_sum_axis0,a_sum_axis0.shape,a_sum_axis1,a_sum_axis1.shape)


# a = torch.arange(12).reshape((3,4))
# print(a)
# print(a.T)
# #矩阵的转置操纵
# b=a.clone()
# clone可以理解为深拷贝
# print(a*b)



#
# X = torch.arange(12)
# a=X.numpy()
# b=torch.tensor(a)
# print(type(a),type(b))

#c=torch.tensor([3.99])
#print(c,c.item(),float(c),int(c))
#torch数据类型的item方法是得到只有一个元素张量里面的元素值

# x=torch.arange(3).reshape((3,1))
# print(x)
# y=torch.arange(2).reshape((1,2))
# print(y)
# print(x+y)
# 此情况下会触发广播机制


# x = torch.arange(12, dtype=torch.float32).reshape((3,4))
# #print(x)
# y= torch.tensor([[2.0,1,3,4],[1,2,3,4],[4,3,2,1]])
# print(y.sum())#对张量y中的元素进行求和操作
# print(x==y)#判断x与y中的每个元素是否相等
# print(torch.cat((x,y),dim=0))#dim=0，原样式合并
# print(torch.cat((x,y),dim=1))#dim=1，按一维合并，即按照行进行拼接，把每一行的元素合起来

# x=torch.tensor([1.2,3,5,7])
#
# y=torch.tensor([2,4.3,5,9])
#
# print(x+y)
# print(x-y)
# print(x/y)
# print(x*y)
# print(x**y)   x的y次方
#print(torch.exp(x))  #e的x次方