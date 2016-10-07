import unittest

from assem_address_book.models import Person, AddressBook, MembershipIndex, Membership, Group


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = AddressBook()
        self.person_1 = Person("Assem", "Chelli", addresses=["Jijel"], phones=["079342423"],
                               emails=["assem@goooogle.org", "omassem@tst.yet"])
        self.person_2 = Person("omar", "lamrI", addresses=["Algiers"], phones=["3242342"], emails=["omar@goooogle.org"])
        self.group_1 = Group("Gamers")
        self.group_2 = Group("Otherz")

    def test_add_person(self):
        self.address_book.add_person(self.person_1)
        self.assertIn(self.person_1.id, self.address_book._persons)
        self.assertIs(self.person_1, self.address_book._persons[self.person_1.id])
        self.assertFalse(self.address_book.add_person(self.person_1, replace=False))
        self.assertTrue(self.address_book.add_person(self.person_1, replace=True))

    def test_add_group(self):
        self.address_book.add_group(self.group_1)
        self.assertIn(self.group_1.id, self.address_book._groups)
        self.assertIs(self.group_1, self.address_book._groups[self.group_1.id])
        self.assertFalse(self.address_book.add_group(self.group_1, replace=False))
        self.assertTrue(self.address_book.add_person(self.group_1, replace=True))

    def test_assign_group(self):
        self.address_book.add_person(self.person_1)
        self.address_book.add_group(self.group_1)
        self.address_book.assign_group(self.person_1, self.group_1)
        self.assertIn(self.group_1.id, self.address_book._membership_index.groups_by_person[self.person_1.id])
        self.assertIn(self.person_1.id, self.address_book._membership_index.persons_by_group[self.group_1.id])

    def test_list_group_members(self):
        self.address_book.add_person(self.person_1)
        self.address_book.add_person(self.person_2)
        self.address_book.add_group(self.group_1)
        self.address_book.add_group(self.group_2)
        self.address_book.assign_group(self.person_1, self.group_1)
        self.address_book.assign_group(self.person_2, self.group_1)
        self.address_book.assign_group(self.person_1, self.group_2)
        self.assertCountEqual(list(self.address_book.list_group_members(self.group_1)), [self.person_1, self.person_2])
        self.assertCountEqual(list(self.address_book.list_group_members(self.group_2)), [self.person_1])

    def test_list_person_groups(self):
        self.address_book.add_person(self.person_1)
        self.address_book.add_person(self.person_2)
        self.address_book.add_group(self.group_1)
        self.address_book.add_group(self.group_2)
        self.address_book.assign_group(self.person_1, self.group_1)
        self.address_book.assign_group(self.person_2, self.group_1)
        self.address_book.assign_group(self.person_1, self.group_2)
        self.assertCountEqual(list(self.address_book.list_person_groups(self.person_1)), [self.group_1, self.group_2])
        self.assertCountEqual(list(self.address_book.list_person_groups(self.person_2)), [self.group_1])

    def test_find_by_name(self):
        self.address_book.add_person(self.person_1)
        self.address_book.add_person(self.person_2)
        self.assertCountEqual(list(self.address_book.find_by_name("Omar", "")), [self.person_2])
        self.assertCountEqual(list(self.address_book.find_by_name("assem", "Chelli")), [self.person_1])
        self.assertCountEqual(list(self.address_book.find_by_name(None, "Chelli")), [self.person_1])

    def test_find_by_email(self):
        self.address_book.add_person(self.person_1)
        self.address_book.add_person(self.person_2)
        self.assertCountEqual(list(self.address_book.find_by_email("omar")), [self.person_2])
        self.assertCountEqual(list(self.address_book.find_by_email("oma")), [self.person_2, self.person_1])
        self.assertCountEqual(list(self.address_book.find_by_email("assem")), [self.person_1])
        self.assertCountEqual(list(self.address_book.find_by_email("assem@goooogle.org")), [self.person_1])


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.group = Group("Hackers")

    def test_init(self):
        self.assertEqual("Hackers", self.group._name)
        self.assertEqual("hackers", self.group.id)

    def test_name(self):
        self.assertEqual("Hackers", self.group.name())


class TestMembership(unittest.TestCase):
    def setUp(self):
        self.person = Person("Assem", "Chelli", addresses=["Jijel"], phones=["079342423"],
                             emails=["assem@goooogle.org"])
        self.group = Group("Gamers")
        self.membership = Membership(self.person, self.group)

    def test_init(self):
        self.assertEqual((self.person.id, self.group.id), self.membership.id)


class TestMembershipIndex(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Assem", "Chelli", addresses=["Jijel"], phones=["079342423"],
                               emails=["assem@goooogle.org"])
        self.group_1 = Group("Gamers")
        self.person_2 = Person("omar", "lamrI", addresses=["Algiers"], phones=["3242342"], emails=["omar@goooogle.org"])
        self.group_2 = Group("Otherz")
        self.membership_1 = Membership(self.person_1, self.group_1)
        self.membership_2 = Membership(self.person_1, self.group_2)
        self.membership_3 = Membership(self.person_2, self.group_2)

        self.membershipindex = MembershipIndex()

    def test_init(self):
        pass

    def test_add_membership(self):
        self.membershipindex.add_membership(self.membership_1)
        self.assertIn(self.group_1.id, self.membershipindex.groups_by_person[self.person_1.id])
        self.assertIn(self.person_1.id, self.membershipindex.persons_by_group[self.group_1.id])

    def test_get_groups(self):
        self.membershipindex.add_membership(self.membership_1)
        self.membershipindex.add_membership(self.membership_2)
        self.membershipindex.add_membership(self.membership_3)
        self.assertCountEqual(self.membershipindex.get_groups(self.person_1.id), [self.group_1.id, self.group_2.id])
        self.assertCountEqual(self.membershipindex.get_groups(self.person_2.id), [self.group_2.id])

    def test_get_members(self):
        self.membershipindex.add_membership(self.membership_1)
        self.membershipindex.add_membership(self.membership_2)
        self.membershipindex.add_membership(self.membership_3)
        self.assertCountEqual(self.membershipindex.get_members(self.group_2.id), [self.person_1.id, self.person_2.id])
        self.assertCountEqual(self.membershipindex.get_members(self.group_1.id), [self.person_1.id])


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Assem", "Chelli", addresses=["Jijel"], phones=["079342423"],
                               emails=["assem@goooogle.org"])
        self.person_2 = Person("omar", "lamrI", addresses=["Algiers"], phones=["3242342"], emails=["omar@goooogle.org"])

    def test_init(self):
        self.assertEqual(self.person_1.first_name, "Assem")
        self.assertEqual(self.person_1.last_name, "Chelli")
        self.assertEqual(self.person_2.first_name, "Omar")
        self.assertEqual(self.person_2.last_name, "Lamri")
        self.assertIn("Jijel", self.person_1.addresses)
        self.assertIn("079342423", self.person_1.phones)
        self.assertIn("assem@goooogle.org", self.person_1.emails)

    def test_full_name(self):
        self.assertEqual(self.person_1.full_name(), "Assem Chelli")
        self.assertEqual(self.person_2.full_name(), "Omar Lamri")

    def test_rules(self):
        pass


if __name__ == '__main__':
    unittest.main()
