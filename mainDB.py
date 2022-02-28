import os
import csv

class MainDB():
	def login():
		if(os.path.exists('database/loginCSV.csv')):
			with open('database/loginCSV.csv', newline='') as f:
				reader = csv.reader(f)
				loginCredRow = next(reader)
				for login in f:
					loginCredRow.append(login)     
		else:
			loginCredRow = []
			loginCredRow.append("")
			loginCredRow.append("")


		return loginCredRow

	def hashtags():
		HashCredRow = []
		if(os.path.exists('database/hashtagCSV.csv')):
			with open('database/hashtagCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for hashtag in f:
					HashCredRow.append(hashtag.rstrip())
					HashCredRow = list(filter(None, HashCredRow))
		else:
			HashCredRow = []

		return HashCredRow

	def badges():
		BadgesCredRow = []
		if(os.path.exists('database/badgesCSV.csv')):
			with open('database/badgesCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for hashtag in f:
					BadgesCredRow.append(hashtag.rstrip())
					BadgesCredRow = list(filter(None, BadgesCredRow))
		else:
			BadgesCredRow = []

		return BadgesCredRow


	def feedsCred():
		FeedsCredRow = []
		if(os.path.exists('database/feedsCSV.csv')):
			with open('database/feedsCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for feed in f:
					FeedsCredRow.append(feed.rstrip())
					FeedsCredRow = list(filter(None, FeedsCredRow))
		else:
			FeedsCredRow = []

		return FeedsCredRow

	def feedsHashCred():
		FeedsHashCredRow = []
		if(os.path.exists('database/feedsHashCSV.csv')):
			with open('database/feedsHashCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for feedHash in f:
					FeedsHashCredRow.append(feedHash.rstrip())
					FeedsHashCredRow = list(filter(None, FeedsHashCredRow))
		else:
			FeedsHashCredRow = []

		return FeedsHashCredRow


	def feedsNumb():
		FeedsNumCredRow = []
		if(os.path.exists('database/feedsNumCSV.csv')):
			with open('database/feedsNumCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for feedNum in f:
					FeedsNumCredRow.append(feedNum.rstrip())
					FeedsNumCredRow = list(filter(None, FeedsNumCredRow))
		else:
			FeedsNumCredRow = ['']

		return FeedsNumCredRow

	def unfollowCred():
		UnfollowExcCredRow = []
		if(os.path.exists('database/unfollowExcCSV.csv')):
			with open('database/unfollowExcCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for unfollowExc in f:
					UnfollowExcCredRow.append(unfollowExc.rstrip())
					UnfollowExcCredRow = list(filter(None, UnfollowExcCredRow))
		else:
			UnfollowExcCredRow = ['']

		return UnfollowExcCredRow


	# #########################################################################
	# SETTINGS PAGE


	def followModuleCron():
		FollowModuleCronCredRow = []
		if(os.path.exists('database/followModuleCronCSV.csv')):
			with open('database/followModuleCronCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for item in f:
					FollowModuleCronCredRow.append(item.rstrip())
					FollowModuleCronCredRow = list(filter(None, FollowModuleCronCredRow))
		else:
			FollowModuleCronCredRow = ['']
		return FollowModuleCronCredRow

	def unFollowModuleCron():
		UnfollowModuleCronCredRow = []
		if(os.path.exists('database/unFollowModuleCronCSV.csv')):
			with open('database/unFollowModuleCronCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for item in f:
					UnfollowModuleCronCredRow.append(item.rstrip())
					UnfollowModuleCronCredRow = list(filter(None, UnfollowModuleCronCredRow))
		else:
			UnfollowModuleCronCredRow = ['']
		return UnfollowModuleCronCredRow


	def postSchCron():
		PostSchCronCredRow = []
		if(os.path.exists('database/postSchCronCSV.csv')):
			with open('database/postSchCronCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for item in f:
					PostSchCronCredRow.append(item.rstrip())
					PostSchCronCredRow = list(filter(None, PostSchCronCredRow))
		else:
			PostSchCronCredRow = ['']
		return PostSchCronCredRow


	def followLimitCron():
		FollowLimitCronCredRow = []
		if(os.path.exists('database/followLimitCronCSV.csv')):
			with open('database/followLimitCronCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for item in f:
					FollowLimitCronCredRow.append(item.rstrip())
					FollowLimitCronCredRow = list(filter(None, FollowLimitCronCredRow))
		else:
			FollowLimitCronCredRow = ['']
		return FollowLimitCronCredRow


	def unFollowLimitCron():
		UnfollowLimitCronCredRow = []
		if(os.path.exists('database/unfollowLimitCronCSV.csv')):
			with open('database/unfollowLimitCronCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for item in f:
					UnfollowLimitCronCredRow.append(item.rstrip())
					UnfollowLimitCronCredRow = list(filter(None, UnfollowLimitCronCredRow))
		else:
			UnfollowLimitCronCredRow = ['']
		return UnfollowLimitCronCredRow


	def unFollowDays():
		UnfollowDaysCredRow = []
		if(os.path.exists('database/unfDaysCSV.csv')):
			with open('database/unfDaysCSV.csv', newline='') as f:
				reader = csv.reader(f)
				for item in f:
					UnfollowDaysCredRow.append(item.rstrip())
					UnfollowDaysCredRow = list(filter(None, UnfollowDaysCredRow))
		else:
			UnfollowDaysCredRow = ['']
		return UnfollowDaysCredRow

			