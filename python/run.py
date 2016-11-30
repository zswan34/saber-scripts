#!/usr/bin/python
import saber

saber.initialize()
saber.print_welcome()

# options
saber.print_primary_options()
opt = saber.smart_input("> ")

while opt != "99":
    if opt == "1":
        saber.print_secondary_options()
        opt = saber.smart_input("> ")

    elif opt == "2":
        saber.print_secondary_options()
        opt = saber.smart_input("> ")

    elif opt == "3":
        print "3"

    elif opt == "99":
        print "4"

    else:
        print "I don't understand...\n"
        saber.print_options()
        opt = saber.smart_input("> ")
