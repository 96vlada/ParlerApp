import feedparser

import os.path
from tkinter import *
from tkinter import ttk
import tkinter as tk

import csv

from login import ParlerLogin
from unfollowing import ParlerUnfollow
from publish import PublishFeed

from mainDB import MainDB
from settingsPage import SettingsPage
import sys


########### DB DATA ##############

loginCredRow        = MainDB.login()
HashCredRow         = MainDB.hashtags()
BadgesCredRow       = MainDB.badges()
FeedsCredRow        = MainDB.feedsCred()
FeedsHashCredRow    = MainDB.feedsHashCred()
FeedsNumCredRow     = MainDB.feedsNumb()
UnfollowExcCredRow  = MainDB.unfollowCred()
UnfDaysCredRow      = MainDB.unFollowDays()

window = tk.Tk()
window.wm_iconbitmap('code.ico')
window.geometry('565x980+50+10')

window.title("ParlerApp");


###########################################
# APP TABS

tcMain = ttk.Notebook(window)
tab1 = ttk.Frame(tcMain)
tab2 = ttk.Frame(tcMain)
tcMain.add(tab1, text ='Main')
tcMain.add(tab2, text ='Settings')
tcMain.grid(row = 0)


loginUserLabel = tk.Label(tab1, text="Parler Username")
loginUserLabel.grid(column=0, row=1, padx=10, pady=2)


storedUsername = StringVar(tab1, value=loginCredRow[0])
loginUser = tk.Entry(tab1, textvariable=storedUsername, font = ('courier', 12, 'bold'))
loginUser.grid(column=0, row=2, pady=10)

loginPassLabel = tk.Label(tab1, text="Parler Password")
loginPassLabel.grid(column=1, row=1, padx=10, pady=2)

storedPassword = StringVar(tab1, value=loginCredRow[1])
loginPass = tk.Entry(tab1, textvariable=storedPassword, font = ('courier', 12, 'bold'))
loginPass.grid(column=1, row=2, pady=10)

# follow module
followModule = tk.Label(tab1, text="Follow module",
 foreground="white",
 background="black", 
 width=47,
 height=1
	)
followModule.config(font=("Courier", 15))
followModule.grid(row=3, columnspan=2)


followModuleHashLabel = followModule = tk.Label(tab1, text="Follow by hashtag (separated by commas)")
followModuleHashLabel.grid(column=0, row=4, padx=10, pady=10)
followModuleHash = tk.Text(tab1, font = ('courier', 12, 'bold'), width=20, height=3)
followModuleHash.grid(column=0, row=5)

HashCredString = ""
for HashCred in HashCredRow:
    HashCredString += HashCred + ","
followModuleHash.insert(tk.END, HashCredString[:-1])




valores = StringVar()
valores.set("all gold rss verified early parler_emp private influencer")

followModuleBadgeLabel = followModule = tk.Label(tab1,text="Follow by badge ( * OR )")
followModuleBadgeLabel.grid(column=1, row=4, padx=10, pady=10)
followModuleBadge = Listbox(tab1, listvariable=valores, selectmode=MULTIPLE, width=25, height=7)


selectedBadgesToFollow = []
if(os.path.exists('database/badgesCSV.csv')):
    with open('database/badgesCSV.csv', newline='') as f:
        reader = csv.reader(f)
        for badge in f:
            badgeArr = badge.split(",")
            for x in badgeArr:
                selectedBadgesToFollow.append(x.rstrip())
                selectedBadgesToFollow = list(filter(None, selectedBadgesToFollow))

                        

for sbtf in selectedBadgesToFollow:
    followModuleBadge.selection_set(followModuleBadge.get(0, "end").index(str(sbtf)))

followModuleBadge.grid(column=1, row=5)


# followModuleBadge = tk.Text(tab1, font = ('courier', 12, 'bold'), width=20, height=3)
# followModuleBadge.grid(column=1, row=5)

# BadgeCredString = ""
# for BadgeCred in BadgesCredRow:
#     BadgeCredString += BadgeCred + ","
# followModuleBadge.insert(tk.END, BadgeCredString[:-1])


# ###########################################################################
# UNFOLLOW MODULE

# login
unfollowSection = tk.Label(tab1, text="Unfollow module",
 foreground="white",
 background="black", 
 width=47,
 height=1
    )
unfollowSection.config(font=("Courier", 15))
unfollowSection.grid(row=10, columnspan=2)


unfollowExceptionLebel = followModule = tk.Label(tab1,text="Users you don't want to unfollow (separated by commas) *Name")
unfollowExceptionLebel.grid(row=11, columnspan=2, padx=10, pady=10)
unfollowException = tk.Text(tab1, font = ('courier', 12, 'bold'), width=45, height=3)
unfollowException.grid(row=12, columnspan=2)

UnfollowCredString = ""
for UnfollowCred in UnfollowExcCredRow:
    UnfollowCredString += UnfollowCred + ","
unfollowException.insert(tk.END, UnfollowCredString[:-1])


dayForUnfollowLabel = tk.Label(tab1,text="Days for the unfollow module to start :")
dayForUnfollowLabel.grid(row=13, column=0, padx=10, pady=10)

storedUnfDays = StringVar(tab1, value=UnfDaysCredRow[0])
dayForUnfollow = tk.Entry(tab1, textvariable=storedUnfDays, font = ('courier', 12, 'bold'))
dayForUnfollow.grid(column=1, row=13, pady=10)

# UNFOLLOW MODULE
# ###########################################################################



def followingSubmited():

    loginCred = [loginUser.get(), loginPass.get()]
    hashtagsDB = followModuleHash.get('1.0', 'end-1c').split(",")
    # badgesDB = followModuleBadge.get('1.0', 'end-1c').split(",")
    badgesDB = []
    # hashtagsNumber = [int(followModuleHashLNumber.get())]

    openDBCsv = open('database/loginCSV.csv', 'w')
    writerCSV = csv.writer(openDBCsv)
    writerCSV.writerow(loginCred)
    openDBCsv.close()

    openDBCsvHash = open('database/hashtagCSV.csv', 'w')
    writerCSV = csv.writer(openDBCsvHash)
    writerCSV.writerow(hashtagsDB)
    openDBCsvHash.close()

    for i in followModuleBadge.curselection():
        badgesToFollow = followModuleBadge.get(i)
        badgesDB.append(badgesToFollow)

    openDBCsvBadge = open('database/badgesCSV.csv', 'w')
    writerCSV = csv.writer(openDBCsvBadge)
    writerCSV.writerow(badgesDB)
    openDBCsvBadge.close()

    # ParlerLogin("Proccessing", followModuleHash.get('1.0', 'end-1c'), badgesDB, loginUser.get(), loginPass.get())



def unfollowingSubmited():

    UnfollowDB = unfollowException.get('1.0', 'end-1c').split(",")
    openDBCsvUnfollow = open('database/unfollowExcCSV.csv', 'w')
    writerCSV = csv.writer(openDBCsvUnfollow)
    writerCSV.writerow(UnfollowDB)
    openDBCsvUnfollow.close()


    UnfollowDB = []
    UnfollowDB.append(dayForUnfollow.get())
    openDBCsvUnfollow = open('database/unfDaysCSV.csv', 'w')
    writerCSV = csv.writer(openDBCsvUnfollow)
    writerCSV.writerow(UnfollowDB)
    openDBCsvUnfollow.close()

    # ParlerUnfollow(loginUser.get(), loginPass.get(), unfollowException.get('1.0', 'end-1c').split(","), 20)

# saveFollowBtn = tk.Button(tab1, text ="Save", command = followingSubmited)
# saveFollowBtn.grid(row=8, column=0,  padx=10, pady=10)

followButton = tk.Button(tab1, text ="Save Follow", command = followingSubmited)
followButton.grid(row=8, columnspan=2,  padx=10, pady=10)


unfollowButton = tk.Button(tab1, text ="Save Unfollow", command = unfollowingSubmited)
unfollowButton.grid(row=14, columnspan=2,  padx=10, pady=10)




# ###########################################################################
# PUBLISH FEED MODULE

# Post Scheduler
post_schedulerSection = tk.Label(tab1, text="Post Scheduler",
 foreground="white",
 background="black", 
 width=47,
 height=1
    )
post_schedulerSection.config(font=("Courier", 15))
post_schedulerSection.grid(row=15, columnspan=2)

post_schedulerLabel = followModule = tk.Label(tab1, text="Enter feeds url (separated by commas)")
post_schedulerLabel.grid(row=18, columnspan=2, padx=10, pady=10)
post_scheduler = tk.Text(tab1, font = ('courier', 12, 'bold'), width=45, height=6)
post_scheduler.grid(row=19, columnspan=2)

FeedCredString = ""
for FeedCred in FeedsCredRow:
    FeedCredString += FeedCred + ","
post_scheduler.insert(tk.END, FeedCredString[:-1])




###################################################
# HASHTAGS FORPUBLISH MODULE

post_schedulerHashLabel = followModule = tk.Label(tab1, text="Enter hashtags (separated by commas)")
post_schedulerHashLabel.grid(row=20, columnspan=2, padx=10, pady=10)
post_schedulerHash = tk.Text(tab1, font = ('courier', 12, 'bold'), width=45, height=3)
post_schedulerHash.grid(row=21, columnspan=2)

FeedHashCredString = ""
for FeedHashCred in FeedsHashCredRow:
    FeedHashCredString += FeedHashCred + ","
post_schedulerHash.insert(tk.END, FeedHashCredString[:-1])

# HASHTAGS FORPUBLISH MODULE
###################################################




# storedPassword = StringVar(window, value=loginCredRow[1])

post_schedulerNumLabel = followModule = tk.Label(tab1, text="Number of items per feed per iteration")
post_schedulerNumLabel.grid(row=22, columnspan=2, padx=10, pady=10)

storedFeedNum = StringVar(tab1, value=FeedsNumCredRow[0])
post_schedulerNumber = tk.Entry(tab1, textvariable=storedFeedNum, font = ('courier', 12, 'bold'))
post_schedulerNumber.grid(row=23, columnspan=2)


def publishFeedSubmited():
    feedDB = post_scheduler.get('1.0', 'end-1c').split(",")
    openDBCsvFeed = open('database/feedsCSV.csv', 'w')
    writerCSV = csv.writer(openDBCsvFeed)
    writerCSV.writerow(feedDB)
    openDBCsvFeed.close()

    feedHashDB = post_schedulerHash.get('1.0', 'end-1c').split(",")
    openDBCsvFeedHash = open('database/feedsHashCSV.csv', 'w')
    writerCSV = csv.writer(openDBCsvFeedHash)
    writerCSV.writerow(feedHashDB)
    openDBCsvFeedHash.close()


    feedNumDB = []
    feedNumDB.append(post_schedulerNumber.get())
    openDBCsvFeedNum = open('database/feedsNumCSV.csv', 'w')
    writerCSV = csv.writer(openDBCsvFeedNum)
    writerCSV.writerow(feedNumDB)
    openDBCsvFeedNum.close()

    # PublishFeed(loginUser.get(), loginPass.get(), post_scheduler.get('1.0', 'end-1c'), post_schedulerNumber.get(), post_schedulerHash.get('1.0', 'end-1c'))

post_schedulerButton = tk.Button(tab1, text ="Save Publish Scheduler", command = publishFeedSubmited)
post_schedulerButton.grid(row=24, columnspan=2,  padx=10, pady=10)

# PUBLISH FEED MODULE
# ###########################################################################
badgesDB2 = []
for i in followModuleBadge.curselection():
        badgesToFollow = followModuleBadge.get(i)
        badgesDB2.append(badgesToFollow)
SettingsPage(window, tab2, tk, loginUser.get(), loginPass.get(), post_scheduler.get('1.0', 'end-1c'), post_schedulerNumber.get(), post_schedulerHash.get('1.0', 'end-1c'), followModuleHash.get('1.0', 'end-1c'), badgesDB2, unfollowException.get('1.0', 'end-1c').split(","))


def reopenParlerApp():
    # window.destroy()
    # exec(open(os.path.abspath("") + "\\" + "main.py").read())
    python = sys.executable
    os.execl(python, python, * sys.argv)


reopenPar = tk.Button(tab1, text ="Save All", command = reopenParlerApp)
reopenPar.grid(row=30, columnspan=2,  padx=10, pady=10)

tk.mainloop()