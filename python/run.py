#!/usr/bin/python
import saber

saber.initialize()
saber.print_welcome()

# options
saber.print_primary_options()
opt = saber.smart_input("> ")

while opt != "99":
    # Auto correlate
    if opt == "1":
        saber.print_secondary_options()
        opt2 = saber.smart_input("> ")

        while opt2 != "99":
            # Find OH 1.6 & OH 2.0 Correlations

            if opt2 == "1":
                print "1"
            elif opt2 == "2":
                print "2"
            else:
                print "I don't understand...\n"
                saber.print_secondary_options()
                opt2 = saber.smart_input("> ")

    # Manual correlate
    elif opt == "2":
        saber.print_secondary_options()
        opt2 = saber.smart_input("> ")
        while opt2 != "99":
            # Find OH 1.6 & OH 2.0 Correlations
            if opt2 == "1":
                oh16 = saber.get_and_check_file()
                oh20 = saber.get_and_check_file()
                oh16 = saber.strip_contents(oh16)
                oh20 = saber.strip_contents(oh20)
                name = saber.save_file_as()
                saber.ShowProgress = True
                results = saber.find_duplicates(oh16, oh20, "Starting")
                formatted = saber.format_list(results)
                saber.cwd()
                saber.manage_data_directory("1620")
                saber.save_to_file("Correlations/OH16_20/CSV/" + name + ".csv", formatted)
                saber.save_to_file("Correlations/OH16_20/TXT/" + name + ".txt", formatted)
                opt2 = "99"
            # Find OH 1.6 & OH 2.0 & 02 Correlations
            elif opt2 == "2":
                oh16 = saber.get_and_check_file()
                oh20 = saber.get_and_check_file()
                o2 = saber.get_and_check_file()
                oh16 = saber.strip_contents(oh16)
                oh20 = saber.strip_contents(oh20)
                o2 = saber.strip_contents(o2)
                name = saber.save_file_as()
                saber.ShowProgress = True
                oh = saber.find_duplicates(oh16, oh20, "Finding OH 1.6 & 2.0 correlations.")
                results = saber.find_duplicates(oh, o2, "Finding OH 1.6, 2.0 & O2 correlations.")
                formatted = saber.format_list(results)
                saber.cwd()
                saber.manage_data_directory("O2")
                saber.save_to_file("Correlations/OH16_20_O2/CSV/" + name + ".csv", formatted)
                saber.save_to_file("Correlations/OH16_20_O2/TXT/" + name + ".txt", formatted)
                opt2 = "99"
            else:
                print "I don't understand...\n"
                saber.print_secondary_options()
                opt2 = saber.smart_input("> ")
    # Help
    elif opt == "3":
        print "3"
    # Quit
    elif opt == "99":
        print "[!] Script ended..."

    else:
        print "I don't understand...\n"
        saber.print_primary_options()
        opt = saber.smart_input("> ")
        if opt == "99":
            print "[!] Script ended..."
