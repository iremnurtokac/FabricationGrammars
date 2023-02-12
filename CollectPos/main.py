import urx
import time
import math
import math3d
import logging
import itertools
import FORCE

HOST = "192.168.1.2"
FORCE_SENSOR_PORT = 63351
rob = urx.Robot(HOST)
# f_01 = open(r"myPositions.txt", "w")
# f_02 = open(r"myData.txt", "w")
i = 0
# f_03 = open(r"myActions.txt", "w")
for i in itertools.count(0):
    pose = rob.getl()
    tcp_X = (float(pose[0]) * 1000)
    tcp_Y = (float(pose[1]) * 1000)
    tcp_Z = (float(pose[2]) * 1000)
    rot_x = (float(pose[3]) * 1)
    rot_y = (float(pose[4]) * 1)
    rot_z = (float(pose[5]) * 1)
    force_x = FORCE.get_FX(HOST, FORCE_SENSOR_PORT)
    force_y = FORCE.get_FY(HOST, FORCE_SENSOR_PORT)
    force_z = FORCE.get_FZ(HOST, FORCE_SENSOR_PORT)
    m_x = FORCE.get_MX(HOST, FORCE_SENSOR_PORT)
    m_y = FORCE.get_MY(HOST, FORCE_SENSOR_PORT)
    m_z = FORCE.get_MZ(HOST, FORCE_SENSOR_PORT)
    fx = force_x
    fy = force_y
    fz = force_z
    myForceState = [fx, fy, fz]

    f = max(enumerate(myForceState), key=lambda x: abs(x[1]))[0]

    if f == 0:
        myForceType = fx
    elif f == 1:
        myForceType = fy
    elif f == 2:
        myForceType = fz

    state_file = open(
        "/Users/iremnurtokac/Dropbox/FabricationGrammars/CollectPos/myState.txt", "r")
    myState = float(state_file.readline())
    sensingPara_file = open(
        "/Users/iremnurtokac/Dropbox/FabricationGrammars/CollectPos/mySensingPara.txt", "r")
    mySensingPara = sensingPara_file.readline()

    if abs(myForceType) >= abs(myState):
        rob.stopj()
        f_01 = open(r"myPositions.txt", "w")
        time.sleep(0.001)
        f_01.write(str(tcp_X) + "," + str(tcp_Y) + "," +
                   str(tcp_Z) + "," + str(rot_x) + "," + str(rot_y) + "," + str(rot_z) + "," + str(force_x) + "," + str(force_y) + "," + str(force_z) + "," + str(m_x) + "," + str(m_y) + "," +
                   str(m_z) + "\n")
        time.sleep(0.5)
        f_01.close()
        time.sleep(0.6)
        f_02 = open(r"myBoolean.txt", "w")
        time.sleep(0.001)
        f_02.write("True")
        f_02.close()
        time.sleep(1)
        f_02 = open(r"myBoolean.txt", "w")
        time.sleep(0.001)
        f_02.write("False")
        f_02.close()
    else:
        pass
    time.sleep(0.001)
