
Running the game :
------------------

run 'python game.py' inside the src/ directory to run the game, pics/
directory must be in the directory you run python in.
You need to install pygame in your python distribution, see http://pygame.org

Running the Python Shell :
--------------------------

This is work in progress :

run 'python pythonshellwindowmain.py' inside the src/ directory to run the shell window, pics/
directory must be in the directory you run python in.

These are the commands :

	def gets parsed to a tabulated (with spaces) line and you jump into
	the text area. If you remove the "..." on a new line, python eval
	function gets called on the full textarea buffer

main screen :
-------------

- Escape key : quit game
- t key : talk (if possible)
- i key : go to inventoryitmes screen
- j key : go to character sheet screen
- o key : go to spellitems screen
- x key : use item, pickup item or enemy
- z key : fight (with main weapon)
- s key : use selected inventory item
- c key : cast selected spell item 
- arrow keys : movement

character selection screen :
----------------------------

use mouse to select a picture as character, if you don't click a character or just 
press a key ni this screen,
a random char is made.

inventory and/or spelbook and/or character sheet screen :
---------------------------------------------------------

- 'z' or 'x' key : exit inventory screen and select itme under rectangle
- arrow keys : movement in inventory
- Escape key : exit screen

Plugins :
---------

Inside src/ there is a plugins directory which gets executed by the program by using
the imagepluginmanager class
All scripts get loaded at the start of the game.
Read the python files in the src/plugins/ directory for more information.

Python scripting shell window :
-------------------------------

- Escape key : quit window 
- keyboard keys

Scripts :
---------

In the scripts directory there are character player file generation scripts.
