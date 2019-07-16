# chatterbot
This chatterbot is built in python which makes it possible to generate responses based on collection of known conversation.
the language independent design of chatterbot allows it to be trained to speak any language.

#before working on chatterbot:
--make sure that a chatterbot is installed(this chatterbot is chatterbot 0.8.6 installed)

INSTALLATION:use "pip install chatterbot==0.8.6" command to install the chatterbot

#while executing the program check for the following:
if you get a EOL error(end of line error):
   ---check if the quotes has been ended correctly
   ---check brackets
   ---use forward slashes instead of back slashes in location addresses
   ---make sure that you have given at the end of the path you provided
   ---dont save the file names same as those present in the chatterbot libraries(ex:chatterbot) since it affects the other existing files.

initially chatterbot have no knowlegde of how to communicate.each time a user enters any message, the libraries saves the text that user 
enters and also responds to the users message based on collection of known conversation.the chatterbot uses the texts saved by libraries
to learn, improve and give accurate responses. 

