class Tool:
    # 使用赋值语句定义类属性，记录所有工具对象的数量

    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool('锤子')
tool2 = Tool('斧头')

# 2.输出工具对象的总数

# 访问类属性：类名.类属性
print(Tool.count)
