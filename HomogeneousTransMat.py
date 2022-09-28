from pickletools import OpcodeInfo, optimize
import numpy as np

# Denavit-Hartenberg Homogeneous Transformation Matrix
def DH(theta, d, a, alpha):
    print("Solving for: ", theta, d, a, alpha, end="\n\n")

    # Rotation alpha about OX axis
    # T(x, alpha)
    Txalpha = np.array([[1, 0, 0, 0],
                    [0, np.cos(alpha), -np.sin(alpha), 0],
                    [0, np.sin(alpha), np.cos(alpha), 0],
                    [0, 0, 0, 1]])

    # Translation a along OX axis
    # T(x, a)
    Txa = np.array([[1, 0, 0, a],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    # Translation d along OZ axis
    # T(z, d)
    Tzd = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, d],
                    [0, 0, 0, 1]])
    
    # Rotation of theta about OZ axis
    # T(z, theta)
    Tztheta = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                    [np.sin(theta), np.cos(theta), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])


    # We have that T = T(z, tetha) T(z,d) T(x,a) T(x, alpha)
    # T = np.matmul( (np.matmul( (np.matmul(Txalpha, Txa)), Tzd) ), Tztheta )
    Temp = np.matmul(Txalpha, Txa)
    Temp2 = np.matmul(Temp, Tzd)
    T = np.matmul(Temp2, Tztheta)
    # We round T to 3 decimals:
    T = np.around(T, decimals=3)
    
    # Print the result T
    print("T = \n", T, end="\n\n")
    
    '''
    # Print all the matrices
    print("Txalpha =", np.around(Txalpha, decimals=3))
    print("Txa = ", np.around(Txa, decimals=3))
    print("Tzd = ", np.around(Tzd, decimals=3))
    print("Tztheta = ", np.around(Tztheta, decimals=3))
    print()
    '''

# Main
if __name__ == "__main__":
    print("Denavit-Hartenberg Homogeneous Transformation Matrix")
    print(" --Option 1: DH(theta, d, a, alpha) in degrees")
    print(" --Option 2: DH(theta, d, a, alpha) in radians")
    option = int(input("Choose an option: "))

    # Parameters in degrees
    if option == 1:
        print("Introduce the values (in degrees) of:")
        theta, d, a, alpha = input("theta d a alpha: ").split()
        print()
        DH( np.deg2rad(float(theta)), 
            np.float(d),
            np.float(a),
            np.deg2rad(float(alpha)))

    # Parameters in radians  
    if option == 2:
        print("Introduce the values (in radians) of:")
        theta, d, a, alpha = input("theta d a alpha: ").split()
        print()
        DH(theta, d, a, alpha)