import pyfiglet, sys, time, os
# pseudocode

# ask user name to input name
user_name = input("Please input you name: ")

# ask user  to input dream job
job = input("Please input your dream job: ")

# ask user to input birthday
birthday = input("Please enter your birthday: ")

# ask user to input its university 
university = input("Please enter your current University: ")

# compile and print username, job, birthday, and university in a sentence
my_description = ("I'am " + user_name + ". My dream career in the future is to be a/an " + job
                  + ". My birthday is on " + birthday + ". I am currently studying at " + university + ".")

# print the sentence in fancy way
fancy_description = pyfiglet.figlet_format(my_description)

# add text animation 
for char in fancy_description:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.001)