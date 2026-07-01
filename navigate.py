# Projeto Way2Go: Movimento em plano 2D

import math

def calculate_velocity(target, current):
    dist_min = 0.1
    ang_min = 0.1
    ang_move = 0.3
    # k_v = 2.0
    # k_w = 1.5
    vx_max = 0.5
    w_max = 0.5

    vel = [0.0, 0.0]

    x_target = target[0]
    y_target = target[1]
    yaw_target = target[2]

    x_real = current[0]
    y_real = current[1]
    yaw_real = current[2]

    dx = x_target - x_real
    dy = y_target - y_real
    dist = (dx ** 2 + dy ** 2) ** 0.5
    ang = math.atan2(dy, dx)
    

    erro = ang - yaw_real

    if erro > 3.14:
        erro = erro - 6.28
    elif erro < -3.14:
        erro = erro + 6.28


    erro_final = yaw_target - yaw_real

    if erro_final > 3.14:
        erro_final = erro_final - 6.28
    elif erro_final < -3.14:
        erro_final = erro_final + 6.28


    vx = dist    # * k_v

    if vx > vx_max:
        vx = vx_max


    w = erro    # * k_w

    if w > w_max:
        w = w_max
    elif w < -w_max:
        w = -w_max


    w_final = erro_final

    if w_final > w_max:
        w_final = w_max
    elif w_final < -w_max:
        w_final = -w_max


    if dist < dist_min:
        vel[0] = 0.0

        if erro_final > ang_min or erro_final < -ang_min:
            vel[1] = w_final
        else:
            vel[1] = 0.0    

    elif erro > ang_move or erro < -ang_move:
        vel[0] = 0.0
        vel[1] = w
    else:
        vel[0] = vx
        vel[1] = w

    return vel


# target = (2.0, 0.0, 1.5)
# current = (0.0, 0.0, 0.0)

# vel = calculate_velocity(target, current)

# print(vel)