'''Main module for NameGeneratior appliction'''
# pylint: disable=R0903
from Generator import Generator
from BandNameGenerator import BandNameGenerator
class Application(object):
    '''Entry class for the NameGeneratior application'''

    def __init__(self, generators):
        self.generators = generators

    def main(self):
        '''Entry method for the NameGeneratior application'''
        print "Which generator would you like to use?"
        print self.generators.keys()
        for key in self.generators.keys():
            print key

        user_selection = raw_input()

        print "You entered: ", user_selection

        while not self.generators.has_key(user_selection):
            print user_selection, " is not a valid generator."
            print "Which generator would you like to use?"

            for key in self.generators.keys():
                print key

            user_selection = raw_input()

        selected_generator = self.generators[user_selection]
        selected_generator.generate_names()


GENERATORS = {'Band Name': BandNameGenerator()}
APP = Application(GENERATORS)
APP.main()
