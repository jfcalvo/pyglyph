#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import cairo
from StringIO import StringIO
from make.template import Template


#CHARACTER_LIST = '''ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890"!'?.,;:()[]{}<>|/@\^$-%+=#_&~*'''
CHARACTER_LIST = '''1234567890'''

# Create a Cairo image surface:
imagesize = (256,32)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *imagesize)
cr = cairo.Context(surface)
padding = 2

# Choose a font (look in /Library/Fonts) and set up the transforms.
cr.select_font_face("FreeSans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
cr.set_font_size(32)
cr.set_source_rgb(0,0,0)

# Render glyphs '0' through '9' and write out their extents:
x, y = 0, 0
glyphs = list()
for character in CHARACTER_LIST:
    extents = cr.text_extents(character)
    x_bearing, y_bearing, width, height, x_advance, y_advance = extents

    glyph = dict(name=character, x=x, y=y, width=width, height=height,
                 xbearing=x_bearing, ybearing=y_bearing,
                 xadvance=x_advance, yadvance=y_advance)

    glyphs.append(glyph)
    
    cr.save()
    cr.translate(x,-y_bearing)
    cr.text_path(character)
    cr.fill()
    cr.restore()
    x += width + padding

# Saving the surface to a png file
surface.write_to_png("NumeralsTexture.png")

glyphs_template = Template(filename='template.mako')



