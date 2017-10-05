name='Hansa'
age=21
height=170 #centimeters
weight=55 #kilograms
eyes='Brown'
teeth='White'
hair='Black'
weight_lbs=weight*2.2
height_feet=height*0.0328

print("Let's talk about %s."% name)
print("She's %d centimeters tall."% height)
print("She weights %d kilograms."% weight)
print("She's got %s eyes and %s hair." % (eyes,hair))
print("Her teeth are %s." % teeth)

print(" If I add %d, %d, and %d - I get %d" % (age,height,weight,age+height+weight))

print("My name is %r." % name) #used %r instead of %s here

print("Height in feet %10.2f" % height_feet)
print("Weight in lbs %10.2f" % weight_lbs)