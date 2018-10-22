# Listing 1-5. Example code for multiline statements
# Example of implicit line continuation

x = ('1' + '2' +
     '3' + '4')
# Example of explicit line continuation

y = '1' + '2' + \
    '11' + '12'
weekdays = {'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday'}
weekend = {'Saturday',
           'Sunday'}
print(('x has a value of', x))
print(('y has a value of', y))
print(weekdays)
print(weekend)
