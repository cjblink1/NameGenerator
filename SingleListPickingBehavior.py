'''SingleListPickingBehavior module'''
# pylint: disable = R0903
import random
from PairPickingBehavior import PairPickingBehavior
class SingleListPickingBehavior(PairPickingBehavior):
    '''SingleListPickingBehavior class. Picks two random words from all of the categories.'''

    def pick_pair(self, words_in_each_category):
        '''Returns a random pair of words.
        The PairPickingBehavior must override this method.'''
        all_words = []
        for category in words_in_each_category:
            all_words.extend(category)

        first_word_choice = random.choice(all_words)
        # all_words.remove(first_word_choice)
        second_word_choice = random.choice(all_words)

        return (first_word_choice, second_word_choice)
