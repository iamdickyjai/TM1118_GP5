function processData(dataset) {
    var result = []
    dataset = JSON.parse(dataset);
    dataset.forEach(item => result.push(item.fields));
    return result;
}

$.ajax({
    url: '/dashboard/temp_data',
    dataType: 'json',
    success: function(data) {
        new Flexmonster({
            container: "#pivot-container-temp",
            componentFolder: "https://cdn.flexmonster.com/",
            toolbar: true,
            report: {
                dataSource: {
                    type: "json",
                    data: processData(data),
                    
                    mapping: {
                        "node_id": { "caption": "ID" },
                        "loc": { "caption": "Location" },
                        "temp": { "caption": "Temperature", "type": "number" },
                        "date_created": { "caption": "Created Date", "type": "datetime", interval: "1m" }
                    },
                },
                slice: {
                    rows: [
                        { uniqueName : "date_created"},
                    ],
                    columns: [
                        { uniqueName : "loc"},
                        { uniqueName : "[measures]", label : "Temperature" },
                    ],
                    measures: [
                        { 
                            uniqueName : "temp", 
                            format : "degree",
                            aggregation : "average",
                        },
                    ]
                },
                formats: [
                    {
                        name: "degree",
                        decimalPlaces: 1,
                    }
                ],
                options: {
                    dateTimePattern: "dd/MM/yy HH:mm",
                    showAggregationLabels: false ,
                    viewType: "charts",
                    chart: {
                        type: "line",
                    },
                },   
            },
        });
    }
});

$.ajax({
    url: '/dashboard/temp_data',
    dataType: 'json',
    success: function(data) {
        new Flexmonster({
            container: "#pivot-container-hum",
            componentFolder: "https://cdn.flexmonster.com/",
            //toolbar: true,
            report: {
                dataSource: {
                    type: "json",
                    data: processData(data),
                    
                    mapping: {
                        "node_id": { "caption": "ID" },
                        "loc": { "caption": "Location" },
                        "hum": { "caption": "Humidity", "type": "number" },
                        "date_created": { "caption": "Created Date", "type": "datetime", interval: "1m" }
                    },
                },
                slice: {
                    rows: [
                        { uniqueName : "date_created"},
                    ],
                    columns: [
                        { uniqueName : "loc"},
                        { uniqueName : "[measures]", label : "Humidity" },
                    ],
                    measures: [
                        { 
                            uniqueName : "hum", 
                            aggregation : "average",
                            format : "degree",
                        },
                    ]
                },
                formats: [
                    {
                        name: "degree",
                        decimalPlaces: 1,
                    }
                ],
                options: {
                    dateTimePattern: "dd/MM/yy HH:mm",
                    showAggregationLabels: false ,
                    viewType: "charts",
                    chart: {
                        type: "line",
                    },
                },   
            },
        });
    }
});

$.ajax({
    url: '/dashboard/temp_data',
    dataType: 'json',
    success: function(data) {
        new Flexmonster({
            container: "#pivot-container-light",
            componentFolder: "https://cdn.flexmonster.com/",
            //toolbar: true,
            report: {
                dataSource: {
                    type: "json",
                    data: processData(data),
                    
                    mapping: {
                        "node_id": { "caption": "ID" },
                        "loc": { "caption": "Location" },
                        "light": { "caption": "Light Intensity", "type": "number" },
                        "date_created": { "caption": "Created Date", "type": "datetime", interval: "1m" }
                    },
                },
                slice: {
                    rows: [
                        { uniqueName : "date_created"},
                    ],
                    columns: [
                        { uniqueName : "loc"},
                        { uniqueName : "[measures]", label : "Light Intensity" },
                    ],
                    measures: [
                        { 
                            uniqueName : "light", 
                            aggregation : "average",
                            format : "degree",
                        },
                    ]
                },
                formats: [
                    {
                        name: "degree",
                        decimalPlaces: 1,
                    }
                ],
                options: {
                    dateTimePattern: "dd/MM/yy HH:mm",
                    showAggregationLabels: false ,
                    viewType: "charts",
                    chart: {
                        type: "line",
                    },
                },   
            },
        });
    }
});

$.ajax({
    url: '/dashboard/temp_data',
    dataType: 'json',
    success: function(data) {
        new Flexmonster({
            container: "#pivot-container-snd",
            componentFolder: "https://cdn.flexmonster.com/",
            //toolbar: true,
            report: {
                dataSource: {
                    type: "json",
                    data: processData(data),
                    
                    mapping: {
                        "node_id": { "caption": "ID" },
                        "loc": { "caption": "Location" },
                        "snd": { "caption": "Sound Level(dB)", "type": "number" },
                        "date_created": { "caption": "Created Date", "type": "datetime", interval: "1m" }
                    },
                },
                slice: {
                    rows: [
                        { uniqueName : "date_created"},
                    ],
                    columns: [
                        { uniqueName : "loc"},
                        { uniqueName : "[measures]", label : "Sound Level(dB)" },
                    ],
                    measures: [
                        { 
                            uniqueName : "snd", 
                            aggregation : "average",
                            format : "degree",
                        },
                    ]
                },
                formats: [
                    {
                        name: "degree",
                        decimalPlaces: 1,
                    }
                ],
                options: {
                    dateTimePattern: "dd/MM/yy HH:mm",
                    showAggregationLabels: false ,
                    viewType: "charts",
                    chart: {
                        type: "line",
                    },
                },   
            },
        });
    }
});

function getFeed() {
    $.ajax({
        url: '/dashboard/temp_data',
        dataType: 'json',
        success: function(data) {
            flexmonster.updateData({
                data: processData(data)
            });
        },
        complete:function(data) {
            setTimeout(getFeed, 5000);
        }
    });
}
$(document).ready(function() {
    setTimeout(getFeed, 5000); // 5 seconds
});