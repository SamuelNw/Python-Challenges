"""
    In a small town the population is p0 = 1000 at the beginning of a year.
    The population regularly increases by 2 percent per year and
    moreover 50 new inhabitants per year come to live in the town.
    How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
    parameters ---> p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
    the function nb_year should return n number of entire years needed to get a population greater or equal to p.

"""

def nb_year(p0, percent, aug, p):
    n = 0
    while p > p0:

        summation = p0 + int(p0 * float(percent / 100)) + aug
        p0 = summation
        n += 1

    print(f"It will take {n} years")


nb_year(1500000, 0.25, 1000, 2000000)
