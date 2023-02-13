import random
when = ['A few years age', 'Yesterday', 'Last night', 'A long time age', 'On 20th Jan']
who = ['a rabit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'marim', 'danial', 'Hoouk', 'Starwalker']
residence = ['Barcelone', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundary']
happend = ['made a lote of friends', 'Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) +'that lived in' + random.choice(residence) + ', went to the' + random.choice(went) + ' and ' +random.choice(happend))