import turtle

# Длина шага
step = 50
# Стартовая точка
posx, posy = -300, -300
# Начальный угол поворота
alpha = 90
# Угол поворота
theta = 180/8
# Аксиома
axiom = 'F'
# Порождающее правило
newrule = {'F': '-F+F+[+F-F-]-[-F+F+F]', 'X': '--FXF++FXF++FXF--'}

# Инициализация черепашки
pen = turtle.Turtle()
pen.shape('classic')
pen.speed('fastest')
pen.color("#3333FF")
pen.up()
pen.setpos(posx, posy)
pen.setheading(alpha)
pen.down()

def draw(rule, iters):
    # Изменяем размер шага, чтобы черепашка не вылезала за экран
    global step
    step /= (iters + 1)

    # Применяем порождающее правило ровно iters раз  
    for i in range(iters):
        rule = list(map(lambda x: newrule[x] if x in newrule else x, rule))
        rule = ''.join(rule)
        
    # Интерпретируем наше правило
    stack = []
    for word in rule:
        if word == 'F': # На F просто двигаемся вперед
            pen.forward(step)
        elif word == 'g': # На g отрываем от холста перо, шагаем вперед и опускаем перо
            pen.up()
            pen.forward(step)
            pen.down()
        elif word == '+': # На + поворачиваемся на theta градусов
            pen.left(theta)
        elif word == '-': # На - поворачиваемся на -theta градусов
            pen.right(theta)
        elif word == '[': # На начало ветвления запоминаем положение пера
            stack.append((*pen.pos(), pen.heading()))
        elif word == ']': # На конец ветвления восстанавливаем запомненное значение
            x, y, a = stack.pop()
            pen.up()
            pen.setpos(x, y)
            pen.setheading(a)
            pen.down()

# Отрисовка
turtle.tracer(0, 0)
draw(axiom, 5)
turtle.update()
turtle.done()
