
import numpy as np
import matplotlib as plt

class Charge:
    """a charge object defined by its position and
    charge"""
    def __init__(self, xpos=None, ypos=None,
                 charge=None):
        self.xpos = xpos
        self.ypos = ypos
        self.charge = charge

class Potential:
    """a potential object defined by a list of charges"""
    def __init__(self, charges=None, #<--list_of_charge_objects,
                 x_values=None, y_values=None):
        self.charge_list = list_of_charge_objects
        self.x_values = x_values
        self.y_values = y_values
        self.potential = self.calculate_total_potential(self.charge_list)

    def calculate_total_potential(self):
        potential = 0
        for charge in self.charge_list:
            charge_xpos = charge.xpos #<--example of how to
            charge_ypos = charge.ypos
            phi =  ((charge)/(4*3.14*(8.85*10**-12)(0- xpos))) * ((charge)/(4*3.14*(8.85*10**-12)(0- ypos))) #<--function that calculates potential of a charge
            
class Electric_field:
    """an electric field object defined by a potential"""
    def __init__(self, potential=None):
        self.potential = potential
        Electric_field = -(np.gradiant*phi)
        #keep filling this in

if __name__ == "__main__":
    Charge1 = Charge(xpos=-0.05, ypos=0, charge=1)
    Charge2 = Charge(xpos=0.05, ypos=0, charge=1)
    #generate x,y values
    spacing = 0.01 #<--spacing 0.01 m = 1 cm
    x_range = np.arange(-0.5, 0.5, spacing)
    y_range = np.arange(-0.5, 0.5, spacing)
    xs, ys  = np.meshgrid(x_range, y_range)
    print('X coordinates')
    print(xs)
    print('Y coordinates')
    print(ys)

#question a
    plt.imshow(xs, ys, phi)
    plt.colorbar()
    plt.show()
                                    
#question b
    phi = solve(
    plt.quiver()
    plt.show()
