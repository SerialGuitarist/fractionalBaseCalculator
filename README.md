# Fraction Base Calculator
Conversion of a fraction in base 10 into specified base


This is a small python code to convert any fraction in base 10, given as numerator and denominator, into any specified base. 

So for example: 355/113, an approximation of pi, would be:
* 11.0010010000 in base 2
* 10.0102110122 in base 3
* 3.0210033312 in base 4
* 3.1415929203 in base 10
* 3.243F6F0243 in base 16


For bases higher than 10, by default, the ```defaultDigits``` list is used to for the digits, which goes like: 0, 1, 2, ... , 8, 9, A, B, C, ... , X, Y, Z, a, b, c, ..., x, y, z. This means by default, the provided function can calculate until base 62.

There are 2 functions: ```fractionBase``` and ```integerBase```. The ```integerBase``` is a basic whole number conversion from base 10, meant to be used inside ```fractionBase```, though can be used independently.

\
I wrote this code because I was curious about how base 10 compares to other bases, when it came to fractional numbers. Base 10 isn't the greatest when it comes to terminating fractions, as its multiples are only 1, 2, 5, and 10, so fractions whose denominator is a composite of those numbers can terminate, without repeating forever: such as 1/2, 1/4, 1/5, 1/10, 1/20, etc etc. But all other denominators, (eg 1/3, 1/6, 1/9, 1/11, etc etc) will repeat forever. So the aim was to figure out how well
some other bases, especially antiprime bases fare in terms of the number of fractions with denominators that repeat forever, resulting in [this spreadsheet]( https://docs.google.com/spreadsheets/d/124ePZxX5gBPvQg7ZtS0qGDLzEbNZM1jRrBb3h43OSx4/edit?usp=sharing), showing that within fractions between 1/2 and 1/60, bases 6, 30, and 60 has some of the highest terminations
    
