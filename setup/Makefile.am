# vim:set noet ts=4:
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2007-2008 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2009 Hideaki ABE <abe.sendai@gmail.com>
# Copyright (c) 2007-2010 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

setup_anthy_PYTHON = \
	prefs.py \
	anthyprefs.py \
	main.py \
	setup.glade \
	$(NULL)

setup_anthydir = $(datadir)/ibus-anthy/setup

libexec_SCRIPTS = ibus-setup-anthy

CLEANFILES = \
	*.pyc \
	$(NULL)

EXTRA_DIST = \
	ibus-setup-anthy.in \
	$(NULL)

test:
	$(ENV) DBUS_DEBUG=true \
		   LANG=en_US \
		   PYTHONPATH=$(abs_top_srcdir):$(pyexecdir) \
		   IBUS_LOCALEDIR=@localedir@ \
		   $(PYTHON) $(srcdir)/main.py

