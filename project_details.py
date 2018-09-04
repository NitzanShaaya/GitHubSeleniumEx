import uuid


class ProjectDetails(object):

    def __init__(self, is_error, title, description, tags, last_update_time, language, stars):
        self.uuid = uuid.uuid4()  # generating a unique id so no identical lines could be generated later on in the db
        self.is_error = is_error
        self.title = title
        self.description = description
        self.tags = tags
        self.last_update_time = last_update_time
        self.language = language
        self.stars = stars

# I have looked for an orm that supports mysql. Found none, how can you say no one likes microsoft
