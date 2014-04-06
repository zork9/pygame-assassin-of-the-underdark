#!/usr/bin/env python

#### From http://gimbook.com/scripting # Copyright is theirs
#### from Hello World in GIMP Python

from gimpfu import *

def write_text_to_image(initstr, font, size, color) :
    # First do a quick sanity check on the font
    if font == 'Comic Sans MS' :
        initstr = "Comic Sans? Are you sure?"

    # Make a new image. Size 10x10 for now -- we'll resize later.
    img = gimp.Image(1, 1, RGB)

    # Save the current foreground color:
    pdb.gimp_context_push()

    # Set the text color
    gimp.set_foreground(color)

    # Create a new text layer (-1 for the layer means create a new layer)
    layer = pdb.gimp_text_fontname(img, None, 0, 0, initstr, 10,
                                   True, size, PIXELS, font)

    # Resize the image to the size of the layer
    img.resize(layer.width, layer.height, 0, 0)

    # Background layer.
    # Can't add this first because we don't know the size of the text layer.
    background = gimp.Layer(img, "Background", layer.width, layer.height,
                            RGB_IMAGE, 100, NORMAL_MODE)
    background.fill(BACKGROUND_FILL)
    img.add_layer(background, 1)

    # Create a new image window
    gimp.Display(img)
    # Show the new image window
    gimp.displays_flush()

    # Restore the old foreground color:
    pdb.gimp_context_pop()

register(
    "python_fu_write_text_to_image",
    "text to image",
    "Create a new image with your text string",
    "Akkana Peck, Johan Ceuppens",
    "Akkana Peck, Johan Ceuppens",
    "2010, 2014",
    "Write text to BMP (Py)...",
    "",      # Create a new image, don't work on an existing one
    [
        (PF_STRING, "string", "Text string", 'This is written to file'),
        (PF_FONT, "font", "Font face", "Sans"),
        (PF_SPINNER, "size", "Font size", 50, (1, 3000, 1)),
        (PF_COLOR, "color", "Text color", (1.0, 0.0, 0.0))
    ],
    [],
    write_text_to_image, menu="<Image>/File/Create")

main()
