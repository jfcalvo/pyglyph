#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import cairo
from StringIO import StringIO
from mako.template import Template


class GlyphCreator(object):

    # Default Values
    __FONT_SIZE = 50
    __FONT_NAME = "Chalkboard"
    __FONT_COLOR = (0, 0, 0) # R, G, B
    __PADDING = (2, 2) # X, Y
    __TEXTURE_SIZE = (512, 512) # W, H
    __TEXTURE_FILENAME = "fonts.png"
    __INFO_FILENAME = "fonts.plist"
    __TEMPLATE_FILENAME = "template.mako"    
    __CHARACTER_LIST = u'''ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890"!'?.,;:()[]{}<>|/@\^$-%+=#_&~*'''
    
    def __init__(self):
        self._font_size = self.__FONT_SIZE
        self._font_name = self.__FONT_NAME
        self._font_color = self.__FONT_COLOR
        self._padding = self.__PADDING
        self._texture_size = self.__TEXTURE_SIZE
        self._texture_filename = self.__TEXTURE_FILENAME
        self._info_filename = self.__INFO_FILENAME
        self._template_filename = self.__TEMPLATE_FILENAME
        self._character_list = self.__CHARACTER_LIST
        
    def __create_cairo_surface(self):
        return cairo.ImageSurface(cairo.FORMAT_ARGB32, *self._texture_size)
        
    def __create_cairo_context(self, surface):
        cairo_context = cairo.Context(surface)
        cairo_context.select_font_face(self._font_name, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cairo_context.set_font_size(self._font_size)
        cairo_context.set_source_rgb(self._font_color[0], self._font_color[1], self._font_color[2])
        return cairo_context
                                                   
    def __save_surface(self, surface):
        # Saving the surface to a png file
        surface.write_to_png(self._texture_filename)
        
    def __save_info(self, glyphs):
        template = Template(filename=self._template_filename, output_encoding='utf-8')
        
        info_file = open(self._info_filename, 'w')
        info_file.write(template.render(characters=glyphs))
        info_file.close()
    
    def run(self):
        surface = self.__create_cairo_surface()      
        cr = self.__create_cairo_context(surface)
      
        glyphs = list()
        max_height = 0
        x, y = self._padding
        x_padding, y_padding = self._padding
        texture_width, texture_height = self._texture_size
        for character in self._character_list:

            extents = cr.text_extents(character)
            x_bearing, y_bearing, width, height, x_advance, y_advance = extents

            # Saving maximum height sized in pixels for all characters
            if height > max_height:
                max_height = height
  
            # Calculating if we need to add a new line of characters
            if (x + x_advance + x_padding) > (texture_width - 1):
                x = x_padding
                y += max_height + y_padding
  
            # Rendering character
            cr.save()
            cr.translate(x-x_bearing, y-y_bearing)
            cr.text_path(character)
            cr.fill()
            cr.restore()

            # Creating a glyph dictionary to use in the template
            glyph = dict(name=character, x=x, y=y, width=width, height=height, xbearing=x_bearing, ybearing=y_bearing, xadvance=x_advance, yadvance=y_advance)
            glyphs.append(glyph)

            # Next character x position
            x += x_advance + x_padding
                 
        # Saving texture to disk
        self.__save_surface(surface)
        
        # Render template to info plist file
        self.__save_info(glyphs)


def main():
    glyph_creator = GlyphCreator()
    glyph_creator.run()

    
if __name__ == '__main__':
    main()