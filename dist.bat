:: Create patool Windows distribution file
:: Copyright (C) 2010 Bastian Kleineidam
:: This program is free software: you can redistribute it and/or modify
:: it under the terms of the GNU General Public License as published by
:: the Free Software Foundation, either version 3 of the License, or
:: (at your option) any later version.
::
:: This program is distributed in the hope that it will be useful,
:: but WITHOUT ANY WARRANTY; without even the implied warranty of
:: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
:: GNU General Public License for more details.
::
:: You should have received a copy of the GNU General Public License
:: along with this program.  If not, see <http://www.gnu.org/licenses/>.
@echo off
set PYDIR=c:\python27
rd build /s /q
rd dist /s /q
%PYDIR%\python.exe setup.py bdist_wininst
pause
