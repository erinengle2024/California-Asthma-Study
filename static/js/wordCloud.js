    // Fetch JSON data from Flask endpoint
    fetch('/data')
    .then(response => response.json())
    .then(data => {
        const dropdown = document.getElementById('data-category');

        // Function to update word cloud based on selected category
        function updateWordCloud(selectedCategory) {
            // Remove duplicate counties
            const uniqueCounties = {};
            data.survey_2018.forEach(item => {
                const county = item["California County"].trim();
                if (!(county in uniqueCounties)) {
                    uniqueCounties[county] = item[selectedCategory] * 0.5; // Adjust multiplier as needed
                }
            });

            // Convert data to word list
            const myWords = Object.entries(uniqueCounties).map(([text, size]) => ({ text, size }));

            // Remove existing word cloud if any
            d3.select("#word-cloud").selectAll("*").remove();

            // Constructs a new cloud layout instance
            var layout = d3.layout.cloud()
                .size([600, 500]) // Set the size of the word cloud container
                .words(myWords)
                .padding(5) // Adjust padding as needed
                .rotate(function() { return ~~(Math.random() * 2) * 90; }) // Randomly rotate words
                .fontSize(d => d.size) // Set font size based on size property
                .on("end", draw);

            layout.start();

            // This function takes the output of 'layout' above and draws the words
            function draw(words) {
                d3.select("#word-cloud").append("svg")
                    .attr("width", 600)
                    .attr("height", 500)
                    .append("g")
                    .attr("transform", "translate(300,250)") // Center the word cloud
                    .selectAll("text")
                    .data(words)
                    .enter().append("text")
                    .style("font-size", function(d) { return d.size + "px"; })
                    .style("fill", "#69b3a2")
                    .attr("text-anchor", "middle")
                    .style("font-family", "Impact")
                    .attr("transform", function(d) {
                        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                    })
                    .text(function(d) { return d.text; });
            }
        }

        // Initial word cloud display
        updateWordCloud(dropdown.value);

        // Event listener for dropdown change
        dropdown.addEventListener('change', function() {
            updateWordCloud(this.value);
        });
    })
    .catch(error => console.error('Error fetching JSON data:', error));