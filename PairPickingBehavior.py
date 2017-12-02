'''PairPickingBehavior module'''
# pylint: disable = W0613, R0903, R0201
class PairPickingBehavior(object):
    '''PairPickingBehavrior class. This is an abstract class which must be overridden.'''

    def pick_pair(self, words_in_each_category):
        '''Returns a random pair of words.
        The PairPickingBehavior must override this method.'''
        raise NotImplementedError("pick_pair() should be overridden in a Generator subclass")
