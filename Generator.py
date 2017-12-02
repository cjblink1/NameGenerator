'''Generator module'''
# pylint: disable=W0613
# pylint: disable=R0201
from SingleListPickingBehavior import SingleListPickingBehavior
class Generator(object):
    '''Generator class'''

    def __init__(self):
        self.pair_picking_behavior = SingleListPickingBehavior()
        self.category_names = []
        self.increment = 10

    def generate_names(self):
        '''This method is the 'Template Method' for Generators.'''
        self.category_names = self.get_category_names()
        num_categories = len(self.category_names)

        words_for_each_category = []

        for i in range(num_categories):
            words_for_each_category.append(self.get_words_for_category(i))

        names_generated = []
        user_response = ''
        total_combinations = self.get_total_combinations()
        while user_response != 'n':
            i = 0
            while i < self.increment and len(names_generated) < total_combinations:
                words = self.pair_picking_behavior.pick_pair(words_for_each_category)
                name_generated = apply(self.concatenate_name, words)
                if name_generated not in names_generated:
                    print name_generated
                    names_generated.append(name_generated)
                    i = i + 1

            user_response = raw_input("\nWould you like to generate more names? [Y/n]")

    def get_words_for_category(self, category_num):
        '''Prompts the user for words in a particular category.'''
        words_in_this_category = []
        num_words_required = self.get_num_words_per_category()[category_num]

        print "\nPlease enter", num_words_required, self.category_names[category_num], ":"
        for _ in range(num_words_required):
            words_in_this_category.append(raw_input())
        return words_in_this_category

    def is_plural(self, word):
        '''Returns True if word is plural. Otherwise returns False'''
        return word.endswith('s') or word.endswith('es')

    def pick_pair(self, words_in_each_category):
        '''The Strategy pattern is used here. Delegate the task of picking pairs to a
        particular PairPickingBehavior.'''
        return self.pair_picking_behavior.pick_pair(words_in_each_category)

    def get_total_combinations(self):
        '''Returns the total number of combinations that the generator will generate.
        The Generator subclass must override this method'''
        raise NotImplementedError("get_num_categories() should be "+
                                  "overridden in a Generator subclass")

    def get_category_names(self):
        '''Returns the names of the categories that the generator will pick from.
        The Generator subclass must override this method'''
        raise NotImplementedError("get_category_names() should be "+
                                  "overridden in a Generator subclass")

    def get_num_words_per_category(self):
        '''Returns a list that containes the number of words in each category
        that the generator will pick from.
        The Generator subclass must override this method'''
        raise NotImplementedError("get_num_words_per_category() should be "+
                                  "overridden in a Generator subclass")

    def concatenate_name(self, *words):
        '''Returns a generated name.
        The Generator subclass must override this method'''
        raise NotImplementedError("concatenate_name() should be overridden in a Generator subclass")
