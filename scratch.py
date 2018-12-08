import time

testTask = Task()

testTask.create_task()

print(testTask.category)

print(time.localtime())

currentTime = time.asctime(time.localtime())

print(currentTime)

startTime = time.asctime(time.localtime())

startTimer = time.time()

print(startTime)

input("press enter to stop timer")

endTime = time.asctime(time.localtime())

endTimer = time.time()

elapsedTime = endTimer - startTimer

print(endTime)

print("Total time elapsed: %s" % elapsedTime)

testTask.print_task()

testTask.main_menu()
