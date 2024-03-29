# -*- coding: utf-8 -*-
# Copyright (C) 2010-2012 Bastian Kleineidam
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
"""Archive commands for the arc program."""
import os

def extract_arc (archive, compression, cmd, **kwargs):
    """Extract a ARC archive."""
    # Since extracted files will be placed in the current directory,
    # the cwd argument has to be the output directory.
    cmdlist = [cmd, 'x', os.path.abspath(archive)]
    return (cmdlist, {'cwd': kwargs['outdir']})

def list_arc (archive, compression, cmd, **kwargs):
    """List a ARC archive."""
    cmdlist = [cmd]
    if kwargs['verbose']:
        cmdlist.append('v')
    else:
        cmdlist.append('l')
    cmdlist.append(archive)
    return cmdlist

def test_arc (archive, compression, cmd, **kwargs):
    """Test a ARC archive."""
    return [cmd, 't', archive]

def create_arc (archive, compression, cmd, *args, **kwargs):
    """Create a ARC archive."""
    cmdlist = [cmd, 'a', archive]
    cmdlist.extend(args)
    return cmdlist
