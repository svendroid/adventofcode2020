# Advent of Code 2020

This year I want to get better at python and learn more about it.

What did I learn?

## Day 1

* unittest with `unittest` module
* Typing module
    * since 3.5 there is support for typing hints but they are not enforced by the compiler. Can be used by linters, IDEs , etc. [Docs](https://docs.python.org/3/library/typing.html#module-typing)
    * Use Pylance in VSCode (under the hood pyright) to have a static type checker in VSCode
        * activate typechecking in settings: `"python.analysis.typeCheckingMode": "strict"`

## Day 2

* Learned what a [Toboggan](https://en.wikipedia.org/wiki/Toboggan) is - a simple sled
* `re.split` for using different characters as delimeters

## Day 3

* slice notation in python is great - `list[start:stop:step]` especially the step parameter makes it super easy to iterate through a list and e.g. only access every third element

## Day 4

* `yield` was nice for generating the single items on the parsing step
* Regex for the win (as every year) - https://regexr.com/ for quick tryouts

## Day 5

* plane boarding is done wrong :) https://www.youtube.com/watch?v=oAHbLRjF0vo
* List comprehension is a nice way to transform lists
* Sort lists: `sorted` returns a sorted list, `sort` changes the list in place