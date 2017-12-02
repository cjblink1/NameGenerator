'''StreetNameGenerator module'''
import random
from Generator import Generator
from SingleListPickingBehavior import SingleListPickingBehavior
class StreetNameGenerator(Generator):
    '''StreetNameGenerator class.'''

    def __init__(self):
        super(StreetNameGenerator, self).__init__()
        self.pair_picking_behavior = SingleListPickingBehavior()
        self.street_suffixes = ['Street', 'Avenue', 'Place', 'Court', 'Drive', 'Road']

    def get_total_combinations(self):
        '''Returns the total number of combinations that the generator will generate.
        The Generator subclass must override this method'''
        return 8*6

    def get_category_names(self):
        '''Returns the manes of the categories that the generator will pick from.
        The Generator subclass must override this method'''
        return ['presidents', 'dog species', 'tree species']

    def get_num_words_per_category(self):
        '''Returns the number of words in each category that the generator will pick from.
        The Generator subclass must override this method'''
        return [4, 2, 2]

    def concatenate_name(self, *words):
        '''Returns a generated name.
        The Generator subclass must override this method'''
        return (words[0]+" "+random.choice(self.street_suffixes)).title()
