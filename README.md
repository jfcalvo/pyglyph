# Pyglyph

Pyglyph is a **font texture generator**, useful to create textures with a character list using a font available in the system. Pyglyph generates a png file with the texture and a file with information about the characters in the texture, the info file can be customized with templates (using Mako as template engine), by now we generate a plist XML file useful to load the texture with Cocoa.

Pyglyph is based in the code example described at [iPhone3D Programming](http://oreilly.com/catalog/9780596804831) book by Philip Rideout. I recommend to get a copy of this incredible book.

## Dependencies:

### [Python 2.6.1](http://www.python.org/)
Pyglyph has been tested successfully with Python version 2.6.1.

### [Mako](http://www.makotemplates.org/)
Pyglyph uses the awesome Make templates module.

Install
<pre><code>sudo easy_install mako</code></pre>
Test
<pre><code>python -c "import mako"</code></pre>

### [Pycairo](http://cairographics.org/pycairo)
Pyglyph uses Pycairo to render the fonts.

Install
<pre><code>sudo easy_install pycairo</code></pre>
Test
<pre><code>python -c "import cairo"</code></pre>


## How to run it

Yo only need to run the script
<pre><code>./pyglyph.py</code></pre>
To get help
<pre><code>./pyglyph.py --help</code></pre>

## Options

Options:
> -s FONT_SIZE, --fontsize=FONT_SIZE
> -f FONT_NAME, --font=FONT_NAME
> -c FONT_COLOR, --color=FONT_COLOR
> -p PADDING, --padding=PADDING
> -z TEXTURE_SIZE, --texturesize=TEXTURE_SIZE
> -o OUTPUT_FILENAME, --output=OUTPUT_FILENAME
> --template=TEMPLATE_FILENAME
> --characters=CHARACTER_LIST
	
## Examples

Create a texture of 512x512 pixels using font Trebuchet with size 50, color red, and the default character list. Output the content to example.png and example.plist:
<pre><code>./pyglyph.py --texturesize=512x512 --fontsize=50 --font=Trebuchet --color=255,0,0 --output=example</code></pre>

By default you can run Pyglyph using all the default values, this will create a 512x512 texture with font Chalkboard of size 50, and black color, output name fonts.png and fonts.plist:
<pre><code>./pyglyph.py</code></pre>
