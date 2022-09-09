import numpy as np

# Denavit-Hartenberg Homogeneous Transformation Matrix
def DH(theta, d, a, alpha):
    print(theta, d, a, alpha)

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
    Tztheta = np.array([[np.cos(alpha), -np.sin(alpha), 0, 0],
                    [np.sin(alpha), np.cos(alpha), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    # We have that T = T(z, tetha) T(z,d) T(x,a) T(x, alpha)
    Temp = np.matmul(Txalpha, Txa)
    Temp2 = np.matmul(Temp, Tzd)
    T = np.matmul(Temp2, Tztheta)

    # Tv2 = np.matmul( (np.matmul( (np.matmul(Txalpha, Txa)), Tzd) ), Tztheta )

    # Print all the matrices
    print("Txalpha =", Txalpha)
    print("Txa = ", Txa)
    print("Tzd = ", Tzd)
    print("Tztheta = ", Tztheta)
    print()
    
    # Print the result T
    print("T = ", T)
    print()
    print("Tv2", Tv2)

# Main
if __name__ == "__main__":
    print("Denavit-Hartenberg Homogeneous Transformation Matrix")
    DH(0, 0, 0, 0)