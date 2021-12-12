import os
import json
import pytest
import sys
import helper
# from StringIO import StringIO
import readchar
from readchar import key
from readchar import readkey
from sys import platform as _platform
from inquirer import events

from io import StringIO

# Setup path assignment.
if _platform.startswith('win'):
    config_path = '..\\test\\config.json'
    path = '..\\src'
else:
    config_path = '../test/config.json'
    path = '../src'
helper.create_config(config_path)
sys.path.append(path)
os.chdir(path)

import utils
import in_college

# Create actual instance of config object.
config = utils.InCollegeConfig(config_path)

def test_connect_friends(monkeypatch, capsys):
    """Example UI test with captured output and simulated keypresses."""
    test_sequence = [
            key.ENTER,           # choose the friends option.
            *'admin', key.ENTER, # enter friend's first name.
            *'admin', key.ENTER, # enter friend's last name.
            key.UP, key.ENTER,   # go back to home screen.
            key.UP, key.ENTER,   # quit the application.
    ]
    # "Monkeypatch" the function, so that it accepts a series of key inputs.
    monkeypatch.setattr('readchar.readkey', lambda: test_sequence.pop(0))
    # Run the script and discard return value. 
    _ = in_college.user_loop(config)
    # Receive output from the execution.
    captured = capsys.readouterr()
    # Check if the stuff printed out as expected.
    assert '🎉 admin is InCollege! Hooray!' in captured.out 
    # Make sure that the error field is empty.
    assert captured.err == ''

def test_save_posting(monkeypatch):
    """Example UI test with simulated keypresses and json update assert."""
    test_sequence = [
            key.DOWN,            # scroll to skip the welcome screen.
            key.ENTER,           # skip welcome screen.
            key.ENTER,           # sign in into application.
            *'admin', key.ENTER, # enter login string.
            *'admin', key.ENTER, # enter password string.
            key.ENTER,           # search for a job.
            key.ENTER,           # internships.
            key.DOWN, key.ENTER, # show list of jobs.
            key.ENTER,           # show the first job.
            key.DOWN, key.ENTER, # save this job.
            key.UP, key.ENTER,   # go back.
            key.UP, key.ENTER,   # go back.
            key.UP, key.ENTER,   # go back.
            key.UP, key.ENTER,   # logout.
            key.UP, key.ENTER,   # go back.
            key.UP, key.ENTER    # quit.
    ]
    monkeypatch.setattr('readchar.readkey', lambda: test_sequence.pop(0))
    _ = in_college.user_loop(config)
    # We saved only one job so far, check length of the saved list.
    assert len(config['accounts']['admin']['saved_jobs']) == 1
    # We store saved jobs as a list of ids, so compare the id of interest.
    assert config['accounts']['admin']['saved_jobs'][0] == '2'

def test_apply_for_job(monkeypatch):
    """Test sequence of inputs to apply for a job using an account."""
    test_sequence = [
            key.DOWN, key.ENTER,      # skip welcome screen.
            key.ENTER,                # sign in into application.
            *'admin', key.ENTER,      # enter login string.
            *'admin', key.ENTER,      # enter password string.
            key.ENTER,                # search for a job.
            key.ENTER,                # internships.
            key.DOWN, key.ENTER,      # apply for a job.
            key.ENTER,                # apply for this specific posting.
            key.ENTER,                # begin application process.
            *'12/12/2022', key.ENTER, # enter graduation date.
            *'12/13/2022', key.ENTER, # enter start date.
            *'I am great', key.ENTER, # enter essay question.
            key.UP, key.ENTER,        # exit job list.
            key.UP, key.ENTER,        # go back.
            key.UP, key.ENTER,        # go back.
            key.UP, key.ENTER,        # go back.
            key.UP, key.ENTER,        # logout.
            key.UP, key.ENTER,        # go back.
            key.UP, key.ENTER         # quit.
    ]
    # Patch the input.
    monkeypatch.setattr('readchar.readkey', lambda: test_sequence.pop(0))
    # Run the user loop.
    _ = in_college.user_loop(config)
    # We applied to only one job so far, check length of the saved list.
    assert len(config['accounts']['admin']['applications']) == 1
    # We store saved jobs as a dict of keys ids, so compare the id of interest.
    assert '2' in config['accounts']['admin']['applications'].keys()

def test_play_video(monkeypatch, capsys):
    """Test "under construction" message for video selection."""
    monkeypatch.setattr('readchar.readkey', lambda: test_sequence.pop(0))
    test_sequence = [
            key.DOWN, key.ENTER,        # skip the welcome selection.
            *[key.DOWN] * 3, key.ENTER, # scroll to video selection.
            key.UP, key.ENTER,          # go back to main screen.
            key.UP, key.ENTER,          # quit the application.
    ]
    # Run the user loop.
    _ = in_college.user_loop(config)
    # Receive output from the execution.
    captured = capsys.readouterr()
    # Check if the stuff printed out as expected.
    assert captured.out.find('🚨 Playing video 🎥. Under construction. 🚨⚠️')
    # Make sure that the error field is empty.
    assert captured.err == ''
