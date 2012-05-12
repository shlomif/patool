python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
# 'brp-compress' compresses the manpages without distutils knowing.
# The sed script appends a * suffix to the affected manpage filename.
# This is because they can be installed under any of several extensions.
RPM_MANDIR=usr/share/man
RPM_LOCALMANDIR=usr/local/share/man

sed -i -e 's@man/man\([[:digit:]]\)/\(.\+\.[[:digit:]]\)$@man/man\1/\2*@' INSTALLED_FILES
