import argparse

from style import Style,TreeStyle, RectangleStyle
from visitor import IVisitor, Visitor

def main():


    # 创建style对象
    style_td = TreeStyle("test.json", "default")
    style_tp = TreeStyle("test.json", "pokerface")
    style_rd = RectangleStyle("test.json", "default")
    style_rp = RectangleStyle("test.json", "pokerface")

    #将这些对象放入列表中
    styles = [style_td, style_tp, style_rd, style_rp]

    # 创建迭代器
    iterator = iter(styles)

    visitor = Visitor()

    while True:
        try:
            style = next(iterator)
            style.accept(visitor)
        except StopIteration:
            break


    '''
    factory = Factory()
    style_tp = factory.create("test.json", "tree", "pokerface")
    style_td = factory.create("test.json", "tree", "default")
    style_rp = factory.create("test.json", "rectangle", "pokerface")
    style_rd = factory.create("test.json", "rectangle", "default")

    #将这些对象放入列表中
    styles = [style_tp, style_td, style_rp, style_rd]
    
    # 创建迭代器
    iterator = iter(styles)
    
    while True:
        try:
            style = next(iterator)
            style.show()  
        except StopIteration:
            break
'''


if __name__ == "__main__":
    main()
