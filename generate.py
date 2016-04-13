from jinja2 import Environment

TEMPLATE = Environment().from_string(
    r"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"

   version="1.1"

   width="{{device_width}}" height="{{device_height}}"
   viewBox="0 0 {{device_width}} {{device_height}}">
  <sodipodi:namedview
     id="base"
     inkscape:cx="{{device_width/2}}"
     inkscape:cy="{{device_height/2}}"
     inkscape:document-units="px"

     showgrid="false"
     units="px"
     showguides="true"
     inkscape:guide-bbox="true">

    {% set origin = (device_width - grid_width) * 0.5 %}
    {% set column = (grid_width / 12.0) %}

    {% for col_idx in range(0, 12) %}
      <sodipodi:guide 
          position="{{origin + col_idx * column}},0"
          orientation="1,0"
          id="column{{col_idx + 1}}"
          inkscape:color="rgb(0,0,255)" />
      <sodipodi:guide 
          position="{{origin + col_idx * column + 15 }},0"
          orientation="1,0"
          id="column{{col_idx + 1}}-leftgutter"
          inkscape:color="rgb(0,0,255)" />
      <sodipodi:guide 
          position="{{origin + (col_idx + 1) * column - 15 }},0"
          orientation="1,0"
          id="column{{col_idx + 1}}-rightgutter"
          inkscape:color="rgb(180,226,223)" />

    {% endfor %}
      <sodipodi:guide 
          position="{{origin + 12 * column}},0"
          orientation="1,0"
          id="column12end"
          inkscape:color="rgb(0,0,255)" />

  </sodipodi:namedview>

  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(0,0)" />
</svg>""")

DEVICES = {
    "xs-iphone-6-portrait":  {"device_width":  375, "device_height":  667, "grid_width":  375},
    "xs-iphone-6-landscape": {"device_width":  667, "device_height":  375, "grid_width":  667},
    "sm-ipad-4-portrait":    {"device_width":  768, "device_height": 1024, "grid_width":  750},
    "md-ipad-4-landscape":   {"device_width": 1024, "device_height":  768, "grid_width":  970},
    "lg-desktop-720p":       {"device_width": 1280, "device_height":  720, "grid_width": 1170},
    "lg-desktop-1080p":      {"device_width": 1920, "device_height": 1080, "grid_width": 1170},
}

for name, dev in DEVICES.items():
    with open("container/%s.svg" % name, 'w') as f:
        f.write(TEMPLATE.render(dev))

    with open("fluid/%s.svg" % name, 'w') as f:
        dev = dict(dev)
        dev["grid_width"] = dev["grid_width"]
        f.write(TEMPLATE.render(dev))
