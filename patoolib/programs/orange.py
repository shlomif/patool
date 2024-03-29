# -*- coding: utf-8 -*-
# Copyright (C) 2011-2012 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Archive commands for the orange program."""

def extract_cab (archive, compression, cmd, **kwargs):
    """Extract a CAB archive."""
    cmdlist = [cmd, '-d', kwargs['outdir']]
    if kwargs['verbose']:
        cmdlist.append('-D 2')
    else:
        cmdlist.append('-D 1')
    cmdlist.append(archive)
    return cmdlist
