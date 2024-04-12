# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Music_List():
    # User-facing properties:
    #   Nothing

    def __init__(self):
        # Parameters:
        #   Nothing
        # Side effects:
        #   Create empty track list
        pass
    
    def add_track(self, track):
        # Parameters:
        #   track: string
        # Side effects:
        #   Add track to track list
        pass

    def get_track_list(self):
        # Parameters:
        #   Nothing
        # Return:
        #   List of strings in track list 
        # Side effects:
        #   Nothing
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE
"""
Given an empty music track list
#return an empty track list
"""
music_list = Music_List()
music_list.get_track_list() # => []

"""
Given an empty music track list
Adding an empty track
#returns a track list with an empty string
"""
music_list = Music_List()
music_list.add_track("")
music_list.get_track_list() # => [""]

"""
Given an empty music track list
Add a track
#returns a track list with one track
"""
music_list = Music_List()
music_list.add_track("Diamond")
music_list.get_track_list() # => ["Diamond"]

"""
Given an empty music track list
Add two tracks
#returns a track list with two tracks
"""
music_list = Music_List()
music_list.add_track("Diamond")
music_list.add_track("Jolene")
music_list.get_track_list() # => ["Diamond", "Jolene"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
