######################################################################
# Author: Rodolfo Alvarado, Dimitrios Ntentia
# Username: Alvaradoreyesr2, Ntentiad
#
# Assignment: T07 Mad Libs
#
# Purpose: To create a fun short story
#

######################################################################
malaka='''\nHe gives his {0} a shake,
And laughs until her belly aches.
The only other sound's the break,
Of distant waves and birds awake.

The {1} is {2}, {3} and deep,
But he has promises to keep,
After {1} and lots of sleep.
Sweet dreams come to him cheap.'''

promise=[input("Please enter a noun about a snake: "),input("please enter an adjective: "),input("please enter another adjective: "),input("Please enter a noun that is a food: ")]
for i in range(len(promise)):
    promise.append(promise[i])
print(malaka.format(promise[0],promise[1],promise[2],promise[3],promise[1]))