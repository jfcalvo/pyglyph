#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import cairo
from optparse import OptionParser
from StringIO import StringIO
from mako.template import Template


class GlyphCreator(object):

    # Default Values
    font_size = 50
    font_name = "Chalkboard"
    font_color = (0, 0, 0) # R, G, B
    padding = (2, 2) # X, Y
    texture_size = (512, 512) # W, H
    texture_filename = "fonts.png"
    info_filename = "fonts.plist"
    template_filename = "template.mako"    
    character_list = u'''AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZaábcdeéfghiíjklmnñoópqrstuúvwxyz1234567890"!'?.,;:()[]{}<>|/@\^$-%+=#_&~*'''
            
    def __create_cairo_surface(self):
        return cairo.ImageSurface(cairo.FORMAT_ARGB32, *self.texture_size)
        
    def __create_cairo_context(self, surface):
        cairo_context = cairo.Context(surface)
        cairo_context.select_font_face(self.font_name, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cairo_context.set_font_size(self.font_size)
        cairo_context.set_source_rgb(self.font_color[0], self.font_color[1], self.font_color[2])
        return cairo_context
                                                   
    def __save_surface(self, surface):
        # Saving the surface to a png file
        surface.write_to_png(self.texture_filename)
        
    def __save_info(self, font_metadata, glyphs):
        template = Template(filename=self.template_filename, output_encoding='utf-8')
        
        info_file = open(self.info_filename, 'w')
        info_file.write(template.render(metadata=font_metadata, characters=glyphs))
        info_file.close()
    
    def run(self):
        surface = self.__create_cairo_surface()      
        cr = self.__create_cairo_context(surface)
      
        # Creating Metadata about the font to save in the template
        font_metadata = dict(fontname=self.font_name, fontsize=self.font_size, width=self.texture_size[0], height=self.texture_size[1], padding=self.padding[0])

        glyphs = list()
        max_height = 0
        x, y = self.padding
        x_padding, y_padding = self.padding
        texture_width, texture_height = self.texture_size
        for character in self.character_list:

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
        self.__save_info(font_metadata, glyphs)


def main():
    glyph_creator = GlyphCreator()
         
    usage = 'usage: %prog [options] arg'
    parser = OptionParser(usage)
    parser.add_option('-s', '--fontsize', type='int', dest='font_size')
    parser.add_option('-f', '--font', type='string', dest='font_name')
    parser.add_option('-c', '--color', type='string', dest='font_color')
    parser.add_option('-p', '--padding', type='int', dest='padding')
    parser.add_option('-z', '--texturesize', type='string', dest='texture_size')
    parser.add_option('-o', '--output', type='string', dest='output_filename')
    parser.add_option('--template', type='string', dest='template_filename')
    parser.add_option('--characters', type='string', dest='character_list')

    (options, args) = parser.parse_args()
    
    # Saving Options
    if options.font_size: glyph_creator.font_size = options.font_size
    if options.font_name: glyph_creator.font_name = options.font_name
    if options.font_color: glyph_creator.font_color = tuple([int(s) for s in options.font_color.split(',')]) # R,G,B
    if options.padding: glyph_creator.padding = (options.padding, options.padding)
    if options.texture_size: glyph_creator.texture_size = tuple([int(s) for s in options.texture_size.split('x')]) # WxH
    if options.output_filename: glyph_creator.texture_filename = options.output_filename + '.png'
    if options.output_filename: glyph_creator.info_filename = options.output_filename + '.plist'
    if options.template_filename: glyph_creator.template_filename = options.template_filename
    if options.character_list: glyph_creator.character_list = options.character_list

    glyph_creator.run()

    
if __name__ == '__main__':
    main()
