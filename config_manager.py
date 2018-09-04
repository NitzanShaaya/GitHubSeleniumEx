import ConfigParser


# Can be mapped but in some cases mapping creates more delays than specific calls(mostly in cases of a lot of values)
# Either way, here its redundant considering the fact there are very few values
class ConfigManager:

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('config.ini')

    def get_config_string(self, section, option):
        try:
            return self.config.get(section, option)
        except:
            print_and_throw_exception(section, option)

    def get_config_int(self, section, option):
        try:
            return self.config.getint(section, option)
        except:
            print_and_throw_exception(section, option)


def print_and_throw_exception(section, option):
    print "Failed to find configuration option{0} at section{1}!", format(option, section)
    raise Exception("Couldn't get expected config parameter")
