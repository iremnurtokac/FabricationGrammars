import socket
import struct
import time
import codecs


def get_FX(host, port):
    valueList1 = []
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host, port))
    time.sleep(0.01)
    V = s1.recv(1024)
    D = str(V)

    # Force Values in list

    LFX = []
    LFY = []
    LFZ = []

    # Moment Values in list
    LMX = []
    LMY = []
    LMZ = []

    # Decoding Data
    # Paranthesis index values
    LP = []

    # Space index values
    LS = []

    # Comma index values
    LC = []
    # print(len(D))

    for i in range(len(D)):
        if D[i] == '(' or D[i] == ')':
            LP.append(i)
        if D[i] == ' ':
            LS.append(i)

        # print(LP)
        # print(LS)

    # FX
    for i in range(LP[0] + 1, LS[0]):
        LFX.append(D[i])
    FX = float(''.join(LFX))
    #print ("FX:", FX)
    # s1.close()
    return FX


def get_FY(host, port):
    valueList1 = []
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host, port))
    time.sleep(0.01)
    V = s1.recv(1024)
    D = str(V)
    # Force Values in list
    LFX = []
    LFY = []
    LFZ = []

    # Moment Values in list
    LMX = []
    LMY = []
    LMZ = []

    # Decoding Data
    # Paranthesis index values
    LP = []

    # Space index values
    LS = []

    # Comma index values
    LC = []
    # print(len(D))

    for i in range(len(D)):
        if D[i] == '(' or D[i] == ')':
            LP.append(i)
        if D[i] == ' ':
            LS.append(i)

    # FY
    for i in range(LS[1] + 1, LS[2]):
        LFY.append(D[i])
    FY = float(''.join(LFY))
    #print("FY:", FY)
    return FY


def get_FZ(host, port):
    valueList1 = []
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host, port))
    time.sleep(0.01)
    V = s1.recv(1024)
    D = str(V)
    # Force Values in list
    LFX = []
    LFY = []
    LFZ = []

    # Moment Values in list
    LMX = []
    LMY = []
    LMZ = []

    # Decoding Data
    # Paranthesis index values
    LP = []

    # Space index values
    LS = []

    # Comma index values
    LC = []
    # print(len(D))

    for i in range(len(D)):
        if D[i] == '(' or D[i] == ')':
            LP.append(i)
        if D[i] == ' ':
            LS.append(i)

    # FZ
    for i in range(LS[3] + 1, LS[4]):
        LFZ.append(D[i])
    FZ = float(''.join(LFZ))
    #print("FZ:", FZ)
    return FZ


def get_MX(host, port):
    valueList1 = []
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host, port))
    time.sleep(0.01)
    V = s1.recv(1024)
    D = str(V)
    # Force Values in list
    LFX = []
    LFY = []
    LFZ = []

    # Moment Values in list
    LMX = []
    LMY = []
    LMZ = []

    # Decoding Data
    # Paranthesis index values
    LP = []

    # Space index values
    LS = []

    # Comma index values
    LC = []
    # print(len(D))

    for i in range(len(D)):
        if D[i] == '(' or D[i] == ')':
            LP.append(i)
        if D[i] == ' ':
            LS.append(i)

    # MX
    for i in range(LS[5] + 1, LS[6]):
        LMX.append(D[i])
    MX = float(''.join(LMX))
    #print("MX:", MX)
    return MX


def get_MY(host, port):
    valueList1 = []
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host, port))
    time.sleep(0.01)
    V = s1.recv(1024)
    D = str(V)
    # Force Values in list
    LFX = []
    LFY = []
    LFZ = []

    # Moment Values in list
    LMX = []
    LMY = []
    LMZ = []

    # Decoding Data
    # Paranthesis index values
    LP = []

    # Space index values
    LS = []

    # Comma index values
    LC = []
    # print(len(D))

    for i in range(len(D)):
        if D[i] == '(' or D[i] == ')':
            LP.append(i)
        if D[i] == ' ':
            LS.append(i)

    # MY
    for i in range(LS[7] + 1, LS[8]):
        LMY.append(D[i])
    MY = float(''.join(LMY))
    #print("MY:", MY)
    return MY


def get_MZ(host, port):
    valueList1 = []
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host, port))
    time.sleep(0.01)
    V = s1.recv(1024)
    D = str(V)
    # Force Values in list
    LFX = []
    LFY = []
    LFZ = []

    # Moment Values in list
    LMX = []
    LMY = []
    LMZ = []

    # Decoding Data
    # Paranthesis index values
    LP = []

    # Space index values
    LS = []

    # Comma index values
    LC = []
    # print(len(D))

    for i in range(len(D)):
        if D[i] == '(' or D[i] == ')':
            LP.append(i)
        if D[i] == ' ':
            LS.append(i)

    # MZ
    for i in range(LS[9] + 1, LP[1]):
        LMZ.append(D[i])
    MZ = float(''.join(LMZ))
    #print('MZ:', MZ)
    return MZ


def get_allForce_Data(host, port):
    valueList1 = []
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host, port))
    time.sleep(0.01)
    V = s1.recv(1024)
    D = str(V)
    # Force Values in list
    LFX = []
    LFY = []
    LFZ = []

    # Moment Values in list
    LMX = []
    LMY = []
    LMZ = []

    # Decoding Data
    # Paranthesis index values
    LP = []

    # Space index values
    LS = []

    # Comma index values
    LC = []
    # print(len(D))

    for i in range(len(D)):
        if D[i] == '(' or D[i] == ')':
            LP.append(i)
        if D[i] == ' ':
            LS.append(i)

    # FX
    for i in range(LP[0] + 1, LS[0]):
        LFX.append(D[i])
    FX = float(''.join(LFX))

    # FY
    for i in range(LS[1] + 1, LS[2]):
        LFY.append(D[i])
    FY = float(''.join(LFY))

    # FZ
    for i in range(LS[3] + 1, LS[4]):
        LFZ.append(D[i])
    FZ = float(''.join(LFZ))

    # MX
    for i in range(LS[5] + 1, LS[6]):
        LMX.append(D[i])
    MX = float(''.join(LMX))

    # MY
    for i in range(LS[7] + 1, LS[8]):
        LMY.append(D[i])
    MY = float(''.join(LMY))

    # MZ
    for i in range(LS[9] + 1, LP[1]):
        LMZ.append(D[i])
    MZ = float(''.join(LMZ))

    return (str(FX) + "," + str(FY) + "," + str(FZ) + "," + str(MX) + "," + str(MY) + "," + str(MZ))

# s1.close()
# print('s1 is closed!')
