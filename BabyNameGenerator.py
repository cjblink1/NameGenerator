'''BabyNameGenerator module'''
import random
from Generator import Generator
from CategoryPickingBehavior import CategoryPickingBehavior
class BabyNameGenerator(Generator):
    '''BabyNameGenerator class. Generates baby names.'''

    def __init__(self):
        super(BabyNameGenerator, self).__init__()
        self.pair_picking_behavior = CategoryPickingBehavior()
        self.middle_names = ['Joshua', 'Dudley', 'McDonald', 'Apple', 'Moon', 'Rose', 'Princess', 'Lily']


    def get_total_combinations(self):
        '''Returns the total number of combinations that the generator will generate.
        The Generator subclass must override this method'''
        return 40

    def get_category_names(self):
        '''Returns the manes of the categories that the generator will pick from.
        The Generator subclass must override this method'''
        return ['first names', 'last name']

    def get_num_words_per_category(self):
        '''Returns a list that containes the number of words in each category that the generator will pick from.
        The Generator subclass must override this method'''
        return [5, 1]

    def concatenate_name(self, *words):
        '''Returns a generated name.
        The Generator subclass must override this method'''
        return words[0]+" "+random.choice(self.middle_names)+" "+words[1]