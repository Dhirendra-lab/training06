# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # ** HTML, Javascript, D3 and SVG **
# MAGIC To view HTML code, such as Javascript, D3, and SVG, use the `displayHTML` method.
# MAGIC
# MAGIC **Note:** 
# MAGIC
# MAGIC - The maximum size for a notebook cell, including contents and output, is 16MB. Make sure that the size of the HTML you pass to the `displayHTML` function does not exceed this value.
# MAGIC
# MAGIC - When linking to external resources, use `https://` instead of `http://`. Otherwise, graphics, images, or Javascript might not render correctly due to mixed content errors.

# COMMAND ----------

# MAGIC %md ## Display HTML code

# COMMAND ----------

displayHTML("<h3>You can view HTML code in notebooks.</h3>")

# COMMAND ----------

# MAGIC %md ## Display **SVG visualizations**

# COMMAND ----------

displayHTML("""<svg width="100" height="100">
   <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
   Sorry, your browser does not support inline SVG.
</svg>""")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Display **D3 visualizations** with **displayHTML**
# MAGIC **Note:** You can program part of the HTML code for D3 visualizations from an RDD.
# MAGIC
# MAGIC Find out more about D3 here: http://d3js.org/.

# COMMAND ----------

# Change these colors to your favorites to change the D3 visualization.
colorsRDD = sc.parallelize([(197,27,125), (222,119,174), (241,182,218), (253,244,239), (247,247,247), (230,245,208), (184,225,134), (127,188,65), (77,146,33)])
colors = colorsRDD.collect()

# COMMAND ----------

htmlCode = """
<!DOCTYPE html>
<meta charset="utf-8">
<style>

path {{
  fill: yellow;
  stroke: #000;
}}

circle {{
  fill: #fff;
  stroke: #000;
  pointer-events: none;
}}

.PiYG .q0-9{{fill:rgb{colorArray[0]}}}
.PiYG .q1-9{{fill:rgb{colorArray[1]}}}
.PiYG .q2-9{{fill:rgb{colorArray[2]}}}
.PiYG .q3-9{{fill:rgb{colorArray[3]}}}
.PiYG .q4-9{{fill:rgb{colorArray[4]}}}
.PiYG .q5-9{{fill:rgb{colorArray[5]}}}
.PiYG .q6-9{{fill:rgb{colorArray[6]}}}
.PiYG .q7-9{{fill:rgb{colorArray[7]}}}
.PiYG .q8-9{{fill:rgb{colorArray[7]}}}

</style>
<body>
<script src="https://d3js.org/d3.v3.min.js"></script>
<script>

width = 960, height = 500;

vertices = d3.range(100).map(function(d) {{
  return [Math.random() * width, Math.random() * height];
}});

svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("class", "PiYG")
    .on("mousemove", function() {{ vertices[0] = d3.mouse(this); redraw(); }});

path = svg.append("g").selectAll("path");

svg.selectAll("circle")
    .data(vertices.slice(1))
  .enter().append("circle")
    .attr("transform", function(d) {{ return "translate(" + d + ")"; }})
    .attr("r", 2);

redraw();

function redraw() {{
  path = path.data(d3.geom.delaunay(vertices).map(function(d) {{ return "M" + d.join("L") + "Z"; }}), String);
  path.exit().remove();
  path.enter().append("path").attr("class", function(d, i) {{ return "q" + (i % 9) + "-9"; }}).attr("d", String);
}}

</script>
 """.format(colorArray = colors)
displayHTML (htmlCode)
