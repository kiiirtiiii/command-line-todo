A command-line program that lets you manage your todos.

- It uses file handling hence, the tasks are preserved for the next time you open the application.


## Usage

### 1. Help

Executing the command `help` prints the CLI usage.

> help

```
Usage :-

add "todo item" # Add a new todo
ls              # Show remaining todos
del "NUMBER"    # Delete a todo
done "NUMBER"   # Complete a todo
help            # Show usage
report          # Statistics
close           # Close the application
```   

### 2. List all pending todos

Use the `ls` command to see all the todos that are not yet complete. The most recently added todo will be displayed first.

> ls

```
[2] change light bulb
[1] water the plants
```

### 3. Add a new todo

Use the `add` command

> add "the thing i need to do"

```
Added todo: "the thing i need to do"
```

### 4. Delete a todo item

Use the `del` command to remove a todo item by its number.

> del 3

```
Deleted todo #3
```

Attempting to delete a non-existent todo item will display an error message.

> del 5

```
Error: todo #5 does not exist. Nothing deleted.
```

### 5. Mark a todo item as completed

Use the `done` command to mark a todo item as completed by its number.

> done 1

```
Marked todo #1 as done.
```

Attempting to mark a non-existed todo item as completed will display an error message.

> done 5

```
Error: todo #5 does not exist.
```

### 6. Generate a report

Use the `report` command to see the latest tally of pending and completed todos.

> report

```
Pending: 2 Completed: 3
```

### 7. Close the application

Use `close` command to close the application.

> close

```
Are you sure, you want to close the application?
Press "enter" to confirm
Press "any key" to decline
```


## Screenshot of a working project

### Command line to do list:

![ss of cmd](https://user-images.githubusercontent.com/61161878/120613626-08557200-c474-11eb-9117-d47b9982e6b0.jpg)


### Text files created:

![Screenshot (23)](https://user-images.githubusercontent.com/61161878/120613679-12777080-c474-11eb-9414-3a0b19576b6a.png)
