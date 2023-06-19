from django.test import TestCase
from mainapp.models import Skill, User, SplitCharField


class SplitCharFieldTestCase(TestCase):
    def test_split_method(self):
        field = SplitCharField()
        value = "Skill 1, Skill 2, Skill 3"
        expected_result = ["Skill 1", "Skill 2", "Skill 3"]

        result = field.split(value)

        self.assertEqual(result, expected_result)

    def test_empty_input(self):
        field = SplitCharField()
        value = ""
        expected_result = []

        result = field.split(value)

        self.assertEqual(result, expected_result)

    def test_whitespace_input(self):
        field = SplitCharField()
        value = "  Skill 1  ,   Skill 2   ,  "
        expected_result = ["Skill 1", "Skill 2"]

        result = field.split(value)

        self.assertEqual(result, expected_result)


class UserModelTestCase(TestCase):
    def test_skills_field(self):
        user = User.objects.create(username="tester", skills="Skill 1, Skill 2, Skill 3")

        self.assertEqual(user.skills, "Skill 1, Skill 2, Skill 3")


class SkillModelTestCase(TestCase):
    def test_skill_name(self):
        skill = Skill.objects.create(name="Python")

        self.assertEqual(str(skill), "Python")
