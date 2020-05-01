

  var all_seasons = {'Monday': 13, 'Tuesday': 15, 'Wednesday':15, 'Thursday':15, 'Friday':15, 'Saturday': 12, 'Sunday': 15}
  var season_19_20 = {'Monday': 14, 'Tuesday': 16, 'Wednesday':11, 'Thursday':20, 'Friday':14, 'Saturday': 11, 'Sunday': 14}
  var season_18_19 = {'Monday': 15, 'Tuesday': 12, 'Wednesday':18, 'Thursday':15, 'Friday':6, 'Saturday': 14, 'Sunday': 20}
  var season_17_18 = {'Monday': 9, 'Tuesday': 18, 'Wednesday':17, 'Thursday':6, 'Friday':28, 'Saturday': 12, 'Sunday': 10}


  function buttonClick(data){
    delete_and_create(data);
    delete_and_create(data);
  }

// A function that create / update the plot for a given variable:
function delete_and_create(data) {
  d3.select("svg").remove();

  // set the dimensions and margins of the graph
  var width = 450
  height = 450
  margin = 40

// The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
var radius = Math.min(width, height) / 2 - margin

// append the svg object to the div called 'my_dataviz'
var svg = d3.select("#my_dataviz")
.append("svg")
.attr("width", width)
.attr("height", height)
.append("g")
.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

// set the color scale
//var color = d3.scaleOrdinal()
//.domain(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
//.range(d3.schemeDark2);
 var color  = {'Monday': '#1b9e77', 'Tuesday': '#d95f02', 'Wednesday':'#7570b3', 
 'Thursday':'#e7298a', 'Friday':'#66a61e', 'Saturday':'#e6ab02', 'Sunday':'#a6761d'}

  // Compute the position of each group on the pie:
  var pie = d3.pie()
  .value(function(d) {return d.value; })
    .sort(function(a, b) { console.log(a) ; return d3.ascending(a.key, b.key);} ) // This make sure that group order remains the same in the pie chart
    var data_ready = pie(d3.entries(data))

  // map to data
  var u = svg.selectAll("path")
  .data(data_ready)
// shape helper to build arcs:
var arcGenerator = d3.arc()
.innerRadius(0)
.outerRadius(radius)
  // Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
  u
  .enter()
  .append('path')
  .merge(u)
  .transition()
  .duration(1000)
  .attr('d', arcGenerator)
  .attr('fill', function(d){ return(color[d.data.key]) })
  .attr("stroke", "white")
  .style("stroke-width", "2px")
  .style("opacity", 1)


  // Now add the annotation. Use the centroid method to get the best coordinates
  u
  .enter()
  .append('text')
  .transition()
  .duration(1000)
  .text(function(d){ return  d.value.toString() + "%"})
  .attr("transform", function(d) { return "translate(" + arcGenerator.centroid(d) + ")";  })
  .style("text-anchor", "middle")
  .style("font-size", 13)

  // remove the group that is not present anymore
  u
  .exit()
  .remove()

}

// Initialize the plot with the first dataset
delete_and_create(all_seasons)


