window.onload = function() {

  var world_pop = "world_pop.json"
  var data = "world.json"
  var requests = [d3.json(world_pop), d3.json(data)];

  Promise.all(requests).then(function(response) {
      var world_pop = response[0];
      var data = response[1];



      var format = d3.format(",");

      // Set tooltips
      var tip = d3.tip()
                  .attr('class', 'd3-tip')
                  .offset([-10, 0])
                  .html(function(d) {
                    return "<strong>Country: </strong><span class='details'>" + d.properties.name + "<br></span>" + "<strong>Population 2017: </strong><span class='details'>" + format(d.Y2017) +"</span>";
                  })

      var margin = {top: 0, right: 0, bottom: 0, left: 0},
                  width = 960 - margin.left - margin.right,
                  height = 700 - margin.top - margin.bottom;

      var color = d3.scaleThreshold()
          .domain([10000,200000,500000,1000000,5000000,10000000,50000000,100000000,500000000, 1000000000000])
          .range(["rgb(247,251,255)", "rgb(222,235,247)", "rgb(198,219,239)", "rgb(158,202,225)", "rgb(107,174,214)", "rgb(66,146,198)","rgb(33,113,181)","rgb(8,81,156)","rgb(8,48,107)","rgb(3,19,43)"]);

      var path = d3.geoPath();

      var svg = d3.select("#map")
                  .append("svg")
                  .attr("width", width)
                  .attr("height", height)
                  .append('g')
                  .attr('class', 'map');

      var projection = d3.geoMercator()
                         .scale(130)
                        .translate( [width / 2, height / 1.5]);

      var path = d3.geoPath().projection(projection);

      svg.call(tip);
      ready(data, world_pop);

      function ready( data, world_pop) {
        var IndexbyCountry = {};
        world_pop.forEach(function(d) { IndexbyCountry[d.id] = +d.Y1960; });
        data.features.forEach(function(d) { d.Y1960 = IndexbyCountry[d.id] });

        data.features.forEach(function(d) { d.Y1970 = IndexbyCountry[d.id] });
        world_pop.forEach(function(d) { IndexbyCountry[d.id] = +d.Y1970; });

        data.features.forEach(function(d) { d.Y1980 = IndexbyCountry[d.id] });
        world_pop.forEach(function(d) { IndexbyCountry[d.id] = +d.Y1980; });

        data.features.forEach(function(d) { d.Y1990 = IndexbyCountry[d.id] });
        world_pop.forEach(function(d) { IndexbyCountry[d.id] = +d.Y1990; });

        data.features.forEach(function(d) { d.Y2000 = IndexbyCountry[d.id] });
        world_pop.forEach(function(d) { IndexbyCountry[d.id] = +d.Y2000; });

        data.features.forEach(function(d) { d.Y2010 = IndexbyCountry[d.id] });
        world_pop.forEach(function(d) { IndexbyCountry[d.id] = +d.Y2010; });


        data.features.forEach(function(d) { d.Y2017 = IndexbyCountry[d.id] });

        world_pop.forEach(function(d) { IndexbyCountry[d.id] = +d.Y2017; });
        data.features.forEach(function(d) { d.Y2017 = IndexbyCountry[d.id] });
        svg.append("g")
            .attr("class", "countries")
          .selectAll("path")
            .data(data.features)
          .enter().append("path")
            .attr("d", path)
            .style("fill", function(d) { return color(IndexbyCountry[d.id]); })
            .style('stroke', 'white')
            .style('stroke-width', 1.5)
            .style("opacity",0.8)
            // tooltips
              .style("stroke","white")
              .style('stroke-width', 0.3)
              .on('click', function(d,i){
                d3.selectAll("#chart > *").remove()

                var data = [];
                data.push(d.Y1960, d.Y1970, d.Y1980, d.Y1990, d.Y2000, d.Y2010, d.Y2017);
                if (d.Y1960 === undefined){
                  var empty = d3.select("#chart").append("svg")
                                .attr("width", 200 - margin.right - margin.left)
                                .attr('height', 100 - margin.top - margin.bottom);
                  empty.append('text')
                    .attr('x', 60)
                    .attr('y', 80)
                    .style('font-size', '20px')
                    .text('Kan niet');
                  empty.append('text')
                      .attr('x', 70)
                      .attr('y', 85)
                      .style("font-size", '16px')
                      .text(d.properties.name)
                }
                else {linechart(data, d.properties.name)};
              })
              .on('mouseover',function(d){
                tip.show(d);

                d3.select(this)
                  .style("opacity", 1)
                  .style("stroke","white")
                  .style("stroke-width",3);
              })
              .on('mouseout', function(d){
                tip.hide(d);

                d3.select(this)
                  .style("opacity", 0.8)
                  .style("stroke","white")
                  .style("stroke-width",0.3);
              });

        svg.append("path")
            .datum(topojson.mesh(data.features, function(a, b) { return a.name !== b.name; }))
             // .datum(topojson.mesh(data.features, function(a, b) { return a !== b; }))
            .attr("class", "names")
            .attr("d", path);


          function linechart(values, country){
            var margin = {
              top: 30,
              right: 30,
              bottom: 40,
              left: 80
            }
            var height = 400 - margin.top - margin.bottom;
            var width = 400 - margin.right - margin.left;
            // specify duration and delay of the animation
            var durationAnimation = 700
            var delayAnimation = 30

            // create interaction with some styles
            var tooltip = d3.select("body").append("div")
              .style('position','absolute')
              .style('background','#f4f4f4')
              .style('padding','5 15px')
              .style('border','1px #333 solid')
              .style('border-radius','5px')
              .style('opacity','0')

            // specify scales
            var yScale = d3.scaleLinear()
              .domain([0, d3.max(values)])
              .range([0, height]);

            var xScale =  d3.scaleBand()
              .domain(d3.range(0, values.length))
              .range([0, width])

            // create nice dynamic colorspectrum
            var colors = d3.scaleLinear()
              .domain([0,values.length])
              .range(["rgb(158,202,225)","rgb(33,113,181)","rgb(3,19,43)"]);

            // initiate variable to allow interaction


            var myChart = d3.select('#chart').append('svg')
              .attr('width', width + margin.right + margin.left)
              .attr('height', height + margin.top + margin.bottom)
              .append('g')
              .attr("id","#chart")
              .attr('transform', 'translate('+margin.left+','+margin.top+')')
              .style('background', '#f4f4f4')

              // make bars
              .selectAll('rect')
                .data(values)
                .enter().append('rect')
                .style('fill', function(d, i){
                  return colors(i);
                })

                // specify ranges of bars
                .attr('width', xScale.bandwidth())
                .attr('height', 0)
                .attr('x', function(d, i){
                  return xScale(i);
                })
                .attr('y', height)

            // create some nice interaction when moving over bars

            .on('mouseover', function(d){
              tooltip.transition()
                .style('opacity', 1)
              tooltip.html(d)
                .text("Population:" + d)
                .style('left', (d3.event.pageX)+'px')
                .style('top', (d3.event.pageY+'px'))
              d3.select(this).style('opacity', 0.5)
            })
            .on('mouseout', function(d){
              tooltip.transition()
                .style('opacity', 0)
              d3.select(this).style('opacity', 1)
            })

        // create animation
        myChart.transition()
          .attr('height', function(d){
            return yScale(d);
          })
          .attr('y', function(d){
            return height - yScale(d)
          })
          .duration(durationAnimation)
          .delay(function(d, i){
            return i * delayAnimation
          })
          .ease(d3.easeElastic)

          myChart.append('text')
              .attr('x', 0)
              .attr('y', 50)
              .style("font-size", '106px')
              .text('oasjdlkjsalkdjsalkjdlksa')

          // adjust scales of axes
          var vScale = d3.scaleLinear()
            .domain([0, d3.max(values)])
            .range([height, 0]);

          var hScale =  d3.scaleBand()
            .domain(d3.range(1960, 2020))
            .range([0, width])

          var vAxis = d3.axisLeft()
            .scale(vScale)
            .ticks(5)
            .tickPadding(5)

          // apply styles to axes
          var vGuide = d3.select("#chart").select('svg')
            .append('g')
              vAxis(vGuide)
              vGuide.attr('transform', 'translate('+margin.left+','+margin.top+')')
              vGuide.selectAll('path')
                .style('fill', 'none')
                .style('stroke', '#000')
              vGuide.selectAll('line')
                .style('stroke', '#000')

          d3.select("#chart").selectAll(".xaxis text")  // select all the text elements for the xaxis
          .attr("transform", function(d) {
             return "translate(" + this.getBBox().height*-2 + "," + this.getBBox().height + ")rotate(-45)";
           })
           // now add titles to the axes
           d3.select("#chart").select('svg')
           .append("text")
             .attr("text-anchor", "centre")
             .attr('x', 120)
             .attr("transform", "translate("+ (100/2) +","+(height/2)+")rotate(-90)")  // text is drawn off the screen top left, move down and out and rotate
             .style('font-size', '15px')
             .text("Value");

           d3.select("#chart").select('svg')
           .append("text")
             .attr('x', 200)  // this makes it easy to centre the text as the transform is applied to the anchor
             .attr('y', 400)  // centre below axis
             .style('font-size', '15px')
             .text("Year");

           d3.select("#chart").select('svg')
             .append("text")
               .attr('x', 200)  // this makes it easy to centre the text as the transform is applied to the anchor
               .attr('y', 20)  // centre below axis
               .style('font-size', '20px')
               .text(country);

          var hAxis = d3.axisBottom()
            .scale(hScale)
            .tickValues(hScale.domain().filter(function(d, i){
              return !(i % 10);
            }));

          var hGuide = d3.select("#chart").select('svg')
            .append('g')
              hAxis(hGuide)
              hGuide.attr('transform', 'translate('+margin.left+','+(height + margin.top)+')')
              hGuide.selectAll('path')
                .style('fill', 'none')
                .style('stroke', '#000')
              hGuide.selectAll('line')
                .style('stroke', '#000')


          }
        };




    }).catch(function(e){
        throw(e);
  });
};
