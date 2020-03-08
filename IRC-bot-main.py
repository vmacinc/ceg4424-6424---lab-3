#!/usr/bin/python
import socket
import time
import platform
import psutil
from datetime import datetime

# variable for irc server
server = "irc.freenode.net"
botnick = "Abot"
channel = "##bot-channel"

# system information
system, node, release, version, machine, processor = platform.uname()

# cpu frequence
cpufreq = psutil.cpu_freq()

# Memory infomation
svmem = psutil.virtual_memory()

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.setblocking(False)
time.sleep(1)
ircsock.send("USER " + botnick + " " + botnick + " " + botnick + " :Hello! I am a test bot!\r\n")
time.sleep(1)
ircsock.send("NICK " + botnick + "\n")
time.sleep(1)
ircsock.send("JOIN " + channel + "\n")

def sendmsg(msg, target=channel):   # send message to the IRC server
    ircsock.send("PRIVMSG " + target + " :" + msg + "\n")

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024.0
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            res = round(bytes,2)
            return str(res) + unit + suffix
        bytes /= factor

# system and cup info
def sys_info():
    return "System: {}".format(system)
def machine_info():
    return "Machine: {}".format(machine)
def processor_info():
    return "Processor: {}".format(processor)
def frequence():
    # CPU frequencies
    return "Max Frequency : {}Mkz".format(round(cpufreq.max,2))

# Memory infomation
def totalM ():
    return "Total Memory: {}".format(get_size(svmem.total))
def AvailableM():
    return "Available: {}".format(get_size(svmem.available))
def UsedM():
    return "Used: {}".format(get_size(svmem.used))
def PercentM():
    return "Percentage: {}%".format(svmem.percent)


def main():
    while True:
        time.sleep(0.1)
        ircmsg = ""
        try:
            ircmsg = ircsock.recv(2040)
            # ircmsg = ircmsg.strip('nr')
            print ircmsg
        except Exception:
            pass
        if ircmsg.find("PING") != -1:
            ircsock.send("PONG " + ircmsg.split()[1] + "\r\n")
        if ircmsg.lower().find(":@hi") != -1:
            ircsock.send("PRIVMSG " + channel + " :Hello!\r\n")

        if ircmsg.find("PRIVMSG") != -1:
            # print ircmsg
            name = ircmsg.split('!', 1)[0][1:]
            message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]
            # print name
            # print message
            if len(name) < 17:
                if message.find('Bye ' + botnick) != -1:
                    sendmsg("Okay...Bye!")
                    ircsock.send("QUIT\r\n")
                    return

                if message.find('Hi ' + botnick) != -1:
                    sendmsg("Hello " + name + "!")

                if message.find('system') != -1:
                    msg = sys_info()
                    sendmsg(msg)
                    msg = machine_info()
                    sendmsg(msg)
                    msg = processor_info()
                    sendmsg(msg)
                    msg = frequence()
                    sendmsg(msg)

                if message.find('memory') != -1:
                    msg = totalM()
                    sendmsg(msg)
                    msg = AvailableM()
                    sendmsg(msg)
                    msg = UsedM()
                    sendmsg(msg)
                    msg = PercentM()
                    sendmsg(msg)
					
				if message.find('All Bots report in!') != -1:
                    sendmsg("Bot " + botnick + "reporting in!")
				
				if message.find('test') != -1:
					sendmsg(botnick + " - got it")
					
				if message.find('test1') != -1:
					sendmsg(botnick + " - got it again")
				
								
main()