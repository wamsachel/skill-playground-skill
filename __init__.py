from mycroft import MycroftSkill, intent_file_handler


class SkillPlayground(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('playground.skill.intent')
    def handle_playground_skill(self, message):
        self.speak_dialog('playground.skill')


def create_skill():
    return SkillPlayground()

