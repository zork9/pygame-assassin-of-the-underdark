;; Copyright (C) http://www.toomuchcookies.net 2009
;; Copyright (C) Johan Ceuppens 2014
;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 2 of the License, or
;; (at your option) any later version.

;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.

;; You should have received a copy of the GNU General Public License
;; along with this program.  If not, see <http://www.gnu.org/licenses/>.

;; display textbox, print text in textbox to bmp file in your home directory
;; (Linux $HOME)


(define (script-fu-text-to-bmp)
  	(let* ((image (car (gimp-image-new 100 100 RGB)))
	       	(layer (car (gimp-layer-new image 100 100
					    	RGB-IMAGE "text" 100 NORMAL-MODE)0))
			(gimp-drawable-fill layer BG-IMAGE-FILL)
			(gimp-image-add-layer image layer 0)
			(gimp-display-new image)
			(outfile (string-append "~/" "text-to-bmp.bmp"))
			(newimage (car (gimp-edit-paste-as-new)))
			(thelayer (car (gimp-image-flatten newimg)))
			(file-bmp-save RUN-NONINTERACTIVE image newimage thelayer outfile outfile)
			(gimp-image-delete newimage)	
			)
	  ))



(script-fu-register
     "script-fu-text-to-bmp"                        ;func name
     "Text Box"                                  ;menu label
     "Creates a simple text box, sized to fit\
      around the user's choice of text,\
      font, font size, and color."              ;description
     "Johan Ceuppens, Michael Terry"
;author
    "copyright 2014, Michael Terry, Johan Ceuppens;\
          2010, the GIMP Documentation Team"        ;copyright notice
    "April 6, 2014"                          ;date created
    ""                     ;image type that the script works on
    SF-STRING      "Text"          "Text Box"   ;a string variable
    SF-FONT        "Font"          "Charter"    ;a font variable
    SF-ADJUSTMENT  "Font size"     '(50 1 1000 1 10 0 1)
                                             ;a spin-button
							        SF-COLOR
    "Color"         '(0 0 0)     ;color variable
)
	  (script-fu-menu-register "script-fu-text-box"
"<Image>/File/Create/Text")
