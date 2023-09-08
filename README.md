# Before starting
I would like to say, that it's my **Harvard's CS50 Python** final assignment project. It's made with the topics that was covered in that course: 
* regexp
* File I/O
* OOP

# PyGit
You don't trust to cloud platforms? Want to save versions locally on your pc? Don't want to learn those fancy syntaxes? Use pygit. Pygit is CLI tool, that allows you to save and track changes in simple .txt files on your PC without need in Internet or trusting your files to cloud platform.
## Downloading
Just download pygit.py to folder where all of your projects saved, like ```C:/coding``` and you're good to go! Or more comfortable option is to convert pygit.py to .exe file via ```PyInstaller``` and adding it to ```PATH``` in system variables.
## Use
python pygit.py [-a] [-n] [-t]
-a -> action/instruction that needs to be done. Options:
* ```crp``` for "create project"
* ```actp``` for "activate project"
* ```crf``` for creating files
* ```addc``` for adding commits
* ```lc``` for listing commits
* ```retc``` for returning commit
* ```scid``` for search commit id
* ```delf``` for deleting file
* ```delp``` for deleting project
-n -> name of a file or a project
-t -> additional text, like a path to project when creating it or comment when adding a commit _(only with crp, addc, retc, scid)_ \n
**Example:**\n
```python pygit.py -a crp -n myproject -t C:/coding/myproject```
**After creating a project, you need to activate it to be able to make commits and do other things**
```python pygit.py -a actp -n myproject```
And then you're good to go and push commits:
```python pygit.py -a addc -n main.py -t "created main class"```
As number of commits go up, you can list them:
```python pygit.py -a lc -n main.py```
This outputs next:
0 created main class
1 deleted main class
2 returned main class
The number on the left is ID of commit, the text on the right is description of commit
To return commit you need to know it's ID
```python pygit.py -a retc -n main.py -t 0``` 0 is ID of a commit
In case if you want to quickly search for commit by it's description, there is:
```python pygit.py -a scid -n main.py -t "created main" ```
## I hope you find this useful or atleast rate my job

