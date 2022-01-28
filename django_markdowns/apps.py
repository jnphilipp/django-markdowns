# -*- coding: utf-8 -*-
# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:
# Copyright (C) 2021-2022 J. Nathanael Philipp (jnphilipp) <nathanael@philipp.land>
#
# This file is part of django_markdowns.
#
# django_markdowns is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django_markdowns is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django_markdowns.  If not, see <http://www.gnu.org/licenses/>.
"""Markdown Django app config."""


from django.apps import AppConfig


class MarkdownConfig(AppConfig):
    """Markdown app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "django_markdowns"
