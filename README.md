# Hello,
# For me from some reason, i couldn't connect to the mysql docker or mongo docker(from anywhere outside the docker, and i think i tried every single solution out there). I created two versions in case that as i suspect this is only a local problem. you can choose either one(scrapper_mysql or scrapper_mongo)
# If you chose mysql:
#   First,Please start the docker in the docker folder placed here.
#   To do so,Use RunMeToClearDocker(to make sure there are no containers with the same name,it will cause problem), Then Run RunMeToSetupDocker(waits 30 seconds to complete, which is the max start time i experienced).
#   After those, open a terminal(or cmd) where the docker is and enter the following commands(these create a table and grant privilages to the user that was already created. but due to a bug doesnt get superuser privileges):
#       docker exec -it scrapperdb mysql -uroot -pPassword1
#       USE scrapper_output;
#       CREATE TABLE search_results(uuid varchar(255), is_error int, title varchar(255), description varchar(255), tags varchar(255), last_update_time date, language varchar(255), stars varchar(255));
#       GRANT ALL PRIVILEGES ON *.* TO 'scrapper' WITH GRANT OPTION;
#   Side note: i decided to set up the data base outside of the scrapper(since in my opinion its not a functionallity that should be taken care of by the scrapper), so 3 out of the 5 lines in the set up script are mean't for     that.
# If you chose mongo:
#   Run StartMongo.bat(will also wait 30 seconds for mongo to load)
# 
# Use the build scrappers.bat(in the directory its in) to build the scrapper(please notice the dist directory will be created)
# After one the docker is all up and running, simply run the exe of the scrapper you chose (which are under their own directory in the dist folder).
# Another side note, you will see some remarks explaining specific sections in my code, they are mean't to inform you of a certain decision i made.
# If run was successful, on top of the text file with the measurements. a succeeded text file will also be created and will state whether the run was successfuls(a simple True or False)
# If none of the dockers work, please connect one of the managers to a working db of its kind(change the properties in the config.ini at the matching section(mysql or mongo), to the matching values of the real db).

# Thanks for looking =)