# vim:set noet ts=4:
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2007-2008 Peng Huang <shawn.p.huang@gmail.com>
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

engine_anthy_PYTHON = \
	engine.py \
	factory.py \
	jastring.py \
	kana.py \
	main.py \
	romaji.py \
	segment.py \
	tables.py \
	thumb.py \
	$(NULL)
engine_anthydir = $(pkgdatadir)/engine

anthy_DATA = \
	anthy.py \
	$(NULL)
anthy_LTLIBRARIES = _anthy.la
anthydir = @pyexecdir@

_anthy_la_SOURCES = \
	$(NULL)

nodist__anthy_la_SOURCES = \
	anthy_wrap.c \
	$(NULL)

_anthy_la_CFLAGS = \
	@ANTHY_CFLAGS@ \
	@PYTHON_CFLAGS@ \
	$(NULL)

_anthy_la_LDFLAGS = \
	@ANTHY_LIBS@ \
	@PYTHON_LIBS@ \
	-avoid-version \
	-module \
	$(NULL)

libexec_SCRIPTS = ibus-engine-anthy
engine_DATA = anthy.xml
enginedir = $(datadir)/ibus/component

anthy.py anthy_wrap.c: anthy.i
	$(SWIG) -python -I/usr/include -o anthy_wrap.c $(srcdir)/anthy.i

anthy.xml: anthy.xml.in
	( \
		libexecdir=${libexecdir}; \
		pkgdatadir=${pkgdatadir}; \
		s=`cat $<`; \
		eval "echo \"$${s}\""; \
	) > $@

test:
	$(ENV) \
		DBUS_DEBUG=true \
		IBUS_ANTHY_PKGDATADIR=$(abs_top_srcdir) \
		PYTHONPATH=$(builddir)/.libs:@pyexecdir@ \
		$(PYTHON) \
		$(srcdir)/main.py

EXTRA_DIST = \
	anthy.i \
	anthy.xml.in.in \
	ibus-engine-anthy.in \
	$(NULL)

CLEANFILES = \
	anthy.xml \
	anthy.py \
	anthy_wrap.* \
	*.pyc \
	$(NULL)

DISTCLEANFILES = \
	$(NULL)
