# -*- coding: utf-8 -*-
# Copyright (C) 2010-2011 Bastian Kleineidam
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
import unittest
import os
import shutil
import patoolib
from tests import datadir, needs_program, needs_one_program

class ArchiveRepackTest (unittest.TestCase):

    @needs_program('diff')
    @needs_one_program(('tar', 'star', '7z'))
    @needs_one_program(('zip', '7z'))
    def test_repack (self):
        archive1 = os.path.join(datadir, "t.tar")
        tmpdir = patoolib.util.tmpdir()
        try:
            archive2 = os.path.join(tmpdir, "t.zip")
            patoolib.handle_archive(archive1, "repack", archive2)
            res = patoolib.handle_archive(archive1, "diff", archive2)
        finally:
            shutil.rmtree(tmpdir)
        # both archives have the same data
        self.assertEqual(res, 0)
