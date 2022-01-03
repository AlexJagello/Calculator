import operator
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLCDNumber
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        for n in range(0, 10):
            setattr(self, 'btn_%s' % n, QPushButton('Button', self))
            getattr(self, 'btn_%s' % n).setText('%s' % n)
            getattr(self, 'btn_%s' % n).resize(50, 50)
            if n != 0:
                getattr(self, 'btn_%s' % n).move(10 + 60 * (n - 1) - 180 * int((n - 1) / 3),
                                                 70 + 60 * int((n - 1) / 3))
            getattr(self, 'btn_%s' % n).pressed.connect(lambda v=n: self.input_number(v))

        self.btn_0.move(10, 250)

        mass_of_name = ['btn_del', 'btn_add', 'btn_minus', 'btn_multiplication', 'btn_division']
        mass_of_text = ['del', '+', '-', '*', '/']
        for n in range(0, 5):
            setattr(self, mass_of_name[n], QPushButton('Button', self))
            getattr(self, mass_of_name[n]).setText(mass_of_text[n])
            getattr(self, mass_of_name[n]).resize(50, 50)
            getattr(self, mass_of_name[n]).move(200, 10 + 60 * n)
        self.btn_del.pressed.connect(self.delete)
        self.btn_add.pressed.connect(lambda: self.operation(operator.add))
        self.btn_minus.pressed.connect(lambda: self.operation(operator.sub))
        self.btn_multiplication.pressed.connect(lambda: self.operation(operator.mul))
        self.btn_division.pressed.connect(lambda: self.operation(operator.truediv))

        self.btn_equal = QPushButton('Button', self)
        self.btn_equal.setText('=')
        self.btn_equal.resize(110, 50)
        self.btn_equal.move(70, 250)
        self.btn_equal.pressed.connect(self.equals)

        self.text_editor = QLCDNumber(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Example')

        self.text_editor.resize(170, 50)
        f = self.text_editor.font()
        f.setPointSize(18)  # sets the size to 27
        self.text_editor.setFont(f)
        self.text_editor.move(10, 10)

        self.reset()
        self.show()

    def display(self):
        self.text_editor.display(self.stack[-1])

    def reset(self):
        self.stack = [0]
        self.stack_op = [operator.add]

    def input_number(self, v):
        self.stack[-1] = self.stack[-1] * 10 + v
        self.display()

    def delete(self):
        self.stack[-1] = int(self.stack[-1]/10)
        self.display()

    def operation(self, op):
        self.stack_op.append(op)
        self.stack.append(0)
        self.display()

    def equals(self):
        s = 0
        for i in range(0, self.stack.__len__()):
            s = self.stack_op[i](s, self.stack[i])
        self.stack.clear()
        self.reset()
        self.stack[-1] = s
        self.display()

