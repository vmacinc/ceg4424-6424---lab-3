============ IRC bot =================
requirement: This is a IRC-bot python2 program. So, you have to install the python2 in you system.
             For windows user,
                1) Open you brower can go here: https://www.python.org/downloads/release/python-2711/
                2) Download the "Windows x86 MSI installer" and then installing the python2 by double clicked the installer.
                3) Following this video to add python and pip to you PATH: https://www.youtube.com/watch?v=UTUlp6L2zkw

             For linux user, Please open you terminal and:
                1) insert this command "sudo apt-get update" and then type Enter.
                2) insert command "sudo apt-get install python", type Enter.
                3) insert command "sudo apt-get install python-pip", type Enter.

             After initializing your environment you need install a python libray named "psutil".
             For window user:
                I highly recommend the "PyCharme" as your IDE during this project. You can install the psutil library in your PyCharm.
                Click: File -> Setting -> Project:irc_project -> Project Interpreter
                You can see the library list in your interpreter and then click the "+" on the right top corner.
                You need search "psutil" as the key words in the pop-up window. Then click the "install package" in the left bottom corner.

             For Linux user:
                insert command "pip install psutil" in your terminal and type Enter.


IRC server: 1) Open a web browser and copy paste the following url: https://webchat.freenode.net
            2) type a nick name you like, such as bot_master, in "Nick" frame
            3) copy and paste "##RussIRCbotTesting" in "Channel" frame
               (Hint: Please customized the Channel name and the variable "channel" in your code as "##somethingyoulike". Otherwise, all of you will join to a same channel)
            4) DON'T check the password

IRC Client:  For Windows User: try to run the main.py in your IDE
             For Linux User: open you terminal and go to your code directory and run this command "python main.py"

Develop your bot: I have already hard code two command system and memory in the bot. You can add your own command.

Good Luck! Fingers are crossed!

