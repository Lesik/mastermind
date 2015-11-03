#! /usr/bin/env python3

import locale
import backend
from dialog import Dialog

__author__ = 'lesik'

class Game:

	global game_backend
	global game_dialog
	empty = ''

	def __init__(self):
		locale.setlocale(locale.LC_ALL, '')
		print('lala')
		self.game_backend = backend.Backend()
		self.game_dialog = Dialog(dialog='dialog')

		user_input = []
		for i in range(0, self.game_backend.code_length):
			user_input.append([self.get_input(i, user_input, True),
							   self.get_input(i, user_input, False)])

		print(user_input)

	def get_input(self, i, user_input, shapes):
		if shapes:
			choicesl = self.game_backend.get_shapes()
			question_text = 'Please pick the ' + str(i + 1) + '. shape. ' \
															'Entered ' \
													 'until now: ' + \
							str(user_input)
			help_text = 'This is helptext for shapes.'
		else:
			choicesl = self.game_backend.get_colours()
			question_text = 'Please pick the ' + str(i + 1) + '. colour. ' \
														   'Entered ' \
													 'until now: ' + \
							str(user_input)
			help_text = 'This is helptext for colours.'

		choices = []
		for i in choicesl:
			choices.append((i, self.empty, False))

		broken = False
		while not broken:
			code, choice = self.game_dialog\
				.radiolist(question_text,\
					choices = choices,\
					help_button = True)

			if code == 'help':
				self.game_dialog.msgbox(help_text)

			else:
				broken = True

		return choicesl.index(choice)