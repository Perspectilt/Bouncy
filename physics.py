"""Module containing physics related functions"""

import math
import os.path
import time
import pygame


# Adds force (vector) to an object
def addforce(object, name, magnitude, direction):
    c = True

    # Check if same force vector exists
    for i in object.forces:
        if i['name'] == name.lower():
            c = False
            break

    if c and magnitude:
        object.forces += [{'name': name.lower(), 'magnitude': math.fabs(float(magnitude)), 'direction': float(direction)}]


# Removes force by name from an object
def removeforce(object, name):
    for i in object.forces:
        if i['name'] == name.lower():       # Checks if same force vector exists
            object.forces.remove(i)


# Applies gravity to all objects
def apply_gravity(objects, p_factor=1):
    for i in objects:
        addforce(i, 'gravity', p_factor * 9.8, -90)


# Main physics handle:-

T, t, xvector, yvector, u_x, u_y, n, s0x, s0y, condition, s_x, s_y = 0, 0, 0, 0, 0, 0, 1, 0, 0, True, 0, 0


# To add the laws of physics (very basic stuff for now -- limited to 1 object and 1 boundary only)
def physics(object, boundary, time_factor=1, log=False, limit=False):
    global t
    global xvector
    global yvector
    global u_x
    global u_y
    global n
    global s0x
    global s0y
    global T
    global condition
    global s_x
    global s_y

    time_factor = (int(time_factor), 1)[not int(time_factor)]

    # Records original position for reference
    if t == 0:
        s0x, s0y = object[0].pos()[0], object[0].pos()[1]

    # File handling for first run
    if log:
        if os.path.exists('debug.log'):
            if n == 1:
                f = open('debug.log', 'w')
                f.close()

    # Logging
    if log:
        with open('debug.log', 'a') as f:
            f.write('Iteration: ' + str(n))
            f.write('------------\n')

    xvector, yvector = 0, 0         # Resets the vectors

    # Resolves and adds all vectors (rounded because of floating point errors in python)
    for i in object[0].forces:
        xvector += round(i['magnitude'] * round(math.cos(math.pi * i['direction']/180), 15), 14)
        yvector += round(i['magnitude'] * round(math.sin(math.pi * i['direction']/180), 15), 14)

    # Logging
    if log:
        with open('debug.log', 'a') as f:
            f.write('\txvector: ' + str(xvector))
            f.write('\tyvector: ' + str(yvector) + '\n')

    # Calculations for x, y positions and velocities at current time 't' (rounded, as coordinates are pixels)
    v_x, v_y = round(u_x + xvector/object[0].mass * t), round(u_y + yvector/object[0].mass * t)
    s_x, s_y = s0x - round((v_x - u_x) * t), s0y - round((v_y - u_y) * t)

    # Logging
    if log:
        with open('debug.log', 'a') as f:
            f.write('\ts_x: ' + str(s_x) + '\ts_y: ' + str(s_y) + '\n')
            f.write('\tv_x: ' + str(v_x) + '\tv_y: ' + str(v_y) + '\n')

    # Gets rid of impulsive forces
    if t == .01 * time_factor or t == .02 * time_factor:
        removeforce(object[0], 'f_x')
        removeforce(object[0], 'f_y')

    # Logging
    if log:
        with open('debug.log', 'a') as f:
            f.write('\txvector: ' + str(xvector))
            f.write('\tyvector: ' + str(yvector) + '\n')

    # Moves object to coordinate
    object[0].move(s_x, s_y)

    # Logging
    if log:
        with open('debug.log', 'a') as f:
            f.write('\tobject[0].pos()[0:2]: ' + str(object[0].pos()[0:2]) + '\n')

    # Changes v to u for the next iteration
    u_x, u_y = v_x, v_y

    # Collision physics (assumes completely elastic collision)  <!!!Fine-tuning needed!!!>
    if (v_x > 0 and object[0].pos()[0] <= boundary[0].pos()[0]) or (v_x < 0 and object[0].pos()[2] >= boundary[0].pos()[2]):
        addforce(object[0], 'f_x', 2 * object[0].mass * u_x + xvector, -math.copysign(1, object[0].mass * u_x) * 90)
        t = 0
        u_x = 0
    if (v_y > 0 and (object[0].pos()[1] <= boundary[0].pos()[1])) or (v_y < 0 and (object[0].pos()[3] >= boundary[0].pos()[3])):
        addforce(object[0], 'f_y', 2 * object[0].mass * u_y/(round(t), 1)[round(t) == 0] + yvector, -math.copysign(1, object[0].mass * u_y/(round(t), 1)[round(t) == 0]) * 90)
        t = 0
        u_y = 0

    t += .01 * time_factor   # Time counter (to be replaced in next version?)
    T += .01 * time_factor   # Master time-keeper

    # Logging
    if log:
        with open('debug.log', 'a') as f:
            f.write('\tobject[0].forces: ' + str(object[0].forces) + '\n')

    # Logging
    if log:
        with open('debug.log', 'a') as f:
            f.write('\tu_x: ' + str(u_x) + '\tu_y: ' + str(u_y) + '\n')
            f.write('\tv_x: ' + str(v_x) + '\tv_y: ' + str(v_y) + '\n')
            f.write('\tt: ' + str(t) + '\n')
            f.write('\tround(T): ' + str(round(T)) + '\n')
            f.write('\n\n')
        n += 1

    # Limiting the loop at 1 iteration per 10ms
    time.sleep(.01 * time_factor)

    if limit:
        if round(T) == limit:
            pygame.quit()
