from spy_details import spy, Spy, ChatMessage, friends,spy_name
from steganography.steganography import Steganography
from colour import color_scale
from datetime import datetime

STATUS_MESSAGES = ['name cool boy', 'avilable', 'im busy text me plz', 'dont text,Sir']

print("hiiiii welcome too spy chat application")
print("***********")
#providing a option to user to select a pre information.
menu=raw_input("do u want to countine as " +spy_name+"( y/n ):")

choice=raw_input(menu)

def add_status():
    # def is a keyword used for declearing a function

    updated_status_message = None #till now we dont updated our status so we put null

    if spy.current_status_message != None: #if spy current status is not null

        print 'Your current status message is %s \n' % (spy.current_status_message) #we have to print his\her status


    default = raw_input("Do you want to select from the older status (y/n)? ") #here we are asking user to select the status from the previous one

    if default.upper() == "N":# upper() function is used to conver the lower input to upper charcter and upper remains same
        new_status_message = raw_input("What status message do you want to set? ")# enter new status


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)# we are appending our new status to the status msg that is our list which is storing our status
            updated_status_message = new_status_message
        else:
            print"plz enter the vaild status dont blank"

    elif default.upper() == 'Y':# if user wants too selct status from the list that is STATUS_MESSG

        item_position = 1 # its is like a pointer which is pointing the position

        for msg in STATUS_MESSAGES: # here we use for loop
            print '%d. %s' % (item_position, msg)
            item_position = item_position + 1 #increment

        message_selection = int(raw_input("\nChoose from the above messages "))  #here we taking a input from user and raw input store that input as string so we are converting it in integer bt using int


        if len(STATUS_MESSAGES) >= message_selection: #here we are checking the length of a list and input given by user in msg_selection
            updated_status_message = STATUS_MESSAGES[message_selection - 1] #here we use msg_selection-1 because in list index it start from 0 so we use this.

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

def add_friend(): # here we have made a function named add_friend

    new_friend = Spy('','',0,0.0)
    # we just have too asking user all info about his frd
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend) #append or the new frd in the list that is friends
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1
        # above we just use for loop to print all friend which are in list
        #rember list alwys start with 0 which is index

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1
    #above frind_choice_postion in list its index wholud nbe caluclate by minus 1

    return friend_choice_position

def send_message():
    # now we have to encypt the text in image which is also called steanography

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "decod.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text) #here we are encrypting the msg the text

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path) #decoding
    print (secret_text)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been save"


def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print("\033[1;32;40m Bright Green  \n")
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print("\033[1;32;40m Bright Green  \n")
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True #True AND False are the boolean in oython python is case sensetive laungaug so T AND F should be in capital

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

def first_spy(spy):

    # user want too creat a new file.sp take a input from user
    # Input new user details
    # Start Chat Application 1
    # Start Chat Application 2
    # Start Chat Application 3
    # Start Chat Application 4
    spy = Spy('', '', 0, 0.0)

    spy_name = raw_input("enter ur name plz")
    if len(spy_name) > 0:
        print spy_name
        spy_salulation = raw_input("what sholud we call you mr or miss")
        print("welcome " + spy_salulation + spy_name + "we are glad too have you back......")
        spy.age = 0
        spy_is_online = False  # python is case sensitive launguage so in False f should be in capital
        spy_rating = 0.0
        spy.age = raw_input("please enter your age")
        spy.age = int(
            spy.age)  # here we have to do casting because raw_input always store a string value so we have to convert it ito integers
        if spy.age > 12 and spy.age < 50:
            # and  or are the logical opreator so they are written as they are.
            print("enter your further details please")
            spy_rating = raw_input("please enter whats ur rating")
            # now through spy_rating we have to comment the user.
            if spy_rating > 4.5:
                print ("great ace!!!")
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print("you are agood one")
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print("you can be a good spy")
            else:
                print("we always use some one in office")
            spy_is_online = True
            print("authenication complete")
            print("welcome" + spy_name + "your age is" + str(spy.age) + "and ur spy rating is" + str(spy_rating))

        else:
            print("you are not allowed to use spy_chat")

        start_chat(spy)  # calling start_chat function

    else:
        print("enter ur name please and try again")
        first_spy(spy) #we cAll first_spy function beacuse it not edd the application if user enter null in name than it restart again.


if menu=="y":
    start_chat(spy)

else:
    first_spy(spy)












