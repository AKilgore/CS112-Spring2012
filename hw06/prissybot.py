#!/usr/bin/env python

# Prissy bot asks the player their name.
print "Hello! I am Prissy Bot! What is your name?"
name = raw_input ()

# Prissy bot insults player using their name.
print "You mean, Hi bot,sir", name

# Prissy bot asks the player why they are rude.
print "Why are you so rude?"
rude_answer = raw_input ()

# Prissy bot responds to the player's reason as to why the player is rude.
print "There are certainly better reasons to be so rude than just" , rude_answer

# Prissy bot insults the player again.
print "But I guess that's about the unrefinement I would expect from someone named" , name

# Prissy bot insults the player while telling the player to answer some math problems.
print "Okay, if you do some math problems correctly, I will give you a present, just because I feel bad for such a monocle-less simplton such as you" , name

# Prissy bot asks the player if they want to do math problems.
print "Is this okay with you" , name
math_answer=raw_input()

# Prissy bot doesn't care about the player's math problem answer.
print "Well you're doing this math whether you like it or not!"

# Prissy bot asks the player to enter in the first number for the math problems.
print "Enter a number:"
n = raw_input ()

# Prissy bot asks the player to enter in the second number for the math problems.
print "Enter another number:"
m = raw_input ()

n = int (n)
m = float (m)

# Prints the math problems.
print n ," + ", m ," = ", n+m
print n ," - ", m ," = ", n-m
print n ," * ", m ," = ", n*m
print n ," / ", m ," = ", n/m

# Prissy bot congratulates the player.
print "Congratulations! (even though I did most of the work) Now you get your diamond!"

# Asks the player what symbol will be used to make the diamond. The "s" variable stands for the spaces used in the making od the diamond while the "c" variable is the symbol that the player wants the diamond to be made of.
print "What will your diamond be made of?"
s = " "
c = raw_input ()

# Prints out the diamond.
print 4*s,1*c
print 3*s,3*c
print 2*s,5*c
print 1*s,7*c
print 0*s,9*c
print 1*s,7*c
print 2*s,5*c
print 3*s,3*c
print 4*s,1*c

print "Now go away."

