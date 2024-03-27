# python-educational-program

It's a window app for teaching children counting basic operation. I've used python and tkinter library.

The program consists of three game modes: operation, areas and text task. The user can choose one of them and select the number of tasks he wants to answer.

![1](https://user-images.githubusercontent.com/44522588/171942095-02336baa-10de-4952-80ce-88143a8d4e28.png)

The program takes the paths of txt files which contains task description. The files for the operations contain equations using x, y and z variables, e.g. x+y+z, for which the values are randomized each time.

For text tasks, the input file provides the contents of the tasks, which are displayed to the user, as well as the actions by which the computer can calculate the correct answer. By randomizing the variables x, y, z, a large number of tasks can be easily created. It is also possible for the user to easily add new tasks.

![4](https://user-images.githubusercontent.com/44522588/171944830-4563842d-f4ca-474d-b9e8-a0507b8d8fc7.png)

The game consists in displaying a task to be counted, the user has to solve a mathematical task and give an answer. The program checks the correctness of the answer and displays an appropriate message.

![3](https://user-images.githubusercontent.com/44522588/171943862-1e57b126-e8cc-423b-a775-5bf04270b0e6.png)

The program counts the number of points earned by the user and displays how many tasks remain to be solved in the series.

![5](https://user-images.githubusercontent.com/44522588/171943996-109833d2-70a1-482d-8205-5c73d4081119.png)


how to run:
1. Double click main.py
2. Add 3 filepath input.txt from the folder
3. Have fun! :)


how to add tasks yourself:
1. Open file input2 or input3
2. Firstly add a new row with operation using x, y, z and operators +, -, *, /
3. In the next row add a task descrition (text)
4. In the places of text where should be numbers, write #x, #y, #z
5. Run again main.py
