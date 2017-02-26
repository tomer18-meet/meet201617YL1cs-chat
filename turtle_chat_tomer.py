#Tomer

import turtle
from turtle_chat_client import Client
from turtle_chat_widgets import Button, TextInput

class TextBox(TextInput):
    def draw_box(self):
        new_t = turtle.clone()
        new_t.hideturtle()
        new_t.penup()
        new_t.goto(-100,-100)
        new_t.pendown()
        new_t.goto(100,-100)
        new_t.goto(100,-50)
        new_t.goto(-100,-50)
        new_t.goto(-100,-100)
    def write_msg(self):
        turtle.hideturtle()
        turtle.penup()
        c=-60
        self.writer.goto(-95,-60)
        self.writer.clear()            
        self.writer.write(self.new_msg)
##        while
##            if len(self.new_msg)>=25:
##                turtle.goto(-95,c-10)
##                b=self.new_msg[0:10] + '\r' + self.new_msg[10:]
##                turtle.clear()            
##                turtle.write(b)
##                c=c-5
##            else:
##                turtle.clear()            
##                turtle.write(self.new_msg)
##           
class SendButton(Button):
    def __init__(self,view):
        super(SendButton,self).__init__(my_turtle=None,shape=None,pos=(0,0))
        self.view=view
        self.RealBotton()

    def RealBotton(self):
        write_SB = turtle.clone()
        write_SB.hideturtle()
        write_SB.pencolor("red")
        write_SB.penup()
        write_SB.write('send here','send here')
        write_SB.onclick(self.fun)
        turtle.listen()
        
    def fun(self,x=None,y=None):
        #View.write_SB()
        self.view.send_msg()
       
##################################################################
#                             View                               #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.
#
#Read the comments below for hints and directions.
##################################################################
##################################################################

class View:
    _MSG_LOG_LENGTH=6 #Number of messages to retain in view
    _SCREEN_WIDTH=300
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,tomer='Me',partner_name='Partner'):
        self.username = tomer
        self.partner_name = partner_name
        #my_client = ()
        self.my_client = Client()
        '''
        :param username: the name of this chat user
        :param partner_name: the name of the user you are chatting with
        '''
        ###
        #Store the username and partner_name into the instance.
        ###

        #Make a new client object and store it in this instance.

        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.
        
        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.msg_queue=[]

        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###
        turtle_writes=turtle.clone()
        self.turtle_writes=turtle_writes
        
        ###
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###
        self.my_textbox=TextBox()
        self.my_sendbutton=SendButton(self)
        
        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###

    def send_msg(self):
        self.my_client.send(self.my_textbox.new_msg)
        self.msg_queue.append(self.my_textbox.new_msg)
        self.my_textbox.clear_msg()
        self.display_msg()
        
        
        '''
        You should implement this method.  It should call the
        send() method of the Client object stored in this View
        instance.  It should also call update the list of messages,
        self.msg_queue, to include this message.  It should
        clear the textbox text display (hint: use the clear_msg method).
        It should call self.display_msg() to cause the message
        display to be updated.
        '''
        

    def get_msg(self):
        return self.textbox.get_msg()

    def setup_listeners(self):
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''
        pass

    def msg_received(self,msg):
        
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''
        print(msg) #Debug - print message
        show_this_msg=self.partner_name+' says:\r'+ msg
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
        #
        #Then, call the display_msg method to update the display
        self.msg_queue.append(show_this_msg)
        self.display_msg()

    def display_msg(self):
        self.turtle_writes.clear()
        self.turtle_writes.write(self.msg_queue[-1])

        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''
            
##############################################################
##############################################################


#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################
if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        msg_in=my_view.my_client.receive()
        if not(msg_in is None):
            if msg_in==my_view.my_client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()
    
