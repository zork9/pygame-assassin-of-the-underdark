# Copyright (C) Johan Ceuppens 2014
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from filelines2list import *
 
def gplheader2list(AUTHOR = "Johan Ceuppens", YEAR = "2014", filename = './gpl.txt'):
	l = filelines2list(filename)
	l.insert(0, "\n")
	l.insert(1, "# Copyright (C) " + AUTHOR + " " + YEAR + "\n")

	return l

