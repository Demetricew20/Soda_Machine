import user_interface
from customer import Customer
from soda_machine import SodaMachine


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        soda_machine.fill_inventory()
        print(soda_machine.fill_inventory())
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 0:
                soda_machine.begin_transaction(customer)
            elif user_option == 1:
                customer.check_coins_in_wallet()
            elif user_option == 2:
                customer.check_backpack()
            elif user_option == 3:
                will_proceed = False
