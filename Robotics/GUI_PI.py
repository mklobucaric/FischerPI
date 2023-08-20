import PySimpleGUI as sg   
import RPi.GPIO as GPIO
import time   


class GUI_motor_position():
    def __init__(self,motor_X_axis,motor_Y_axis,motor_rotation,motor_gripper,position_dict,gripper_dict,command_list_keys,command_list_values,
                 command_list_items,position_combo,gripper_combo):
        self.motor_X_axis = motor_X_axis
        self.motor_Y_axis = motor_Y_axis
        self.motor_rotation = motor_rotation
        self.motor_gripper = motor_gripper
        self.position_dict = position_dict
        self.gripper_dict = gripper_dict
        self.command_list_keys = command_list_keys
        self.command_list_values = command_list_values
        self.command_list_items = command_list_items
        self.position_combo = position_combo
        self.gripper_combo = gripper_combo
        
        
        
        # Images are located in a subfolder in the Fisher robotics.py folder
 
        image_homing = './ButtonGraphics/home_2.png'
        image_close = './ButtonGraphics/agt_action_fail_256.png'

        image_teach1 = './ButtonGraphics/Fisher_robotics.png'


        image_homing1 = './ButtonGraphics/search1.png'
        image_homing2 = './ButtonGraphics/search.png'

        image_arrow_left = './ButtonGraphics/arrow_left.png'
        image_arrow_right = './ButtonGraphics/arrow_right.png'

        image_arrow_up = './ButtonGraphics/arrow_up.png'
        image_arrow_down = './ButtonGraphics/arrow_down (2).png'

        image_arrow_forward = './ButtonGraphics/forward_2.png'
        image_arrow_back = './ButtonGraphics/back_2.png'

        image_gripper_open = './ButtonGraphics/rightleft2red.png'
        image_gripper_close = './ButtonGraphics/rightleft2red_r01.png'
        
        col2 = [[sg.Image(image_teach1,pad=(0,0))],
                [sg.Text('Teach gripper position'), sg.Text('          '), sg.Text('Gripper position coordinates')],
                [sg.RealtimeButton('',image_filename=image_gripper_open,image_size=(60, 60), image_subsample=2,border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='_gopen_'),
                sg.Text(' '),sg.RealtimeButton('',image_filename=image_gripper_close,image_size=(60, 60), image_subsample=2,border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='_gclose_'),
                sg.Text('          '), sg.Drop(self.gripper_combo,size=(20,1),enable_events = True, 
                                               key = '_gripper_combo_2_',readonly = True, 
                                               default_value = 'G5. Pozicija'),sg.Text('G:'),
                 sg.Text('15', key='_G_'),sg.Text('/ 15',pad=(0,0))],

                ]

        col3 = [[sg.RealtimeButton('',image_filename=image_homing2,image_size=(60, 60), image_subsample=2,
                           border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), 
                           key='_homing2_'),sg.Text(' '),
                 sg.Button('',image_filename=image_close,image_size=(60, 60), image_subsample=2,
                           border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), 
                           key='_close2_')],
                [sg.Text('Ready',pad=(0,0))],
                [sg.Text('_____________________',pad=(0,0))],
                [sg.Text('Teach position',pad=(0,0))],
    #               [sg.Text('')],

                [sg.RealtimeButton('',image_filename=image_arrow_left,image_size=(60, 60), image_subsample=2,border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='_left_'),
                sg.Text(' '),sg.RealtimeButton('',image_filename=image_arrow_right,image_size=(60, 60), image_subsample=2,border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='_right_')],
                [sg.Text('')],

                [sg.RealtimeButton('',image_filename=image_arrow_up,image_size=(60, 60), image_subsample=2,border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='_up_'),
                sg.Text(' '),sg.RealtimeButton('',image_filename=image_arrow_down,image_size=(60, 60), image_subsample=2,border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='_down_')],
                [sg.Text('')],

                [sg.RealtimeButton('',image_filename=image_arrow_forward,image_size=(60, 60), image_subsample=3,border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='_forward_'),
                sg.Text(' '), sg.RealtimeButton('',image_filename=image_arrow_back,image_size=(60, 60), image_subsample=3,border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='_back_')],
                [sg.Text('')],

                [sg.Drop(self.position_combo,pad=(0,0),size=(20,1),enable_events = True, key = '_position_combo_2_',
               readonly = True, default_value = '10. Pozicija')],
    #                [sg.Text('')],
                [sg.Text('Position coordinates:',pad=(0,0))],
                [sg.Text('X:',pad=(0,0)), sg.Text('100',pad=(0,0), key='_X_'),sg.Text('/ 76')],
                [sg.Text('Y:',pad=(0,0)), sg.Text('1050',pad=(0,0), key='_Y_'),sg.Text('/ 2200')],
                [sg.Text('R:',pad=(0,0)), sg.Text('4050',pad=(0,0), key='_R_'),sg.Text('/ 2300')],

               ]

        layout2 = [[sg.Column(col2),sg.Column(col3)],

                  [sg.Text('Ready', relief=sg.RELIEF_SUNKEN, size=(113, 1), pad=(4, 3), key='_status2_')]]

        self.window2=sg.Window('Teach position',layout2, size=(804, 600), resizable=True,grab_anywhere = True, no_titlebar = True).Finalize()
        
    def homing(self):
        self.motor_X_axis.run_robot = True
        self.motor_Y_axis.run_robot = True
        self.motor_rotation.run_robot = True
        self.motor_gripper.run_robot = True
        
        self.motor_X_axis.homing()
        self.motor_Y_axis.homing() 
        self.motor_rotation.homing()
        self.motor_gripper.homing()
    
    def run(self):
        
        self.homing()
        
        while True:
            event2, values2 = self.window2.Read(timeout=0)

            if event2 is not None or event2 is not '_homing2_':

                if event2 == '_left_':
                    self.motor_X_axis.forward()

                elif event2 == '_right_':
                    self.motor_X_axis.back() 

                elif event2 == '_up_':
                    self.motor_Y_axis.forward()

                elif event2 == '_down_':
                    self.motor_Y_axis.back()

                elif event2 == '_forward_':
                    self.motor_rotation.forward()

                elif event2 == '_back_':
                    self.motor_rotation.back()

                elif event2 == '_gopen_':
                    self.motor_gripper.forward()

                elif event2 == '_gclose_':
                    self.motor_gripper.back()
                elif event2 == '_homing2_':
                    self.homing()

                    
                elif event2 == '_position_combo_2_' and len(values2['_position_combo_2_']):
                    if self.motor_Y_axis.counter < 0:
                        self.motor_Y_axis.counter =0
                    if self.motor_rotation.counter < 0:
                        self.motor_rotation.counter =0
                    position2 = values2['_position_combo_2_']
                    self.position_dict.update({position2:{'X':self.motor_X_axis.counter,
                                                     'Y':round(self.motor_Y_axis.position_coordinate),
                                                   'R':self.motor_rotation.position_coordinate}})


                elif event2 == '_gripper_combo_2_' and len(values2['_gripper_combo_2_']):
                    gposition2 = values2['_gripper_combo_2_']
                    self.gripper_dict.update({gposition2:self.motor_gripper.counter})

                else:
                    self.motor_X_axis.stop()
                    self.motor_Y_axis.stop()
                    self.motor_rotation.stop()
                    self.motor_gripper.stop()

            self.window2.Element('_X_').Update(self.motor_X_axis.counter)
            self.window2.Element('_Y_').Update(self.motor_Y_axis.counter)
            self.window2.Element('_R_').Update(self.motor_rotation.counter)
            self.window2.Element('_G_').Update(self.motor_gripper.counter)
            self.window2.Element('_status2_').Update('X:'+str(self.motor_X_axis.counter)+'; Y:'+str(self.motor_Y_axis.counter)+
                                    '; R:'+str(self.motor_rotation.counter)+'; G:'+str(self.motor_gripper.counter)+
                                    '; X_home: '+str(GPIO.input(self.motor_X_axis.lButton_pin))+'; Y_home: '+
                                    str(GPIO.input(self.motor_Y_axis.lButton_pin))+'; R_home: '+str(GPIO.input(self.motor_rotation.lButton_pin))+
                                    '; G_home: '+str(GPIO.input(self.motor_gripper.lButton_pin)))

            if event2 is '_close2_':
                self.window2.Close()
                self.window2_active = False
                break
        


class GUI_robot_control():
    def __init__(self,motor_X_axis,motor_Y_axis,motor_rotation,motor_gripper,stopButton_pin,callback_func):

               
        self.motor_X_axis = motor_X_axis
        self.motor_Y_axis = motor_Y_axis
        self.motor_rotation = motor_rotation
        self.motor_gripper = motor_gripper

        
        self.position_dict = {}
        self.gripper_dict = {}
        self.command_list_keys = []
        self.command_list_values = []
        self.command_list_items = []
        self.position_combo = ['1. Position','2. Position','3. Position','4. Position','5. Position','6. Position','7. Position','8. Position','9. Position','10. Position'] 
        self.gripper_combo = ['G1. Position','G2. Position','G3. Position','G4. Position','G5. Position']
        self.command_counter = 0
        self.stopButton_pin = stopButton_pin
        self.callback_func = callback_func
         
        GPIO.setup(self.stopButton_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.stopButton_pin,GPIO.FALLING, callback=callback_func, bouncetime=500)
  
        sg.SetOptions(auto_size_buttons=True, margins=(0,0), button_color=sg.COLOR_SYSTEM_DEFAULT)

        # Images are located in a subfolder in the Fisher robotics.py folder
        image_new = './ButtonGraphics/tab_new_r.png'
        image_open = './ButtonGraphics/folder_yellow_open.png'
        image_save = './ButtonGraphics/save.png'

        image_close = './ButtonGraphics/agt_action_fail_256.png'

        image_single = './ButtonGraphics/arrow_stop_down.png'
        image_scycle = './ButtonGraphics/arrow_down_1.png'
        image_continuously = './ButtonGraphics/arrow_circle_down.png'

        image_homing = './ButtonGraphics/home_2.png'
        image_teach = './ButtonGraphics/industrial_robot (2).png'

        image_enter_position = './ButtonGraphics/03_robot.png'
        image_enter_gposition = './ButtonGraphics/06_robot.png'
        image_delete_position = './ButtonGraphics/hitchhikeguidetogalaxy1_close.png'

        image_teach1 = './ButtonGraphics/Fisher_robotics.png'


        image_homing1 = './ButtonGraphics/search1.png'
        image_homing2 = './ButtonGraphics/search.png'

        image_arrow_left = './ButtonGraphics/arrow_left.png'
        image_arrow_right = './ButtonGraphics/arrow_right.png'

        image_arrow_up = './ButtonGraphics/arrow_up.png'
        image_arrow_down = './ButtonGraphics/arrow_down (2).png'

        image_arrow_forward = './ButtonGraphics/forward_2.png'
        image_arrow_back = './ButtonGraphics/back_2.png'

        image_gripper_open = './ButtonGraphics/rightleft2red.png'
        image_gripper_close = './ButtonGraphics/rightleft2red_r01.png'

        # ------ Menu Definition ------ #      
        menu_def = [['&File', ['&Open','Save &as','---', 'E&xit' ]],['&Edit', ['&Undo','---','C&ut','&Copy','&Paste']],['&Run', ['&Homing', '&Teach Positions', '---', 'R&un single line', '&Run single cycle','Run &continuously']],['&Help', '&About...'],]  



        toolbar_buttons = [[sg.Button('', image_filename=image_open,image_size=(40, 40), image_subsample=5, border_width=1, 
                                      button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0, 0), key='_open_'),
                            sg.Button('', image_filename=image_save,image_size=(40, 40), image_subsample=5, border_width=1, 
                                      button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0, 0), key='_save_'),
                            
                            sg.VerticalSeparator(pad=(0,0)),
                            
                            sg.Button('', image_filename=image_single,image_size=(40, 40), image_subsample=1, 
                                      button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0, 0), 
                                      key='_run_single_line_'),
                            sg.Button('', image_filename=image_scycle,image_size=(40, 40), image_subsample=1, 
                                      button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0, 0), 
                                      key='_run_single_cycle_'),
                            sg.Button('', image_filename=image_continuously,image_size=(40, 40), image_subsample=1, 
                                      button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0, 0), 
                                      key='_run_continuously_'),
                            sg.VerticalSeparator(pad=(0,0)),
                            
                            sg.Button('', image_filename=image_homing1,image_size=(40, 40), image_subsample=1, 
                                      button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0, 0), key='_homing_'),
                            sg.Button('', image_filename=image_teach,image_size=(40, 40), image_subsample=1, 
                                      button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0, 0), key='_teach_position_'),
                            ]]

        # Column layout      
        col=[[sg.Text('Select robot position:',pad=(0,0))],
          
            [sg.Drop(self.position_combo,size=(20,1),pad=(0,0),enable_events = True, key = '_position_combo_1_',
                   readonly = True)], 
            [sg.Text('                  '),sg.Text('X:',pad=(0,0)),sg.Text('____',pad=(0,0),key='_X1_')],

            [sg.Text('                  '),sg.Text('Y:',pad=(0,0)), sg.Text('____',pad=(0,0),key='_Y1_')], 
            [sg.Text('                  '),sg.Text('R:',pad=(0,0)), sg.Text('____',pad=(0,0),key='_R1_')],
            [sg.Button('',image_filename=image_enter_position,image_size=(60, 60), image_subsample=2,
                      border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), 
                      key='_enter_position_')],
            #       [sg.Text('')],

            [sg.Text('Select gripper position:',pad=(0,0))],      
            [sg.Drop(self.gripper_combo,pad=(0,0),size=(20,1),enable_events = True, key = '_gripper_combo_1_',
                   readonly = True)],
            [sg.Text('                  '),sg.Text('G:',pad=(0,0)), sg.Text('____',key='_G1_')], 
            [sg.Button('',image_filename=image_enter_gposition,image_size=(60, 60), image_subsample=2,
                      border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), 
                      key='_enter_gposition_'),
            sg.Text(' '),sg.Button('',image_filename=image_gripper_open,image_size=(60, 60), image_subsample=2,
                                   border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), 
                                   key='_gripperOpen_')],
            #       [sg.Text('')],

            [sg.Text('Delete position:',pad=(0,0))], 

            [sg.Button('',image_filename=image_delete_position,image_size=(60, 60), image_subsample=2,
                      border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), 
                      key='_stop_robot_')],
            #       [sg.Text('')],
            [sg.Text('Exit:',pad=(0,0))],
            [sg.Button(image_filename=image_close,image_size=(60, 60), image_subsample=2,border_width=1,button_color=('black', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='_close1_') ],
            ]      


        right_click_menu_1 = ['&Right', [ 'C&ut', 'C&opy', '&Paste']]


            # layout = toolbar_buttons
            # ------ GUI Defintion ------ #     
        layout = [[sg.Menu(menu_def, )], 
                [sg.Frame('', toolbar_buttons,title_color='white', background_color=sg.COLOR_SYSTEM_DEFAULT, pad=(0,0))],
                [sg.Listbox(values=[''], size=(43,29),pad=(0,0),key = '_list_box_', enable_events = True), sg.Column(col)],
                #[sg.Output(size=(60, 20),key='_output_'), sg.Column(col)],

                [sg.Text('Status Bar', relief=sg.RELIEF_SUNKEN, size=(80, 1), pad=(0, 1), key='_status1_')]
                ]      


        self.window1 = sg.Window('Fishertechnik robotics', layout,no_titlebar = True, size=(480, 570), grab_anywhere = True, resizable=True,
                                 right_click_menu=right_click_menu_1).Finalize()
        self.window2_active = False

    def homing(self):
        self.motor_X_axis.run_robot = True
        self.motor_Y_axis.run_robot = True
        self.motor_rotation.run_robot = True
        self.motor_gripper.run_robot = True
        
        self.motor_X_axis.homing()
        self.motor_Y_axis.homing() 
        self.motor_rotation.homing()
        self.motor_gripper.homing()
        
    def move_position(self,command,coordinate):
        if command[0] == 'G':
            if coordinate <= 1:
                self.motor_gripper.homing()
            else:
                if coordinate >= 23:
                    coordinate = 22
                self.motor_gripper.go_to_position(coordinate)
        else:
            if coordinate['X'] <= 1:
                self.motor_X_axis.homing()
            else:
                if coordinate['X'] >= 75:
                    coordinate['X'] = 75
                self.motor_X_axis.go_to_position(coordinate['X'])
            if coordinate['Y'] <= 50:
                self.motor_Y_axis.homing()
            elif abs(coordinate['Y']-self.motor_Y_axis.counter) > 50:
    #            if coordinate['Y'] >= 1300:
    #                coordinate['Y'] = 1300
                if coordinate['Y'] >= 2200:
                    coordinate['Y'] = 2200
                self.motor_Y_axis.go_to_position(coordinate['Y'])
            else:
                pass
            if coordinate['R'] <= 50:
                self.motor_rotation.homing()
            elif abs(coordinate['R']-self.motor_rotation.counter) > 100:
    #            if coordinate['R'] >=1150:
    #                coordinate['R'] = 1150
                if coordinate['R'] >=2300:
                    coordinate['R'] = 2300
                self.motor_rotation.go_to_position(coordinate['R'])
    #            print(coordinate['R'])
            else:
                pass
       

    def run_1command(self):
        self.motor_X_axis.run_robot = True
        self.motor_Y_axis.run_robot = True
        self.motor_rotation.run_robot = True
        self.motor_gripper.run_robot = True
        self.command_counter
        try:
            test = self.command_list_keys[self.command_counter]

        except:
            pass
        else:

            self.window1.Element('_list_box_').Update(values = self.command_list_items,set_to_index = self.command_counter)
            self.move_position(self.command_list_keys[self.command_counter],self.command_list_values[self.command_counter])
            self.command_counter+=1
            if self.command_counter == len(self.command_list_keys) or self.motor_X_axis.run_robot == False or self.motor_Y_axis.run_robot == False or self.motor_rotation.run_robot == False or self.motor_gripper.run_robot == False:
                self.command_counter = 0


    def run_1cycle(self):
        self.motor_X_axis.run_robot = True
        self.motor_Y_axis.run_robot = True
        self.motor_rotation.run_robot = True
        self.motor_gripper.run_robot = True
        for (item1,item2) in zip(self.command_list_keys,self.command_list_values):
            self.move_position(item1,item2)
        
    def run_continuously(self):
        self.motor_X_axis.run_robot = True
        self.motor_Y_axis.run_robot = True
        self.motor_rotation.run_robot = True
        self.motor_gripper.run_robot = True
        while self.motor_X_axis.run_robot and self.motor_Y_axis.run_robot and self.motor_rotation.run_robot and self.motor_gripper.run_robot:
            for (item1,item2) in zip(self.command_list_keys,self.command_list_values):
                self.move_position(item1,item2) 
                

                    
    
    def run(self):

        # ------ Loop & Process button menu choices ------ #      
        while True:      
            event1, values1 = self.window1.Read(timeout=100)
           

            if event1 == 'Exit' or event1 == '_close1_':    
                self.window1.Close()
                break      
            #print('Button = ', event)      
            # ------ Process menu choices ------ #      
            if event1 == 'About...':      
                sg.Popup('About this program', 'Version 1.0', 'Python rocks...')      
        #    elif event1 == 'Open':      
        #        filename = sg.PopupGetFile('file to open', no_window=True)      
        #        print(filename)
            elif event1 == '_homing_' or event1 == 'Homing': 
                self.homing()

                
            elif event1 == '_position_combo_1_':
                position1 = values1['_position_combo_1_']


                try:
                    list_box_values = self.position_dict[position1]
                except:
                    pass
                else:
                    self.command_list_keys.append(position1)
                    self.command_list_values.append(list_box_values)
                    self.command_list_items.append(position1+' '+str(list_box_values))
                    self.window1.Element('_list_box_').Update(values = self.command_list_items)
                    
                    self.window1.Element('_X1_').Update(str(self.position_dict[position1]['X']))
                    self.window1.Element('_Y1_').Update(str(self.position_dict[position1]['Y']))
                    self.window1.Element('_R1_').Update(str(self.position_dict[position1]['R']))
                    
            elif event1 == '_gripper_combo_1_':
                gposition1 = values1['_gripper_combo_1_']

                try:
                    list_box_values1 = self.gripper_dict[gposition1]
                except:
                    pass
                else:
                    self.command_list_keys.append(gposition1)
                    self.command_list_values.append(list_box_values1)
                    self.command_list_items.append(gposition1+' '+str(list_box_values1))
                    self.window1.Element('_list_box_').Update(values = self.command_list_items) 
                    
                    self.window1.Element('_G1_').Update(str(self.gripper_dict[gposition1]))
                    
            elif event1 == '_gripperOpen_': 
                    self.command_list_keys.append('Gripper open')
                    self.command_list_values.append(0)
                    self.command_list_items.append('Gripper open'+' '+str(0))
                    self.window1.Element('_list_box_').Update(values = self.command_list_items)        
                
            elif event1 == '_list_box_':   
                try:
                    current_value = values1['_list_box_'][0]

                except:
                    pass
                else:
                    try:
                        index_list = self.command_list_items.index(current_value)
                    except:
                        pass
                    else:

                        self.command_list_keys.pop(index_list)
                        self.command_list_values.pop(index_list)
                        self.command_list_items.pop(index_list)
                        self.window1.Element('_list_box_').Update(values = self.command_list_items)
                
            elif event1 == '_teach_position_' or event1 == 'Teach Positions' and not self.window2_active:
                    self.window2_active = True
                    self.window1.Hide()
                    
                    motor_positions = GUI_motor_position(self.motor_X_axis,self.motor_Y_axis,self.motor_rotation,self.motor_gripper,
                                                         self.position_dict,self.gripper_dict,self.command_list_keys,
                                                         self.command_list_values,self.command_list_items,self.position_combo,self.gripper_combo)
                    motor_positions.run()
                    self.window1.UnHide()
             
            elif event1 == '_run_single_line_' or event1  == 'Run single line':
                self.run_1command()



            elif event1 == '_run_single_cycle_' or event1 == '_enter_position_'or event1 == 'Run single cycle':
                self.run_1cycle()
            
            elif event1 == '_run_continuously_' or event1 == '_enter_gposition_' or event1 == 'Run continuously':
                self.run_continuously()
                
            elif event1 == '_stop_robot_':        
                sg.Popup('Im am havig a feeling of...')
                
            elif event1 == 'Open' or event1 =='_open_': 
                try:
                   filename = sg.PopupGetFile('file to open', default_path = '/home/pi/Fisher_PI/Projects',default_extension ='.txt', initial_folder = '/home/pi/Fisher_PI/Projects',
                                               ) 
                except:
                    pass
                else:
                    try:
        #                open_file=open(filename,'r')
                        open_list = []
                        open_list = [line.rstrip('\n') for line in open(filename)]

                    except:
                        pass
                        print('ne printam')
                    else:
                        self.position_dict = eval(open_list[0])
                        self.gripper_dict = eval(open_list[1])
                        self.command_list_keys = eval(open_list[2])
                        self.command_list_values = eval(open_list[3])
                        self.command_list_items = eval(open_list[4])
                        self.window1.Element('_list_box_').Update(values = self.command_list_items) 

                        
                
            elif event1 == 'Save as' or event1 == '_save_':
                try:
                    filename1 = sg.PopupGetFile('file to save as', save_as = True, default_path = '/home/pi/Fisher_PI/Projects',
                                               
                                               default_extension ='.txt',
                                               initial_folder = '/home/pi/Fisher_PI/Projects')
                except:
                    pass
                else:
                    
                    try:
                        save_file=open(filename1,'w')
                    except:
                        pass
                    else:
                        save_list = str(self.position_dict)+'\n' + str(self.gripper_dict)+'\n'+str(self.command_list_keys)+'\n'+str(
                self.command_list_values)+'\n'+str(self.command_list_items)+'\n'

                        save_file.write(save_list)
                        
        #                save_file.write('{}'.format(filename))
                        save_file.close()

                
            if event1 != sg.TIMEOUT_KEY:
                pass
        #        print('Button = ', event1)
                    #window.Element('_output_').Update(event)
        self.window1.Close()
        GPIO.remove_event_detect(self.motor_rotation.counter_pin)
        GPIO.remove_event_detect(self.motor_Y_axis.counter_pin)
        GPIO.remove_event_detect(self.motor_X_axis.counter_pin)
        GPIO.remove_event_detect(self.motor_gripper.counter_pin)
        GPIO.remove_event_detect(self.stopButton_pin)

        GPIO.cleanup() 
