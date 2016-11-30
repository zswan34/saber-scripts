#!/usr/bin/python
import saber

saber.initialize()
saber.print_welcome()

# options
saber.print_primary_options()
opt = saber.smart_input("> ")

while opt != "4":
    if opt == "1":
        print "1"

    elif opt == "2":
        print "2"

    elif opt == "3":
        print "3"

    elif opt == "4":
        print "4"

    else:
        print "I don't understand...\n"
        saber.print_options()
        opt = saber.smart_input("> ")
