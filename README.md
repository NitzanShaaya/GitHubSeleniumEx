# Hello,
# Please follow the instructions to run the scrapper.
# First,Please start the docker in the docker folder placed here.
# To do so,Use RunMeToClearDocker(to make sure there are no containers with the same name,it will cause problem), Then Run RunMeToSetupDocker.
# After those, open a terminal(or cmd) where the docker is and enter the following commands(these create a table and grant privilages to the user that was already created. but due to a bug doesnt get superuser privileges):
#   docker exec -it scrapperdb mysql -uroot -pPassword1
#   USE scrapper_output;
#   CREATE TABLE search_results(uuid varchar(255), is_error int, title varchar(255), description varchar(255), tags varchar(255), last_update_time date, language varchar(255), stars varchar(255));
#   GRANT ALL PRIVILEGES ON *.* TO 'scrapper' WITH GRANT OPTION;
# Side note: i decided to set up the data base outside of the scrapper(since in my opinion its not a functionallity that should be taken care of by the scrapper), so 3 out of the 5 lines in the set up script are mean't for that.
# After the docker is all up and running, simply run scrapper.exe which is in this directory.
# Another side note, you will see some remarks explaining specific sections in my code, they are mean't to inform you of a certain decision i made.

# Thanks for looking =)