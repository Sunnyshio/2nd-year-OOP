# program that accepts the dimensions of a 3D shape (right-cyliner and sphere) and prints its volume

class Shape:
    # Constructor method to process the given object: dimension
    def __init__(self, *argument):
        self.dimension = argument

    # printVolume method: code to process/calculate the volume of the given dimension/s
    def printVolume(self):
        if len(self.dimension) == 2:
            volume = (3.14159 * ((self.dimension[0] / 2) ** 2) * self.dimension[1])
            if volume == 0 or volume <= 0:  # Prints the output if the result is equal to zero or a negative integer
                print("Shape Volume Error!")
            else:  # Prints the output if the result is a positive integer
                print("{:.1f}".format(volume))
        elif len(self.dimension) == 1:  # Processes the input if there is only one argument
            volume = (4 / 3) * 3.14159 * ((self.dimension[0] / 2) ** 3)
            print("{:.1f}".format(volume))

        # Processes entered inputs that are more than 2 arguments
        else:
            print("Shape Volume Error!")
