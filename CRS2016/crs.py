"""
author: Jan Aldous Torres

This project was created right after the submission of SEG project run where my group submitted
sub par code. Started this project to look back at some python code that I can improve on and fix.

Created this project 2 years after dropping out of UP. Just want to check if I knew more about python
through project run and see what was wrong with my python code before.

Good luck to me.

"""
import operator

courses = []
students = []
teachers = []
admins = []


def login_menu():
    """
    Login. First method run, and first menu seen by user.
    :return:
    """

    while(True):
        option = input("Login \n[1] Student \n[2] Admin \n[3] Teacher \n[4] Quit \nEnter option: ")
        if option == "1":
            print("student menu")
        elif option == "2":
            print("admin menu")
        elif option == "3":
            print("teacher menu")
        elif option == "4":
            print("quitting...")
            exit(0)
        else:
            print("Invalid input. PLease try again.")

login_menu()

class Block(object):
    def __init__(self):
        self.courses = []

class Day(object):
    def __init__(self):
        self.block_1 = Block()
        self.block_2 = Block()
        self.block_3 = Block()
        self.block_4 = Block()
        self.block_5 = Block()
        self.block_6 = Block()

class Schedule(object):
    def __init__(self):
        self.mon = Day()
        self.tue = Day()
        self.wed = Day()
        self.thu = Day()
        self.fri = Day()