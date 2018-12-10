window.onload = function() {
    var bubble_map = new Datamap({
        element: document.getElementById('canada'),
        scope: 'canada',
        geographyConfig: {
            popupOnHover: true,
            highlightOnHover: true,
            borderColor: '#444',
            borderWidth: 0.5,
            dataUrl: 'https://rawgit.com/Anujarya300/bubble_maps/master/data/geography-data/canada.topo.json'
            //dataJson: topoJsonData
        },
        fills: {
            'MAJOR': '#306596',
            'MEDIUM': '#0fa0fa',
            'MINOR': '#bada55',
            defaultFill: '#dddddd'
        },
        data: {
            'JH': { fillKey: 'MINOR' },
            'MH': { fillKey: 'MINOR' }
        },
        setProjection: function (element) {
              var projection = d3.geo.mercator()
            .center([-106.3468, 68.1304]) // always in [East Latitude, North Longitude]
            .scale(250)
            .translate([element.offsetWidth / 2, element.offsetHeight / 2]);
            var path = d3.geo.path().projection(projection);
            return { path: path, projection: projection };
        }
    });
    let bubbles = [
        {
            centered: "MB",
            fillKey: "MAJOR",
            radius: 20,
            state: "Manitoba"
        },
        {
            centered: "AB",
            fillKey: "MAJOR",
            radius: 22,
            state: "Alberta"
        },
        {
            centered: "NT",
            fillKey: "MAJOR",
            radius: 40,
            state: "Northwest Territories"
        },
        {
            centered: "NU",
            fillKey: "MEDIUM",
            radius: 60,
            state: "Nunavut"
        },
        {
            centered: "BC   ",
            fillKey: "MEDIUM",
            radius: 15,
            state: "British Columbia"
        },
        {
            centered: "QC",
            fillKey: "MINOR",
            radius: 8,
            state: "Québec"
        },
        {
            centered: "NB",
            fillKey: "MINOR",
            radius: 1,
            state: "New Brunswick"
        },
        {
            centered: "YT",
            fillKey: "MINOR",
            radius: 25,
            state: "Yukon"
        },
        {
            centered: "ON",
            fillKey: "MINOR",
            radius: 25,
            state: "Ontario"
        },
        {
            centered: "NF",
            fillKey: "MINOR",
            radius: 25,
            state: "Newfoundland and Labrador"
        },
        {
            centered: "SK",
            fillKey: "MINOR",
            radius: 25,
            state: "Saskatchewan"
        },
        {
            centered: "NS",
            fillKey: "MINOR",
            radius: 10,
            state: "Nova Skotia"
        },
        {
            centered: "PE",
            fillKey: "MINOR",
            radius: 1,
            state: "Prince Edward Island"
        }
    ]
    // // ISO ID code for city or <state></state>
    setTimeout(() => { // only start drawing bubbles on the map when map has rendered completely.
        bubble_map.bubbles(bubbles, {
            popupTemplate: function (geo, data) {
                return `<div class="hoverinfo">city: ${data.state}, Slums: ${data.radius}%</div>`;
            }
        });
    }, 1000);
};