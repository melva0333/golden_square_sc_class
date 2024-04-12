from lib.music_track_list import *
"""
Given an empty music track list
#return an empty track list
"""
def test_empty_list_returns_empty_list():
    music_list = Music_List()
    assert music_list.get_track_list() == []

"""
Given an empty music track list
Adding an empty track
#returns a track list with an empty string
"""
def test_empty_list_add_empty_return_empty_list():
    music_list = Music_List()
    music_list.add_track("")
    assert music_list.get_track_list() == [""]

"""
Given an empty music track list
Add a track
#returns a track list with one track
"""
def test_empty_list_add_track_return_track():
    music_list = Music_List()
    music_list.add_track("Diamond")
    assert music_list.get_track_list() == ["Diamond"]

"""
Given an empty music track list
Add two tracks
#returns a track list with two tracks
"""
def test_empty_list_add_tracks_return_list_of_tracks():
    music_list = Music_List()
    music_list.add_track("Diamond")
    music_list.add_track("Jolene")
    assert music_list.get_track_list() == ["Diamond", "Jolene"]