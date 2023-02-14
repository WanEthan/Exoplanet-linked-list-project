"""
Yu Jen Wan (Ethan)
Foothill College, CS3B, 2022
Exoplanet, displaying a list of planets and take user input to display
the modified list

"""


class ExoplanetNode:
    """Create a node for every new exoplanet"""
    id = 1001

    def __init__(self, name=None, mass=None, au=None, period=None,
                 discovery=None):
        """ Initializes ExoplanetNode objects """
        self.planet_name = name
        self.planet_mass = mass
        self.orbital_radius = au
        self.orbital_period = period
        self.discovery_date = discovery
        self.next = None
        self.id = ExoplanetNode.id
        ExoplanetNode.id = ExoplanetNode.id + 1

    def display_data(self):
        """Display readable data for each exoplanet """
        return f"ID number: {self.id} \n" \
               f"Planet_name: {self.planet_name} \n" \
               f"Mass (x of Planet): {self.planet_mass} \n"\
               f"Orbital Radius (AU): {self.orbital_radius} \n" \
               f"Orbital Period (days): {self.orbital_period} \n" \
               f"Discovery Date: {self.discovery_date} \n"

    def display(self):
        """ using recursion to display every exoplanet's
         information data """
        print(self.display_data())
        if self.next:
            self.next.display()


class UnorderedList:
    """ Linked each exoplanet node into a list and
     create a function to remove for first planet from the list

    """
    def __init__(self):
        """ Initializes UnorderedList objects """
        self.head = None

    def add(self, name=None, mass=None, au=None, period=None, discovery=None):
        """ creat a node for each exoplanet and add it into the list"""
        new_planet = ExoplanetNode(name, mass, au, period, discovery)
        new_planet.next = self.head
        self.head = new_planet

    def remove_by_id(self, id_number):
        """ remove for a planet from the list (by its ID number) """
        current_planet = self.head
        previous = None
        while current_planet is not None:
            if current_planet.id == id_number:
                break
            previous = current_planet
            current_planet = current_planet.next
        if previous is None:
            self.head = current_planet.next
        else:
            previous.next = current_planet.next

    def display_list(self):
        """ Go to each planet node and display traversing a Linked List
        by calling the recursion function

        """
        self.head.display()
        # -------- a Linked List with a Loop ------- (Another way)
        # current_planet = self.head
        # while current_planet is not None:
        #     print(current_planet.display_data())
        #     current_planet = current_planet.next
        # print()


def main():
    """ Creat an instance of unorderedList class and add five exoplanets
    into the list;
    Display all exoplanets' data in the list;


    """
    my_planet_list = UnorderedList()
    my_planet_list.add("Cancri b", 0.8306, 0.1134, 14.7, 1996)
    my_planet_list.add("Cancri c", 0.1714, 0.2373, 44.4, 2004)
    my_planet_list.add("Cancri d", 3.8780, 5.9570, 15.3*365, 2002)
    my_planet_list.add("Cancri e", "7.99 Earths", 0.01544, 0.7, 2004)
    my_planet_list.add("Cancri f", 0.141, 0.7708, 259.9, 2007)

    while True:
        print(f"Here are all exoplanets in the list \n")
        my_planet_list.display_list()
        remove_a_planet = input("Please enter an ID that you want to remove! ")
        try:
            remove_a_planet = int(remove_a_planet)  # convert str to int
        except ValueError:
            print("Please only enter ID numbers in the list, thank you!")
            continue  # ask the user to select a number again
        if remove_a_planet in range(1001, 1006):
            my_planet_list.remove_by_id(remove_a_planet)
            print()
            my_planet_list.display_list()
            break  # exit the loop
        else:
            print("This ID number is not in the list.\n")


if __name__ == "__main__":
    main()


""" ------- Sample Run -------
Here are all exoplanets in the list 

ID number: 1005 
Planet_name: Cancri f 
Mass (x of Planet): 0.141 
Orbital Radius (AU): 0.7708 
Orbital Period (days): 259.9 
Discovery Date: 2007 

ID number: 1004 
Planet_name: Cancri e 
Mass (x of Planet): 7.99 Earths 
Orbital Radius (AU): 0.01544 
Orbital Period (days): 0.7 
Discovery Date: 2004 

ID number: 1003 
Planet_name: Cancri d 
Mass (x of Planet): 3.878 
Orbital Radius (AU): 5.957 
Orbital Period (days): 5584.5 
Discovery Date: 2002 

ID number: 1002 
Planet_name: Cancri c 
Mass (x of Planet): 0.1714 
Orbital Radius (AU): 0.2373 
Orbital Period (days): 44.4 
Discovery Date: 2004 

ID number: 1001 
Planet_name: Cancri b 
Mass (x of Planet): 0.8306 
Orbital Radius (AU): 0.1134 
Orbital Period (days): 14.7 
Discovery Date: 1996 

Please enter an ID that you want to remove! 1002

ID number: 1005 
Planet_name: Cancri f 
Mass (x of Planet): 0.141 
Orbital Radius (AU): 0.7708 
Orbital Period (days): 259.9 
Discovery Date: 2007 

ID number: 1004 
Planet_name: Cancri e 
Mass (x of Planet): 7.99 Earths 
Orbital Radius (AU): 0.01544 
Orbital Period (days): 0.7 
Discovery Date: 2004 

ID number: 1003 
Planet_name: Cancri d 
Mass (x of Planet): 3.878 
Orbital Radius (AU): 5.957 
Orbital Period (days): 5584.5 
Discovery Date: 2002 

ID number: 1001 
Planet_name: Cancri b 
Mass (x of Planet): 0.8306 
Orbital Radius (AU): 0.1134 
Orbital Period (days): 14.7 
Discovery Date: 1996 


Process finished with exit code 0

"""