'''CategoryPickingBehavior module'''
# pylint: disable = R0903
import random
from PairPickingBehavior import PairPickingBehavior
class CategoryPickingBehavior(PairPickingBehavior):
    '''CategoryPickingBehavior class. Picks a pair according to the first two categories.'''

    def pick_pair(self, words_in_each_category):
        '''Returns a random pair of words.
        The PairPickingBehavior must override this method.'''
        first_word_choice = random.choice(words_in_each_category[0])
        second_word_choice = random.choice(words_in_each_category[1])
        return (first_word_choice, second_word_choice)
