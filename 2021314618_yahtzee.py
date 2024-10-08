import random

p1_total_score = 0
p1_scores = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Chance': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0}
p1_scores_expected = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Chance': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0}

p2_total_score = 0
p2_scores = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Chance': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0}
p2_scores_expected = {'Aces': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Chance': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0}

for i in range(13):
	#Player 1 Turn

	print("Player 1: Round %d" % (i+1))
	print("Choose the option.")
	print("1. Roll the dice")
	print("2. Check the score sheet")
	temp_option = input()
	option = int(temp_option) if temp_option in ['1', '2'] else temp_option
	print("")
	
	while True:
		#wrong input loop
		if option not in [1, 2]:
			print("You input wrong option. Please enter 1 or 2.")
			print("")
			print("Choose the option.")
			print("1. Roll the dice")
			print("2. Check the score sheet")
			temp_option = input()
			option = int(temp_option) if temp_option in ['1', '2'] else temp_option
			print("")
		#option 2 loop
		elif option == 2:
			print("+-------<Player 1>--------+")
			print("+-----------------+-------+")
			print("|    Category     | Score |")
			print("+-----------------+-------+")
			print("|      Aces       |%4s   |" % (str(p1_scores['Aces']) if p1_scores['Aces'] != 0 else '-'))
			print("|      Twos       |%4s   |" % (str(p1_scores['Twos']) if p1_scores['Twos'] != 0 else '-'))
			print("|     Threes      |%4s   |" % (str(p1_scores['Threes']) if p1_scores['Threes'] != 0 else '-'))
			print("|      Fours      |%4s   |" % (str(p1_scores['Fours']) if p1_scores['Fours'] != 0 else '-'))
			print("|      Fives      |%4s   |" % (str(p1_scores['Fives']) if p1_scores['Fives'] != 0 else '-'))
			print("|      Sixes      |%4s   |" % (str(p1_scores['Sixes']) if p1_scores['Sixes'] != 0 else '-'))
			print("|     Chance      |%4s   |" % (str(p1_scores['Chance']) if p1_scores['Chance'] != 0 else '-'))
			print("| Three of a Kind |%4s   |" % (str(p1_scores['Three of a Kind']) if p1_scores['Three of a Kind'] != 0 else '-'))
			print("| Four of a Kind  |%4s   |" % (str(p1_scores['Four of a Kind']) if p1_scores['Four of a Kind'] != 0 else '-'))
			print("|   Full House    |%4s   |" % (str(p1_scores['Full House']) if p1_scores['Full House'] != 0 else '-'))
			print("| Small Straight  |%4s   |" % (str(p1_scores['Small Straight']) if p1_scores['Small Straight'] != 0 else '-'))
			print("| Large Straight  |%4s   |" % (str(p1_scores['Large Straight']) if p1_scores['Large Straight'] != 0 else '-'))
			print("|     Yahtzee     |%4s   |" % (str(p1_scores['Yahtzee']) if p1_scores['Yahtzee'] != 0 else '-'))
			print("+-----------------+-------+")
			print("")
			print("Player 1 Current Score: %d" % p1_total_score)
			print("")
			print("Player 1: Round %d" % (i+1))
			print("Choose the option.")
			print("1. Roll the dice")
			print("2. Check the score sheet")
			temp_option = input()
			option = int(temp_option) if temp_option in ['1', '2'] else temp_option
			print("")

		else:
			break
	
	if option == 1:
		result = random.choices(range(1, 7), k = 5)
		print("Result of dice")
		print(result)
		print("Reroll the dice? [Y/N]", end = ' ')
		reroll = input()
		print("")
		
		while True:
			if reroll not in ['Y', 'N']:
				print("You input wrong option. Please enter [Y/N].")
				print("")
				print("Reroll the dice? [Y/N]", end = ' ')
				reroll = input()
				print("")
			else:
				break
		
		if reroll == 'Y':
			print("Choose all of dice that you want to keep. Seperate number with space.")
			print("If you want to change all of the dice, then input '0'")
			keep = list(input().split())
			print("")

			while True:
				keep_check = False
				if keep[0] == '0' and len(keep) == 1:
					break
				for j in keep:
					if j.isdigit() == False or (int(j) < 1 or int(j) > 5):
						keep_check = True
				if keep_check == False:
					break
				print("You input wrong option. Please enter between 1~5.")
				print("")
				print("Choose all of dice that you want to keep. Seperate number with space.")
				print("If you want to change all of the dice, then input '0'")
				keep = list(input().split())
				print("")

			for j in range(len(keep)):
				keep[j] = int(keep[j])
			
			if keep[0] == 0 and len(keep) == 1:
				result = random.choices(range(1, 7), k = 5)
			else:
				for j in range(5):
					if j+1 not in keep:
						result[j] = random.randint(1, 6)

			print("Result of dice")
			print(result)
			print("Reroll the dice? [Y/N]", end = ' ')
			reroll = input()
			print("")
			
			while True:
				if reroll not in ['Y', 'N']:
					print("You input wrong option. Please enter [Y/N].")
					print("")
					print("Reroll the dice? [Y/N]", end = ' ')
					reroll = input()
					print("")
				else:
					break

			if reroll == 'Y':
				print("Choose all of dice that you wnat to keep. Seperate number with space.")
				print("If you want to change all of the dice, then input '0'")
				keep = list(input().split())
				print("")

				while True:
					keep_check = False
					if keep[0] == '0' and len(keep) == 1:
						break
					for j in keep:
						if j.isdigit() == False or (int(j) < 1 or int(j) > 5):
							keep_check = True
					if keep_check == False:
						break
					print("You input wrong option. Please enter between 1~5.")
					print("")
					print("Choose all of dice that you want to keep. Seperate number with space.")
					print("If you want to change all of the dice, then input '0'")
					keep = list(input().split())
					print("")

				for j in range(len(keep)):
					keep[j] = int(keep[j])

				if keep[0] == 0 and len(keep) == 1:
					result = random.choices(range(1, 7), k = 5)
				else:
					for j in range(5):
						if j+1 not in keep:
							result[j] = random.randint(1, 6)

				print("Result of dice")
				print(result)

		temp_set = set(result)
		tok_check = False
		fok_check = False
		if len(temp_set) <= 3:
			for j in temp_set:
				if result.count(j) >= 4:
					tok_check = True
					fok_check = True
				elif result.count(j) >= 3:
					tok_check = True

		temp_sorted_setlist = sorted(list(set(result)))
		ss_check = False
		ls_check = False
		if (temp_sorted_setlist[:4] in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]] or temp_sorted_setlist[1:] in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]):
			ss_check = True
		if temp_sorted_setlist in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
			ls_check = True

		p1_scores_expected['Aces'] = result.count(1)
		p1_scores_expected['Twos'] = result.count(2) * 2
		p1_scores_expected['Threes'] = result.count(3) * 3
		p1_scores_expected['Fours'] = result.count(4) * 4
		p1_scores_expected['Fives'] = result.count(5) * 5
		p1_scores_expected['Sixes'] = result.count(6) * 6
		p1_scores_expected['Chance'] = sum(result)
		p1_scores_expected['Three of a Kind'] = sum(result) if tok_check else 0
		p1_scores_expected['Four of a Kind'] = sum(result) if fok_check else 0
		p1_scores_expected['Full House'] = 25 if (len(set(result)) == 2 and tok_check == True and fok_check == False) else 0
		p1_scores_expected['Small Straight'] = 30 if ss_check else 0
		p1_scores_expected['Large Straight'] = 40 if ls_check else 0
		p1_scores_expected['Yahtzee'] = 50 if len(set(result)) == 1 else 0

		print("")
		print("+-------<Player 1>--------+")
		print("+-----------------+-------+")
		print("|    Category     | Score |")
		print("+-----------------+-------+")
		print("|      Aces       |%4s   |" % (str(p1_scores_expected['Aces']) if p1_scores['Aces'] == 0 else '-'))
		print("|      Twos       |%4s   |" % (str(p1_scores_expected['Twos']) if p1_scores['Twos'] == 0 else '-'))
		print("|     Threes      |%4s   |" % (str(p1_scores_expected['Threes']) if p1_scores['Threes'] == 0 else '-'))
		print("|      Fours      |%4s   |" % (str(p1_scores_expected['Fours']) if p1_scores['Fours'] == 0 else '-'))
		print("|      Fives      |%4s   |" % (str(p1_scores_expected['Fives']) if p1_scores['Fives'] == 0 else '-'))
		print("|      Sixes      |%4s   |" % (str(p1_scores_expected['Sixes']) if p1_scores['Sixes'] == 0 else '-'))
		print("|     Chance      |%4s   |" % (str(p1_scores_expected['Chance']) if p1_scores['Chance'] == 0 else '-'))
		print("| Three of a Kind |%4s   |" % (str(p1_scores_expected['Three of a Kind']) if p1_scores['Three of a Kind'] == 0 else '-'))
		print("| Four of a Kind  |%4s   |" % (str(p1_scores_expected['Four of a Kind']) if p1_scores['Four of a Kind'] == 0 else '-'))
		print("|   Full House    |%4s   |" % (str(p1_scores_expected['Full House']) if p1_scores['Full House'] == 0 else '-'))
		print("| Small Straight  |%4s   |" % (str(p1_scores_expected['Small Straight']) if p1_scores['Small Straight'] == 0 else '-'))
		print("| Large Straight  |%4s   |" % (str(p1_scores_expected['Large Straight']) if p1_scores['Large Straight'] == 0 else '-'))
		print("|     Yahtzee     |%4s   |" % (str(p1_scores_expected['Yahtzee']) if p1_scores['Yahtzee'] == 0 else '-'))
		print("+-----------------+-------+")
		print("")
		print("Choose a category to record the score")
		category = input()
		print("")
		
		while True:
			if category not in p1_scores.keys() or p1_scores[category] != 0:
				print("You input wrong category. Please enter again.")
				print("")
				print("Choose a category to record the score")
				category = input()
				print("")
			else:
				break
		p1_scores[category] = p1_scores_expected[category]
		p1_total_score = sum(p1_scores.values())


	#Player 2 Turn

	print("Player 2: Round %d" % (i+1))
	print("Choose the option.")
	print("1. Roll the dice")
	print("2. Check the score sheet")
	temp_option = input()
	option = int(temp_option) if temp_option in ['1', '2'] else temp_option
	print("")
	while True:
		if option not in [1, 2]:
			print("You input wrong option. Please enter 1 or 2.")
			print("")
			print("Choose the option.")
			print("1. Roll the dice")
			print("2. Check the score sheet")
			temp_option = input()
			option = int(temp_option) if temp_option in ['1', '2'] else temp_option
			print("")
		elif option == 2:
			print("+-------<Player 2>--------+")
			print("+-----------------+-------+")
			print("|    Category     | Score |")
			print("+-----------------+-------+")
			print("|      Aces       |%4s   |" % (str(p2_scores['Aces']) if p2_scores['Aces'] != 0 else '-'))
			print("|      Twos       |%4s   |" % (str(p2_scores['Twos']) if p2_scores['Twos'] != 0 else '-'))
			print("|     Threes      |%4s   |" % (str(p2_scores['Threes']) if p2_scores['Threes'] != 0 else '-'))
			print("|      Fours      |%4s   |" % (str(p2_scores['Fours']) if p2_scores['Fours'] != 0 else '-'))
			print("|      Fives      |%4s   |" % (str(p2_scores['Fives']) if p2_scores['Fives'] != 0 else '-'))
			print("|      Sixes      |%4s   |" % (str(p2_scores['Sixes']) if p2_scores['Sixes'] != 0 else '-'))
			print("|     Chance      |%4s   |" % (str(p2_scores['Chance']) if p2_scores['Chance'] != 0 else '-'))
			print("| Three of a Kind |%4s   |" % (str(p2_scores['Three of a Kind']) if p2_scores['Three of a Kind'] != 0 else '-'))
			print("| Four of a Kind  |%4s   |" % (str(p2_scores['Four of a Kind']) if p2_scores['Four of a Kind'] != 0 else '-'))
			print("|   Full House    |%4s   |" % (str(p2_scores['Full House']) if p2_scores['Full House'] != 0 else '-'))
			print("| Small Straight  |%4s   |" % (str(p2_scores['Small Straight']) if p2_scores['Small Straight'] != 0 else '-'))
			print("| Large Straight  |%4s   |" % (str(p2_scores['Large Straight']) if p2_scores['Large Straight'] != 0 else '-'))
			print("|     Yahtzee     |%4s   |" % (str(p2_scores['Yahtzee']) if p2_scores['Yahtzee'] != 0 else '-'))
			print("+-----------------+-------+")
			print("")
			print("Player 2 Current Score: %d" % p2_total_score)
			print("")
			print("Player 2: Round %d" % (i+1))
			print("Choose the option.")
			print("1. Roll the dice")
			print("2. Check the score sheet")
			temp_option = input()
			option = int(temp_option) if temp_option in ['1', '2'] else temp_option
			print("")

		else:
			break
	
	if option == 1:
		result = random.choices(range(1, 7), k = 5)
		print("Result of dice")
		print(result)
		print("Reroll the dice? [Y/N]", end = '')
		reroll = input()
		print("")
		while True:
			if reroll not in ['Y', 'N']:
				print("You input wrong option. Please enter [Y/N].")
				print("")
				print("Reroll the dice? [Y/N]", end = ' ')
				reroll = input()
				print("")
			else:
				break
		
		if reroll == 'Y':
			print("Choose all of dice that you want to keep. Seperate number with space.")
			print("If you want to change all of the dice, then input '0'")
			keep = list(input().split())
			print("")

			while True:
				keep_check = False
				if keep[0] == '0' and len(keep) == 1:
					break
				for j in keep:
					if j.isdigit() == False or (int(j) < 1 or int(j) > 5):
						keep_check = True
				if keep_check == False:
					break
				print("You input wrong option. Please enter between 1~5.")
				print("")
				print("Choose all of dice that you want to keep. Seperate number with space.")
				print("If you want to change all of the dice, then input '0'")
				keep = list(input().split())
				print("")

			for j in range(len(keep)):
				keep[j] = int(keep[j])

			if keep[0] == 0 and len(keep) == 1:
				result = random.choices(range(1, 7), k = 5)
			else:
				for j in range(5):
					if j+1 not in keep:
						result[j] = random.randint(1, 6)

			print("Result of dice")
			print(result)
			print("Reroll the dice? [Y/N]", end = ' ')
			reroll = input()
			print("")
			
			while True:
				if reroll not in ['Y', 'N']:
					print("You input wrong option. Please enter [Y/N].")
					print("")
					print("Reroll the dice? [Y/N]", end = ' ')
					reroll = input()
					print("")
				else:
					break

			if reroll == 'Y':
				print("Choose all of dice that you wnat to keep. Seperate number with space.")
				print("If you want to change all of the dice, then input '0'")
				keep = list(input().split())
				print("")

				while True:
					keep_check = False
					if keep[0] == '0' and len(keep) == 1:
						break
					for j in keep:
						if j.isdigit() == False or (int(j) < 1 or int(j) > 5):
							keep_check = True
					if keep_check == False:
						break
					print("You input wrong option. Please enter between 1~5.")
					print("")
					print("Choose all of dice that you want to keep. Seperate number with space.")
					print("If you want to change all of the dice, then input '0'")
					keep = list(input().split())
					print("")

				for j in range(len(keep)):
					keep[j] = int(keep[j])

				if keep[0] == 0 and len(keep) == 1:
					result = random.choices(range(1, 7), k = 5)
				else:
					for j in range(5):
						if j+1 not in keep:
							result[j] = random.randint(1, 6)

				print("Result of dice")
				print(result)

		temp_set = set(result)
		tok_check = False
		fok_check = False
		if len(temp_set) <= 3:
			for j in temp_set:
				if result.count(j) >= 4:
					tok_check = True
					fok_check = True
				elif result.count(j) >= 3:
					tok_check = True

		temp_sorted_setlist = sorted(list(set(result)))
		ss_check = False
		ls_check = False
		if (temp_sorted_setlist[:4] in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]] or temp_sorted_setlist[1:] in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]):
			ss_check = True
		if temp_sorted_setlist in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
			ls_check = True

		p2_scores_expected['Aces'] = result.count(1)
		p2_scores_expected['Twos'] = result.count(2) * 2
		p2_scores_expected['Threes'] = result.count(3) * 3
		p2_scores_expected['Fours'] = result.count(4) * 4
		p2_scores_expected['Fives'] = result.count(5) * 5
		p2_scores_expected['Sixes'] = result.count(6) * 6
		p2_scores_expected['Chance'] = sum(result)
		p2_scores_expected['Three of a Kind'] = sum(result) if tok_check else 0
		p2_scores_expected['Four of a Kind'] = sum(result) if fok_check else 0
		p2_scores_expected['Full House'] = 25 if (len(set(result)) == 2 and tok_check == True and fok_check == False) else 0
		p2_scores_expected['Small Straight'] = 30 if ss_check else 0
		p2_scores_expected['Large Straight'] = 40 if ls_check else 0
		p2_scores_expected['Yahtzee'] = 50 if len(set(result)) == 1 else 0

		print("")
		print("+-------<Player 2>--------+")
		print("+-----------------+-------+")
		print("|    Category     | Score |")
		print("+-----------------+-------+")
		print("|      Aces       |%4s   |" % str(p2_scores_expected['Aces']) if p2_scores['Aces'] == 0 else '-')
		print("|      Twos       |%4s   |" % str(p2_scores_expected['Twos']) if p2_scores['Twos'] == 0 else '-')
		print("|     Threes      |%4s   |" % str(p2_scores_expected['Threes']) if p2_scores['Threes'] == 0 else '-')
		print("|      Fours      |%4s   |" % str(p2_scores_expected['Fours']) if p2_scores['Fours'] == 0 else '-')
		print("|      Fives      |%4s   |" % str(p2_scores_expected['Fives']) if p2_scores['Fives'] == 0 else '-')
		print("|      Sixes      |%4s   |" % str(p2_scores_expected['Sixes']) if p2_scores['Sixes'] == 0 else '-')
		print("|     Chance      |%4s   |" % str(p2_scores_expected['Chance']) if p2_scores['Chance'] == 0 else '-')
		print("| Three of a Kind |%4s   |" % str(p2_scores_expected['Three of a Kind']) if p2_scores['Three of a Kind'] == 0 else '-')
		print("| Four of a Kind  |%4s   |" % str(p2_scores_expected['Four of a Kind']) if p2_scores['Four of a Kind'] == 0 else '-')
		print("|   Full House    |%4s   |" % str(p2_scores_expected['Full House']) if p2_scores['Full House'] == 0 else '-')
		print("| Small Straight  |%4s   |" % str(p2_scores_expected['Small Straight']) if p2_scores['Small Straight'] == 0 else '-')
		print("| Large Straight  |%4s   |" % str(p2_scores_expected['Large Straight']) if p2_scores['Large Straight'] == 0 else '-')
		print("|     Yahtzee     |%4s   |" % str(p2_scores_expected['Yahtzee']) if p2_scores['Yahtzee'] == 0 else '-')
		print("+-----------------+-------+")
		print("")
		print("Choose a category to record the score")
		category = input()
		print("")
		
		while True:
			if category not in p2_scores.keys() or p2_scores[category] != 0:
				print("You input wrong category. Please enter again.")
				print("")
				print("Choose a category to record the score")
				category = input()
				print("")
			else:
				break
		p2_scores[category] = p2_scores_expected[category]
		p2_total_score = sum(p2_scores.values())
