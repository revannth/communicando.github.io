/*d3.js*/
	var canvas = d3.selectAll("#banner,#menu_test")
        .append("svg")
        .attr("width", 300)
        .attr("height", 50);

function circleTransition() { 

    var timeCircle = canvas.append("circle")
        .attr("fill", "#FFECB3")
        .attr("r", 10);
    repeat();
    
    function repeat() {
      timeCircle
        .attr('cx', 11)      // position the circle at 40 on the x axis
        .attr('cy', 25)     // position the circle at 250 on the y axis
        .transition()        // apply a transition
        .duration(2000)      // apply it over 2000 milliseconds
        .attr('cx', 250)
        .attr('fill',"#FFEBEE")     // move the circle to 920 on the x axis
        .transition()        // apply a transition
        .duration(2000)      // apply it over 2000 milliseconds
        .attr('cx', 11)
        .attr('fill',"#FFECB3")      // return the circle to 40 on the x axis
        .on("end", repeat);  // when the transition finishes start again
    };

};

circleTransition();