import move_robot

# 1º teste - Sem disturbio
robo = move_robot.Robo("Controle PID")
# 2º teste - Disturbio de 10º
robo = move_robot.Robo("Controle PID", disturbio = 10)

GANHO_P = 0.5
GANHO_D = 2 #1.8
GANHO_I = 0.01

erro = 0
erro_acumulado = 0

STEPS = 120
for i in range(STEPS):
    erro_diferenca = robo.getYPos() - erro
    erro = robo.getYPos()
    erro_acumulado += erro
   
    controle = - erro * GANHO_P \
               - erro_diferenca * GANHO_D\
               - erro_acumulado * GANHO_I

    robo.move(controle)

# robo.plotError()
robo.end()