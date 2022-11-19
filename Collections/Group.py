from collections import defaultdict
import copy
import random
import logging

logging.basicConfig(level=logging.ERROR)

"""group
Groups true means symmetrical pairing.

Keyword arguments:
domain -- the list to group
codomain -- if you want to group domain values with another set
exclusion -- groupings to forbid
symmetric - whether pairings should apply in both directions
"""


def group(domain, codomain=None, exclusion=None, symmetric=False):
    if exclusion is None:
        exclusion = defaultdict(list)
    '''if size < 2:
        size = 2
    if size > 2:
        groups = False
        exclusion = defaultdict(list) #remove this when implemented
        symmetric = False
        if codomain == None:
            print("Cannot assign multiples over one group.")
            return
        if len(codomain) != (size - 1 ) * len(domain):
            print("Size issues")
            return'''

    if codomain is None:
        codomain = copy.deepcopy(domain)

    results = defaultdict(list)
    print(domain)
    for each in domain:
        print(each)
        for _ in range(1):
            if (codomain != exclusion[each] + [each]
                and codomain != [each]
                    and codomain != exclusion[each]):

                person = random.choice(codomain)
                while person in exclusion[each] + [each]:
                    person = random.choice(codomain)
                print(each, person)
                results[each].append(person)
                codomain.remove(person)
                '''if symmetric:
                    results[person].append(each)
                    domain.remove(each)'''
            else:
                raise Exception('No possible transitions')

    return results


if __name__ == "__main__":
    import doctest
    doctest.testmod()
