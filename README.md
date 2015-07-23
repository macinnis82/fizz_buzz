Project Requirements

- Have a hard-coded upper line, n.
- Print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
- Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
- Print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen).
- Each number should be printed on a new line.

Extra Challenge

Create a second version of your FizzBuzz program which has a user-supplied upper limit.

If the user supplies a value at the command line when script runs, we'll use that value.
Otherwise, we'll use the raw_input() function to get a value from the user.

Extension exercise

Earlier in the lesson you learned about exception handling. 
Practice this skill by writing code that handles users supplying non-numeric inputs to either sys.argv or raw_input(). 
First you should figure out where this user behavior would raise an exception in your code, 
then use a try/except block to catch it. 
When you catch the error you should print a message telling the user that they need to supply numeric inputs, 
then use raw_input() to ask for a new value.
