The assignment is to implement a simple address book library in Python.


Overview
========

* Assignment version: 1.0

* Language: Python

* Type: Library

* Estimated effort needed: 3-4 hours


Guidelines
==========

There are multiple aspects to the assignment. It will help you to think about
each one as you work through it:

* Object oriented modeling - how do we represent the problem domain in code?
  Software is always evolving - are we making any assumptions that will make it
  hard to extend the model in the future?

* API design - how will users of the library code against the library? Are we
  providing an understandable and convenient API?

* Problem solving - what's a clean way to implement the features we need to
  support?

* Testing - how do we demonstrate to ourselves and others that the code works
  as expected?


When in doubt, here are good guidelines to follow:

* Understand the problem you are solving before you start coding.

* Use object orientation to model the problem domain.

* Keep your code modular and testable.

* Keep it simple.

* We are interested in seeing *your code* and *your solutions*. Don't use
  existing code as part of your solution, otherwise we don't get to see that!

* If you can't solve a part of the assignment, don't worry and send us what
  you have. A partial solution is still useful!


Requirements
============

Facts:

* A person has a first name and a last name.

* A person has one or more street addresses.

* A person has one or more email addresses.

* A person has one or more phone numbers.

* A person can be a member of one or more groups.

* An address book is a collection of persons and groups.


Required features (these need to be unit tested):

* Add a person to the address book.

* Add a group to the address book.

* Given a group we want to easily find its members.

* Given a person we want to easily find the groups the person belongs to.

* Find person by name (can supply either first name, last name, or both).

* Find person by email address (can supply either the exact string or a prefix
  string, ie. both "alexander@company.com" and "alex" should work).


Design-only questions:

* Find person by email address (can supply any substring, ie. "comp" should
  work assuming "alexander@company.com" is an email address in the address
  book) - discuss how you would implement this without coding the solution.


What to deliver:

* A README that documents the public API. For each of the required features
  please mention how to use the API to achieve that result. Also include
  your answer to the design-only questions here.

* The library as a Python package. Make sure the code works and the unit tests
  are passing.

Please provide a link to a Github or Bitbucket repository (or similar) so
we can easily obtain and run your code.