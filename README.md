# Address book

This assignment is done by Assem Chelli (bigOTHER).

## Installation
```sh
    $ sudo python setup.py install
```
## Usage 

Import classes:
```python
    >>> from assem_address_book import AddressBook, Group, Person
```    
Create the `AddressBook`:
```python
    >>> address_book = AddressBook()
```           
Create `Person` and add it to the  `AddressBook`:
```python
    >>> person_1 = Person("Assem", "Chelli", addresses=["Jijel"], phones=["079342423"],
                               emails=["assem@goooogle.org", "omassem@tst.yet"])
    >>> address_book.add_person(person_1)
```    
By default, nothing will be added in the case of duplication(the key is full name). Use the argument `replace` in order to replace old element.
```python    
    >>> address_book.add_person(person_1, replace= True)
``` 
Create `Group` and add it to the `AddressBook`:
```python    
    >>> group_1 = Group("Gamers")
    >>> address_book.add_group(group_1)
```
Assign a `Person` to a `Group`:
```python
    >>> address_book.assign_group( person_1, group_1)
```
List members of a `Group` (Generator):
```python
    >>> address_book.list_group_members(group_1)
```    
List groups of a `Person` (Generator):
```python     
    >>> address_book.list_person_groups(person_1)
```   
Finding Persons by name (Generator):
```python
    >>> address_book.find_by_name(None, "Chelli")
    >>> address_book.find_by_name("Assem", "")
    >>> address_book.find_by_name("Assem", "Chelli")
```

Finding by email prefix (Generator):
```python
    >>> address_book.find_by_email("assem")
```    
    
## Answer to design-only question

Finding by substring could be done easily by `in`: 
    
```python
    >>> "comp" in "alexander@company.com" 
    True
```
    




