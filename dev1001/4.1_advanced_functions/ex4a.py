# map() Exercises
#
# Exercise 1
# ----------
# You have a list of product prices.
# Use `map` and a lambda to create a new list where each price
# has a 20% tax added to it (price * 1.20).
# Remember to format the output nicely if you can
# (e.g., to two decimal places, but the core is the map).

prices = [10.99, 5.49, 20.00]

# def tax_price(p):
#     return p * 1.20

# new_price = map (tax_price , prices)
# print(f'Final price: {list(new_price:.2f)}')

# print (prices)

prices_plus_tax = list(map(lambda price: round(price *1.2, 2), prices))
print(prices_plus_tax)


# Exercise 2
# ----------
# Given a list of scores, use map() to get a list of the grade level for each score.
#
# HD if >=90
# D if >=80
# C if >=70
# P if >=50
# F if <50

scores = [85, 92, 78, 60, 42, 95, 70, 53]

def scores_to_grade(scores):
    '''takes a numeric score (0-100) and returns the corresponding grade (HD,D,C,P,F)'''
    if scores >= 90:
        return 'HD'
    elif scores >= 80:
        return 'D'
    elif scores >= 70:
        return 'C'
    elif scores >= 50:
        return 'P'
    else:
        return 'F'
    
# print(score_to_grade(76))

grades = list(map(scores_to_grade, scores))
print(scores)
print(grades)