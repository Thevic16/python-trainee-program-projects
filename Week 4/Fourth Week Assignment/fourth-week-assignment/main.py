from packages.administration.admin_logic import AdminLogic
from packages.administration.admin_print import AdminPrint

if __name__ == '__main__':
    print("-> Write 'help' to see all the commands.")
    print("-> Remember to call the command 'EOF' "
          "to exit the program successfully.")

    AdminLogic.setup_database('URL_DATABASE')
    admin_print = AdminPrint()
    admin_print.cmdloop()
