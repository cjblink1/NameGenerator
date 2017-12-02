'''BandNameGenerator module'''
from Generator import Generator
from CategoryPickingBehavior import CategoryPickingBehavior
class BandNameGenerator(Generator):
    '''BandNameGenerator class generates a name for a band'''

    def __init__(self):
        super(BandNameGenerator, self).__init__()
        self.pair_picking_behavior = CategoryPickingBehavior()

    def get_total_combinations(self):
        '''Returns the total number of combinations that the generator will generate.
        The Generator subclass must override this method'''
        return 25

    def get_num_categories(self):
        '''Returns the number of categories that the generator will pick from.
        The Generator subclass must override this method'''
        return 1

    def get_category_names(self):
        '''Returns the manes of the categories that the generator will pick from.
        The Generator subclass must override this method'''
        return ['adjective', 'animal']

    def get_num_words_per_category(self):
        '''Returns the number of words in each category that the generator will pick from.
        The Generator subclass must override this method'''
        return 5

    def concatenate_name(self, *words):
        '''Returns a generated name.
        The Generator subclass must override this method'''
        return ('The '+words[0]+' '+words[1]+'s').title()
