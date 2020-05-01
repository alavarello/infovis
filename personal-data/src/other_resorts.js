 // Assign the specification to a local variable vlSpec.
      var vlSpec = {
        "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
        "description": "Vega-Lite version of bar chart from https://observablehq.com/@d3/learn-d3-scales.",
        "width": 400,
        "data": {
          "values": [
          {"name": "Breckenridge", "amount": 8178, "color": "#265a88"},
          {"name": "Keystone", "amount": 10307, "color": "#419641"}, 
          {"name":"Beaver Creek", "amount": 17410, "color": "#eb9316"}
          ]
        },
        "encoding": {
          "x": {"field": "name", "type": "nominal", "title": "Other Mountains"},
          "y": {"field": "amount", "type": "quantitative", "title": "Vertical Meters"},
          "color": {
            "field": "color",
            "type": "nominal",
            "scale": null
          }
        },
        "layer": [{
          "mark": "bar"
        }, {
          "mark": {
            "type": "text",
            "align": "center",
            "baseline": "bottom"
          },
          "encoding": {
            "text": {"field": "amount", "type": "quantitative"},
            "color": {
              "value": "black"
            }
          }
        }]
      };


      // Embed the visualization in the container with id `vis`
      vegaEmbed('#vis', vlSpec);