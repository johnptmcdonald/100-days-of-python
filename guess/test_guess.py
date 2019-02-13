from unittest.mock import patch
import random
import pytest

from guess import get_random_number, Game

@patch.object(random, 'randint')
def test_get_random_number(m):
	m.return_value = 17
	assert get_random_number() == 17

@patch("builtins.input", side_effect=[11, '12', 'test', 12, 5, -1, 21, 7, None])
def test_guess(inp):
	game = Game()
	
	# good guesses (int or string)
	assert game.guess() == 11
	assert game.guess() == 12
	
	# guess the word 'test'
	with pytest.raises(ValueError):
		game.guess()
	# guess a previously guessed value
	with pytest.raises(ValueError):
		game.guess()

	assert game.guess() == 5

	# guess -ve value
	with pytest.raises(ValueError):
		game.guess()
	# guess out of range
	with pytest.raises(ValueError):
		game.guess()		

	assert game.guess() == 7

	# guess None
	with pytest.raises(ValueError):
		game.guess()

# capfd captures the standard output
def test_validate_guess(capfd):
	game = Game()
	game._answer = 2

	# use capfd to look at and test the stdout
	assert not game._validate_guess(1)
	out, error = capfd.readouterr()
	assert out.rstrip() == '1 is too low'

	assert not game._validate_guess(3)
	assert game._validate_guess(2)

# run with `pytest`
# when run with `pytest -s` if gives you the stdout 
# get coverage with `pytest --cov-report term-missing --cov='guess'`




