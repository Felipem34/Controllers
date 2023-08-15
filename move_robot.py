import turtle
import matplotlib.pyplot as plt

class Robo():
    def __init__(self, name = "Controle", speed = 0, disturbio = 0):
        '''Inicializa a instancia

            Args:
                name: nome dado a janela do 'turtle'
                speed: velocidade da instancia do 'turtle'
                        0 = velocidade máxima
                disturbio: disturbio no ângulo ao movimentar (em graus)
                            angulo final = rotação + disturbio
        '''
        # Configura a tela do turtle
        self.win = turtle.Screen()
        self.win.setup(0.4, 0.3)
        self.win.bgcolor('white')
        self.win.title(name)

        # Cria a linha vermelha de referência
        turtle.hideturtle()
        turtle.pensize(3)
        turtle.speed(0)
        turtle.color('red')
        turtle.goto(-800, 0)
        turtle.forward(1600)

        turtle.penup()
        turtle.goto(400,-36)
        turtle.write('y = 0', font=('Courier', 22, 'italic'), align='center')

        # Configura o robo
        self.robo = turtle.Turtle()
        self.robo.hideturtle()
        self.robo.pensize(4)
        self.robo.shape('arrow')
        self.robo.color('blue')
        self.robo.resizemode('user')
        #robo.shapesize(0.3, 0.3, 0.3)
        self.robo.speed(speed)

        # Coloca o robo na posição inicial
        self.robo.penup()
        self.robo.goto(-450, 50)
        self.robo.showturtle()
        self.robo.pendown()

        #Acompanha o angulodo robô
        self.angle = 0

        # Lista para plotar erro
        self.erro_list = []

        # Disturbio natural na medição da direção
        self.disturbio = disturbio

        self.counter = 1

    def getYPos(self):
        '''Retorna a posição Y do robô
        '''
        return self.robo.ycor()


    def move(self, turn, distance = 10):
        '''Move o robô em uma direção considerando
           a mudança no ângulo e a distância

           Args:
               turn: ângulo que o robô deve rotacionar para movimentar
               distance: distancia que o robô deve andar
        '''
        # Obtem o novo valor do ângulo considerando o
        # erro e o disturbio
        new_angle = turn + self.disturbio

        # Muda a direção e anda
        self.robo.forward(distance)

        if new_angle < 0:
            self.robo.right(abs(new_angle))
        else:
            self.robo.left(new_angle)

        self.angle += new_angle

        # Limita o movimento em +-45º
        if(self.angle > 45):
            self.angle = 45
            self.robo.setheading(45)
        elif(self.angle < -45):
            self.angle = -45
            self.robo.setheading(-45)

        # Adiciona o erro atual à lista
        self.erro_list.append(self.getYPos())


    def plotError(self):
        '''Plota a curva do erro em função dos passos
        '''
        plt.xlabel("Passos")
        plt.ylabel("Erro")
        plt.plot(self.erro_list)
        plt.title("Evolução do erro")
        plt.show()


    def end(self):
        turtle.done()
