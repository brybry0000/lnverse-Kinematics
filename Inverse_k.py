import numpy as np
import math
import PySimpleGUI as sg
import pandas as pd

# GUI code

sg.theme('LightBlue')

# Excel Read Code

EXCEL_FILE = 'Inverse_k.xlsx'
df = pd.read_excel(EXCEL_FILE)

# Lay-out code

Main_layout = [
    [sg.Push(), sg.Text('Cartesian MEXE CALCULATOR', font = ("Courier New", 20)), sg.Push()],
    [sg.Text('Forward Kinematics Calculator', font = ("Courier New", 12))],
    [sg.Text('Fill out the following fields:', font = ("Courier New", 10)),
    sg.Push(), sg.Push(), sg.Button('Click Here to Start Calculation', font = ("Courier New", 15), size=(36,0), button_color=('thistle', 'mediumvioletred')), sg.Push(),
    sg.Text('OR', font = ("Courier New",12)),
    sg.Push(), sg.Button('Solve Inverse Kinematics', font = ("Courier New", 12), disabled=True, size=(35,0), button_color=('thistle', 'green')), sg.Push()],
    
    [sg.Text('a1 =', font = ("Courier New", 10)),sg.InputText('0', key='a1', size=(20,10)),
    sg.Text('d1 =', font = ("Courier New", 10)),sg.InputText('0', key='d1', size=(20,10)), sg.Push(),
    sg.Push(), sg.Button('Jacobian Matrix (J)', font = ("Courier New", 12), disabled=True, size=(20,0), button_color=('thistle', 'palevioletred')),
    sg.Button('Det(J)', font = ("Courier New", 12), size=(14,0), disabled=True, button_color=('thistle', 'palevioletred')),
    sg.Button('Inverse of J', font = ("Courier New", 12), size=(15,0), disabled=True, button_color=('thistle', 'palevioletred')),
    sg.Button('Transpose of J', font = ("Courier New", 12), size=(15,0), disabled=True, button_color=('thistle', 'palevioletred')), sg.Push()],

    [sg.Text('a2 =', font = ("Courier New", 10)),sg.InputText('0', key='a2', size=(20,10)),
    sg.Text('d2 =', font = ("Courier New", 10)),sg.InputText('0', key='d2', size=(20,10))],

    [sg.Text('a3 =', font = ("Courier New", 10)),sg.InputText('0', key='a3', size=(20,10)),
    sg.Text('d3 =', font = ("Courier New", 10)),sg.InputText('0', key='d3', size=(20,10)),
    

    ],
    [sg.Text('a4 =', font = ("Courier New", 10)),sg.InputText('0', key='a4', size=(20,10))],
    [sg.Button('Solve Forward Kinematics', tooltip='Go to "Click Here to Start Calculation"!', font = ("Courier New", 12), disabled=True, button_color=('thistle', 'palevioletred')), sg.Push(),
    sg.Push(), sg.Button('Path and Trajectory Planning', font = ("Courier New", 12), size=(40, 0), disabled=True, button_color=('thistle', 'green')), sg.Push()],
    
    [sg.Frame('Position Vector: ',[[
        sg.Text('X =', font = ("Courier New", 10)),sg.InputText('0', key='X', size=(10,1)),
        sg.Text('Y =', font = ("Courier New", 10)),sg.InputText('0', key='Y', size=(10,1)),
        sg.Text('Z =', font = ("Courier New", 10)),sg.InputText('0', key='Z', size=(10,1))]])],

    [sg.Push(), sg.Frame('H0_3 Transformation Matrix = ', [[sg.Output(size=(60,12), key = '_output_')]]),
    sg.Push(), sg.Image('carrtesian.png', key='ccartesian'), sg.Push()],
    [sg.Submit(font = ("Courier New", 10)), sg.Exit(font = ("Courier New", 10))]]

window = sg.Window('Cartesian Manipulator Forward Kinematics',Main_layout, resizable=True)

#Inverse Kinematics Window function 

def Inverse_Kinematics_window():
    sg.theme('LightBlue')
    EXCEL_FILE = 'Inverse_k.xlsx'
    IK_df = pd.read_excel(EXCEL_FILE) 

    IK_layout = [
        [sg.Push(), sg.Text('Inverse Kinematics', font = ("Courier New", 12)),sg.Push()],
        [sg.Text('Fill out the following fields:', font = ("Courier New", 10))],
        [sg.Text('a1 =', font = ("Courier New", 10)),sg.InputText('0', key='a1', size=(20,10)),
        sg.Text('mm',font = ("Courier New", 10)),
            sg.Text('X =', font = ("Courier New", 10)),sg.InputText('0', key='X', size=(10,1)),    
            sg.Text('mm',font = ("Courier New", 10))],
        [sg.Text('a2 =', font = ("Courier New", 10)),sg.InputText('0', key='a2', size=(20,10)),
        sg.Text('mm',font = ("Courier New", 10)),
            sg.Text('Y =', font = ("Courier New", 10)),sg.InputText('0', key='Y', size=(10,1)),
            sg.Text('mm',font = ("Courier New", 10))],
        [sg.Text('a3 =', font = ("Courier New", 10)),sg.InputText('0', key='a3', size=(20,10)),
        sg.Text('mm',font = ("Courier New", 10)),
            sg.Text('Z =', font = ("Courier New", 10)),sg.InputText('0', key='Z', size=(10,1)),
            sg.Text('mm',font = ("Courier New", 10))],
        [sg.Text('a4 =', font = ("Courier New", 10)),sg.InputText('0', key='a4', size=(20,10)),
        sg.Text('mm',font = ("Courier New", 10))],
        [sg.Button('Solve Inverse Kinematics', font = ("Courier New", 10), button_color=('red', 'yellow')), sg.Push()],

        [sg.Frame('Position Vector: ',[[
            sg.Text('d1 =', font = ("Courier New", 10)),sg.InputText(key='IK_d1', size=(20,10)),
            sg.Text('mm',font = ("Courier New", 10)),
            sg.Text('d2 =', font = ("Courier New", 10)),sg.InputText(key='IK_d2', size=(20,10)),
            sg.Text('mm',font = ("Courier New", 10)),
            sg.Text('d3 =', font = ("Courier New", 10)),sg.InputText(key='IK_d3', size=(20,10)),
            sg.Text('mm',font = ("Courier New", 10)),]])], 
            [sg.Submit(font = ("Courier New", 10)),sg.Exit(font = ("Courier New", 10))]
        
    ]

    # Window Code
    Inverse_Kinematics_window = sg.Window('Inverse Kinematics',IK_layout)

    while True:
        event,values = Inverse_Kinematics_window.read(0)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == 'Solve Inverse Kinematics':
            # Link Lengths 
            a1 = float(values['a1'])
            a2 = float(values['a2'])
            a3 = float(values['a3'])
            a4 = float(values['a4'])

            # Position Vectors 
            X = float(values['X'])
            Y = float(values['Y'])
            Z = float(values['Z'])

            try:
                d1 = Y - a2 
            except:
                d1 = -1
                sg.popup('Warning! Present values causes error.')
                sg.popup('Restart the GUI then assign proper values')
                break 

            # d1
            d1 = Y - a2

            # d2
            d2 = X - a3

            # d3
            d3 = a1 - Z - a4

            Inverse_Kinematics_window['IK_d1'].Update(np.around(d1,3))
            Inverse_Kinematics_window['IK_d2'].Update(np.around(d2,3))
            Inverse_Kinematics_window['IK_d3'].Update(np.around(d3,3))
    
    Inverse_Kinematics_window.close()

      
# Variable Codes for disabling buttons

disable_FK = window['Solve Forward Kinematics']
disable_J = window['Jacobian Matrix (J)']
disable_D = window['Det(J)']
disable_IV = window['Inverse of J']
disable_TJ = window['Transpose of J']
disable_PT = window['Path and Trajectory Planning']
disable_IK = window['Solve Inverse Kinematics']
while True:
    event,values = window.read(200)
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    window.Element('carrtesian').UpdateAnimation('ccartesian.png', time_between_frames=50)

    if event == 'Click Here to Start Calculation' :
        disable_FK.update(disabled=False)
        disable_J.update(disabled=False)
        disable_IK.update(disabled=False)


    if event == 'Solve Forward Kinematics' :
        
        # Forward Kinematic Codes
      
        # link lengths in cm
        a1 = float(values['a1'])
        a2 = float(values['a2'])
        a3 = float(values['a3'])
        a4 = float(values['a4'])

        # Joint Variable (Thetas in degrees & dinstance in cm)
        d1 = float(values['d1'])
        d2 = float(values['d2'])
        d3 = float(values['d3'])

      

        DHPT = [
            [0,(270.0/180.0)*np.pi,0,float(a1)],
            [(270.0/180.0)*np.pi,(270.0/180.0)*np.pi,0,float(a2)+float(d1)],
            [(270.0/180.0)*np.pi,(90.0/180.0)*np.pi,0,float(a3)+float(d2)],
            [0,0,0,float(a4)+float(d3)]
            ]

        # D-H Notation Formula for HTM
        i = 0
        H0_1 = [
            [np.cos(DHPT[i][0]), -np.sin(DHPT[i][0])*np.cos(DHPT[i][1]), np.sin(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.cos(DHPT[i][0])],
            [np.sin(DHPT[i][0]), np.cos(DHPT[i][0])*np.cos(DHPT[i][1]), -np.cos(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.sin(DHPT[i][0])],
            [0, np.sin(DHPT[i][1]), np.cos(DHPT[i][1]), DHPT[i][3]],
            [0, 0, 0, 1],
            ]

        i = 1
        H1_2 = [
            [np.cos(DHPT[i][0]), -np.sin(DHPT[i][0])*np.cos(DHPT[i][1]), np.sin(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.cos(DHPT[i][0])],
            [np.sin(DHPT[i][0]), np.cos(DHPT[i][0])*np.cos(DHPT[i][1]), -np.cos(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.sin(DHPT[i][0])],
            [0, np.sin(DHPT[i][1]), np.cos(DHPT[i][1]), DHPT[i][3]],
            [0, 0, 0, 1],
            ]

        i = 2
        H2_3 = [
            [np.cos(DHPT[i][0]), -np.sin(DHPT[i][0])*np.cos(DHPT[i][1]), np.sin(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.cos(DHPT[i][0])],
            [np.sin(DHPT[i][0]), np.cos(DHPT[i][0])*np.cos(DHPT[i][1]), -np.cos(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.sin(DHPT[i][0])],
            [0, np.sin(DHPT[i][1]), np.cos(DHPT[i][1]), DHPT[i][3]],
            [0, 0, 0, 1],
            ]

        i = 3
        H3_4 = [
            [np.cos(DHPT[i][0]), -np.sin(DHPT[i][0])*np.cos(DHPT[i][1]), np.sin(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.cos(DHPT[i][0])],
            [np.sin(DHPT[i][0]), np.cos(DHPT[i][0])*np.cos(DHPT[i][1]), -np.cos(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.sin(DHPT[i][0])],
            [0, np.sin(DHPT[i][1]), np.cos(DHPT[i][1]), DHPT[i][3]],
            [0, 0, 0, 1],
            ]

        # Transformation Matrices from base to end-effector
        #print("HO_1 = ")
        #print(np.matrix(H0_1))
        #print("H1_2 = ")
        #print(np.matrix(H1_2))
        #print("H2_3 = ")
        #print(np.matrix(H2_3))

        # Dot Product of H0_3 = HO_1*H1_2*H2_3
        H0_2 = np.dot(H0_1,H1_2)
        H0_3 = np.dot(H0_2,H2_3)
        H0_4 = np.dot(H0_3,H3_4)

        # Transformation Matrix of the Manipulator
        print("H0_3 = ")
        print(np.matrix(H0_3))

        # Position Vector X Y Z

        X0_4 = H0_4[0,3]
        print("X = ", X0_4)

        Y0_4 = H0_4[1,3]
        print("Y = ", Y0_4)

        Z0_4 = H0_4[2,3]
        print("Z = ", Z0_4)
        
        # Disabler program 
        disable_J.update(disabled=False)
        disable_PT.update(disabled=False)
        disable_D.update(disabled=True)
        disable_TJ.update(disabled=True)

        # XYZ OUTPUT TO INPUT UPDATER
        window['X'].update(X0_4)
        window['Y'].update(Y0_4)
        window['Z'].update(Z0_4)

    if event == 'Jacobian Matrix (J)' :
        
        # Defining the equations

        i = [[0],[0],[1]]
        A = [[0],[0],[0]]
        IM = [[1,0,0],[0,1,0],[0,0,1]]

      #  try:
      #      H0_1 = np.matrix(H0_1)
      #  except:
      #      H0_1 = -1
      #      sg.popup('WARNING')
      #      sg.popup('Restart the GUI, then click first the "Click Here to Start Calculation" button!')
      #     break


        # Row 1 - 3, column 1
        #H0_0 = np.dot(H0_1,H0_1)
        #R0_0 = H0_0[0:3, 0:3]
        #R0_0 = i
        J0 = np.dot(IM,i)

        # Row 1-3, column 2
        H0_1a = np.dot(H0_1,1)
        R0_1 = H0_1a[0:3,0:3]
        J1 = np.dot(R0_1,i)

        # Row 1-3, column 3
        R0_2 = H0_2[0:3, 0:3]
        J2 = np.dot(R0_2,i)

        # Row 1-3, column 4
        R0_3 = H0_3[0:3, 0:3]
        J3 = np.dot(R0_3,i)
        
        

        # Jacobian Matrix
        JM1 = np.concatenate((J0, J1, J2, J3), 1)
        JM2 = np.concatenate((A, A, A, A), 1)
        Jacobian = np.concatenate((JM1, JM2), 0)
        sg.popup('J =', Jacobian)
        JM1a = np.concatenate((J0, J1, J2), 1)
        #Jacobi_a = Jacobian[4:0, 4:]
        #Jacobi_b = np.dot(Jacobi_a,1)
        # Disabler program 
        disable_J.update(disabled=True)
        disable_D.update(disabled=False)
        disable_TJ.update(disabled=False)

    if event == 'Det(J)' :
       # try:
       #    JM1 = np.concatenate((J0, J1, J2), 1)
       # except:
       #     JM1 = -1
       #     sg.popup('WARNING')
       #     sg.popup('Restart the GUI, then click first the "Click Here to Start Calculation" button!')
       #     break

        DJ = np.linalg.det(Jacobian[0:3,1:])
        #print("D(J) = ", DJ)
        sg.popup('D(J) = ', "%.4f" % DJ)

        if 0.0 >= DJ > -1.0:
            disable_IV.update(disabled=True)
            sg.popup('Warning: This is Non-Invertible')
        elif DJ != 0.0 or DJ != -0.0:
            disable_IV.update(disabled=False)
    
    if event == 'Inverse of J' :
        #try:
        #    JM1 = np.concatenate((J0, J1, J2), 1)
        #except:
        #    JM1 = -1
        #    sg.popup('WARNING')
        #    sg.popup('Restart the GUI, then click first the "Click Here to Start Calculation" button!')
        #    break 
        IJ = np.linalg.inv(Jacobian[0:3,1:])
        sg.popup('I(J) = ', IJ)

    if event == 'Transpose of J' :
        #try:
        #    JM1 = np.concatenate((J0, J1, J2), 1)
        #except:
        #    JM1 = -1
        #    sg.popup('WARNING')
        #    sg.popup('Restart the GUI, then click first the "Click Here to Start Calculation" button!')
        #    break
        TJ = np.transpose(Jacobian[0:3,1:])
        sg.popup('T(J) = ', TJ)

    if event == 'Submit' :
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data Saved!')
    
    elif event == 'Solve Inverse Kinematics':
        Inverse_Kinematics_window()

window.close()