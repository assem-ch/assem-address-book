#!/usr/bin/env python

"""models.py: contains the models of the address book."""

__author__ = "Assem Chelli"


class AddressBook:
    """ِManage a set of groups and persons

    Create the `AddressBook`:

        >>> address_book = AddressBook()

    """

    def __init__(self):
        self._groups = {}
        self._persons = {}
        self._membership_index = MembershipIndex()

    def add_person(self, person, replace=False):
        """
        Add a person to the address book.

        :param person: an instance of Person class.
        :param replace: if True, person will replace any old instance.
        :return: True if the person added, False if not.
        """
        if replace or person.id not in self._persons:
            self._persons[person.id] = person
            return True

        return False

    def add_group(self, group, replace=False):
        """
        Add a group to the address book.

        :param group: an instance of Group class.
        :param replace: if True, `group` will replace any old instance.
        :return: True if the group added, False if not.
        """
        if replace or group.id not in self._groups:
            self._groups[group.id] = group
            return True

        return False

    def assign_group(self, person, group):
        """
        Assign a person to a group.

        :param person: an instance of Person class.
        :param group: an instance of Group class.
        :return: None
        :raise: Exception if person or group are not part of the address book.
        """
        if person.id not in self._persons:
            raise Exception("This person {} is not part of this Address book".format(person))

        if group.id not in self._groups:
            raise Exception("This group {} is not part of this Address book".format(group))

        membership = Membership(person, group)
        self._membership_index.add_membership(membership)

    def list_group_members(self, group):
        """
        List all members of a group.

        :param group: an instance of Group class.
        :return: generator of persons
        """
        for person_id in self._membership_index.get_members(group_id=group.id):
            yield self._persons.get(person_id)

    def list_person_groups(self, person):
        """
        List all groups of a person.

        :param person: an instance of Person class.
        :return: generator of groups
        """
        for group_id in self._membership_index.get_groups(person_id=person.id):
            yield self._groups.get(group_id)

    def find_by_name(self, first_name, last_name):
        """
        Find persons in the address book by their first, last, or full name.

        :param first_name: the first name to search for.
        :param last_name: the last name to search for.
        :return: generator of persons.
        """
        for person in self._persons.values():
            if (not first_name or person.first_name == first_name.capitalize()) \
                    and (not last_name or person.last_name == last_name.capitalize()):
                yield person

    def find_by_email(self, prefix):
        """
        Find persons in the address book by prefix of their email.

        :param prefix: prefix of the email to search for.
        :return: generator of persons.
        """
        for person in self._persons.values():
            for email in person.emails:
                if email.startswith(prefix):
                    yield person
                    break


class Group:
    """
    Group a set of persons.

        >>> group_1 = Group("Gamers")
    """

    def __init__(self, name):
        """
        :param name: Name of the group.
        """
        self._name = name
        self.id = self._name.lower()

    def name(self):
        return self._name

    def __str__(self):
        return self.name()

    def __repr__(self):
        return "<Group '{}'>".format(self.name())


class Person:
    """
    Represent the different info of a person.

        >>> person_1 = Person("Assem", "Chelli", addresses=["Jijel"], phones=["079342423"], emails=["assem@gogle.org"])

    """

    def __init__(self, first_name, last_name, addresses, phones, emails):
        """

        :param first_name: the first name.
        :param last_name:  the last name.
        :param addresses: a list of addresses.
        :param phones: a list of phones.
        :param emails: a list of emails.
        """
        if not (first_name and last_name and addresses and phones and emails):
            raise Exception("All info are mandatory!")
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.addresses = addresses
        self.phones = phones
        self.emails = emails
        self.id = self.full_name()

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()

    def __repr__(self):
        return "<Person '{}'>".format(self.full_name())


class Membership:
    def __init__(self, person, group):
        self.person_id = person.id
        self.group_id = group.id
        self.id = (self.person_id, self.group_id)

    def __repr__(self):
        return "<Membersip '{} - {}'>".format(self.person_id, self.group_id)


class MembershipIndex:
    def __init__(self):
        self.groups_by_person = {}
        self.persons_by_group = {}

    def add_membership(self, membership):
        # add membership to groups_by_person
        if membership.person_id in self.groups_by_person:
            self.groups_by_person[membership.person_id].append(membership.group_id)
        else:
            self.groups_by_person[membership.person_id] = [membership.group_id]

        # add membership to persons_by_groups
        if membership.group_id in self.persons_by_group:
            self.persons_by_group[membership.group_id].append(membership.person_id)
        else:
            self.persons_by_group[membership.group_id] = [membership.person_id]

    def get_groups(self, person_id):
        return self.groups_by_person.get(person_id)

    def get_members(self, group_id):
        return self.persons_by_group.get(group_id)
