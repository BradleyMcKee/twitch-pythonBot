import socket,string
from crappysocket import *

# Method for sending a message
def Send_message(message):
    s.send("PRIVMSG #creepytrash :" + message + "\r\n")

while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        # Checks whether the message is PING because its a method of Twitch to check if you're afk
        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])
        else:
            # Splits the given string so we can work with it better
            parts = string.split(line, ":")

            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    # Sets the message variable to the actual message sent
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""
                # Sets the username variable to the actual username
                usernamesplit = string.split(parts[1], "!")
                username = usernamesplit[0]

                # Only works after twitch is done announcing stuff (MODT = Message of the day)
                if MODT:
                    print username + ": " + message

                    # You can add all your plain commands here
                    if message == "Hey":
                        Send_message("Welcome to my stream, " + username)

                    if message == "idk":
                        Send_message("if u don't know then I don't know")

                for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True
