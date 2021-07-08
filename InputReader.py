class InputReader:

    def readInput(args):
        image_path = ""
        extension = ""
        output_path = ""
        number_of_outputs = 1
        properties = []
        parameters = []

        #--take input here--#

        image_path = args.input
        extension = args.input.split('.')[-1]
        output_path = args.o
        number_of_outputs = args.n
        properties = args.p
        parameters = args.l

        if number_of_outputs == None:
            number_of_outputs = 1

        return (image_path, extension, output_path, number_of_outputs, properties, parameters)