## Denavit-Hartenberg-Homogeneous-Transformation-Matrix
# Description
This program will find the homogeneous transformation matrix (T) for the following operation:<br>
-Rotation alpha about OX axis<br>
-Translation of d along OZ axis<br>
-Translation of a along OX axis<br>
-Rotation of about OZ axis<br>

# Example of use:
Denavit-Hartenberg Homogeneous Transformation Matrix<br>
 --Option 1: DH(theta, d, a, alpha) in degrees<br>
 --Option 2: DH(theta, d, a, alpha) in radians<br>
Choose an option: 1<br>
Introduce the values (in degrees) of:<br>
theta d a alpha: 60 90 0 20<br>
<br>
Solving for:  1.0471975511965976 1.5707963267948966 0.0 0.3490658503988659<br>
<br>
T =<br>
 [[ 0.94  -0.342  0.     0.   ]<br>
 [ 0.321  0.883 -0.342 -0.537]<br>
 [ 0.117  0.321  0.94   1.476]<br>
 [ 0.     0.     0.     1.   ]]<br>
