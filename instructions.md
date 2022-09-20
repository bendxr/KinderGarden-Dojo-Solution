# Instructions

Given a diagram, determine which plants each child in the kindergarten class is responsible for.

The kindergarten class is learning about growing plants. The teacher thought it would be a good idea to give them actual seeds, plant them in actual dirt, and grow actual plants.

They've chosen to grow **grass**, **clover**, **radishes**, and **violets**.

To this end, the children have put little cups along the window sills, and planted one type of plant in each cup, choosing randomly from the available types of seeds.

```bash
[window][window][window]
........................ # each dot represents a cup
........................
```

There are 12 children in the class:
```text
    Alice, Bob, Charlie, David,
    Eve, Fred, Ginny, Harriet,
    Ileana, Joseph, Kincaid, and Larry.
```

Each child gets 4 cups, two on each row. Their teacher assigns cups to the children alphabetically by their names.

The following diagram represents Alice's plants:
```text
[window][window][window]
VR......................
RG......................
```
In the first row, nearest the windows, she has a violet and a radish. In the second row she has a radish and some grass.

Your program will be given the plants from left-to-right starting with the row nearest the windows. From this, it should be able to determine which plants belong to each student.

For example, if it's told that the garden looks like so:
```text
[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
```

Then if asked for Alice's plants, it should provide:
```
    Violets, radishes, violets, radishes
```

While asking for Bob's plants would yield:
```
    Clover, grass, clover, clover
```

# Python Implementation

The tests for this exercise expect your program to be implemented as a Garden class in Python. If you are unfamiliar with classes in Python, classes from the Python docs is a good place to start.

Your class should implement a method called plants, which takes a student's name as an argument and returns the list of plant names belonging to that student.
Constructors

Creating the example garden
```text
[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
```

would, in the tests, be represented as 
```python
Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
```

To make this representation work, your class will need to implement an `__init__()` method. If you're not familiar with `__init__()` or constructors, class and instance objects from the Python docs gives a more detailed explanation.
Default Parameters

In some tests, a list of students is passed as an argument to `__init__()`. This should override the twelve student roster provided in the problem statement. Both of these statements need to work with your `__init__()` method:

* Make a garden based on the default 12-student roster.
```python
Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
```

* Make a garden based on a 2-student roster.
```python
Garden("VRCC\nVCGG", students=["Valorie", "Raven"]) 
```
