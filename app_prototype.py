#!/usr/bin/python
# python 3.7
# -*- coding: utf-8 -*-
# ==============================================================================
#
#         FILE: app_prototype.py
#
#        USAGE: ./app_prototype.py
#
#  DESCRIPTION: # App that tracks time and provides a log of how many hours you
#                 have done a certain task for//divided into categories and
#                 sub-categories.
#
#
#       AUTHOR: Justen Crockett
#      VERSION: 1.0
#      CREATED: 12/07/2018
# ==============================================================================

import time


class Task:

    def __init__(self):
        self.generalCategory = 'Free-Time'
        self.category = 'Reading'
        self.subCategory = 'Poetry'
        self.status = False

    def main_menu(self):
        while True:                                 # IDEAS: Show options - create new task, start a task, task summary
            print("\n=============================") # Under start a task menu will show all the tasks you have created-
            print("========= MAIN MENU =========")  # to show you which tasks you can choose from
            print("=============================")  # Task summary show time spent on each task, can show by date range
            print("=    1. Create New Task     =")
            print("=    2. Start a Task        =")
            print("=    3. Task Summary        =")
            print("=    9. Exit Program        =")
            print("=============================\n")

            choice = int(input("Choose option from list: "))

            print('\n')

            if choice == 1:
                self.new_task_menu()
            elif choice == 2:
                self.start_task_menu()
            elif choice == 3:
                self.task_summary_menu()
            elif choice == 9:
                print("EXITING PROGRAM...")
                return
            else:
                print("Please make a choice from the window above.")
                return

    def new_task_menu(self):
        print("=============================")
        print("====== 1. Productive  =======")
        print("====== 2. Free-Time   =======")
        print("=============================\n")

        choice_new_task = int(input('Choose task category from above: '))

        if choice_new_task == 1:
            print("Productive")
        elif choice_new_task == 2:
            print("Free-Time")
        else:
            print("Please restart program and enter valid choice")

    def start_task_menu(self):
        print("Start task menu!!")

    def task_summary_menu(self):
        print("Task summary menu!!!")

    def create_task(self):
        self.generalCategory = input("Enter task general category: ")
        self.category = input("Enter task category: ")
        self.subCategory = input("Enter task sub category: ")

    def store_tasks(self):
        print("placeholder")

    def print_task(self):
        print("\nGeneral Category: %s\n" % self.generalCategory)
        print("Category: %s\n" % self.category)
        print("General Category: %s\n" % self.subCategory)

    def start_task(self):
        self.status = True
        start_time = time.time()
        input("Press enter when you want to stop task")
        self.end_task(start_time)

    def end_task(self, start_time):
        self.status = False
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Time elapsed: %s" % elapsed_time)


TEST_OBJECT = Task()

TEST_OBJECT.main_menu()
