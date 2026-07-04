# Projeto Way2Go: Movimento em plano 2D

import math

def calculate_velocity(target, current):
    dist_min = 0.1
    ang_min = 0.1
    ang_move = 0.3
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
    if erro > math.pi:
        erro = erro - 2 * math.pi
    elif erro < -math.pi:
        erro = erro + 2 * math.pi

    erro_final = yaw_target - yaw_real
    if erro_final > math.pi:
        erro_final = erro_final - 2 * math.pi
    elif erro_final < -math.pi:
        erro_final = erro_final + 2 * math.pi

    vx = dist
    if vx > vx_max:
        vx = vx_max

    w = erro
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


def simulate(target, start, dt=0.1, max_steps=300):
    x, y, yaw = start

    print(f"{'Passo':>6} | {'Tempo (s)':>9} | {'x':>7} | {'y':>7} | {'yaw (rad)':>10} | {'vx':>6} | {'w':>6}")
    print("-" * 70)

    for step in range(max_steps):
        vel = calculate_velocity(target, (x, y, yaw))
        vx, w = vel

        if step % 10 == 0:
            t = step * dt
            print(f"{step:6d} | {t:9.2f} | {x:7.3f} | {y:7.3f} | {yaw:10.3f} | {vx:6.3f} | {w:6.3f}")

        x += vx * math.cos(yaw) * dt
        y += vx * math.sin(yaw) * dt
        yaw += w * dt

        while yaw > math.pi:
            yaw -= 2 * math.pi
        while yaw < -math.pi:
            yaw += 2 * math.pi

        dx = target[0] - x
        dy = target[1] - y
        dist = math.sqrt(dx**2 + dy**2)
        yaw_err = target[2] - yaw
        if dist < 0.1 and abs(yaw_err) < 0.1:
            print("-" * 70)
            print(f"{step:6d} | {step*dt:9.2f} | {x:7.3f} | {y:7.3f} | {yaw:10.3f} | {vx:6.3f} | {w:6.3f}  <- chegou!")
            break

    print(f"\nEstado final: x={x:.3f}, y={y:.3f}, yaw={yaw:.3f} rad")
    print(f"Alvo:         x={target[0]:.3f}, y={target[1]:.3f}, yaw={target[2]:.3f} rad")


target = (5.0, 2.0, 3.0)
current = (0.0, 0.0, 0.0)

simulate(target, current)