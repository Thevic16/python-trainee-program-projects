from packages.administration.admin_logic import AdminLogic
from packages.administration.admin_print import AdminPrint
from packages.auxiliary.storage_functions import load_data_from_json_file
from packages.auxiliary.storage_functions import save_data_as_json_file


if __name__ == '__main__':
    print("-> Write 'help' to see all the commands.")
    print("-> Remember to call the command 'EOF' "
          "to exit the program successfully.")

    load_data_from_json_file()

    admin_print = AdminPrint()
    admin_print.cmdloop()

    admin_logic_list = AdminLogic.get_admin_logic_as_list()
    print(f'Admin Json Representation: {admin_logic_list}')
    save_data_as_json_file(admin_logic_list)
