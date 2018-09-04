# Hello,
# Please follow the instructions to run the scrapper.
# First,Please start the docker in the docker folder placed here.
# To do so,Use RunMeToClearDocker(to make sure there are no containers with the same name,it will cause problem), Then Run RunMeToSetupDb, please notice it might fail due to an open bug in the image. if that happens, use the clear bat once more, then insert the commands written there with a cmd opened to the docker's folder. Please notice that the bug occurs after the docker exec command occurs, when it asks for a password. Re-enter that command once or twice more and it will work.
# Side note, i decided to set up the data base outside of the scrapper(since in my opinion its not a functionallity that should be taken care of by the scrapper), so 3 out of the 5 lines in the set up script are mean't for that.
# After the docker is all up and running, simply run scrapper.exe which is in this directory.
# Another side note, you will see some remarks explaining specific sections in my code, they are mean't to inform you of a certain decision i made.

# Thanks for looking =)