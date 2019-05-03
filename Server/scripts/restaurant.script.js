$(document).ready(function() {
    let now = new Date();
    let day = ("0" + now.getDate()).slice(-2);
    let month = ("0" + (now.getMonth() + 1)).slice(-2);
    let today = now.getFullYear() + "-" + month + "-" + day;
    $("#date-picker").val(today);
    update_page(today);
});

function update_page(date) {
    let restaurant = window.location.href.substr(window.location.href.indexOf('=') + 1)
    $.ajax({
        url: "/action_servlet",
        data: {
            "action": "get-restaurant-details",
            "id": restaurant,
            "date": date
        },
        dataType: "json",
        success: function(data) {
            update_infos(data);
            update_chart(data.data);
        }
    });
    // update_chart(create_random_data());
}

function update_infos(data) {
    $("#restaurant-name").html(data.name);
    $("#restaurant-theme").html(data.theme);
    $("#restaurant-schedule").html(data.schedule);
    $("#restaurant-status").html(data.status);
    $("#restaurant-throughput").html(data.throughput);
    $("#restaurant-current-waiting-time").html(data.eta); 
}

function update_chart(data) {
    let nb_of_realtime_points = 0;
    let nb_of_predicted_points = 0;
    formatted_data = [];
    
    for(let i=0; i<data.length; i++) {
        let hh = parseInt(data[i].date.substr(0, 2), 10);
        let mm = parseInt(data[i].date.substr(3, 2), 10);
        let ss = parseInt(data[i].date.substr(6, 2), 10);
        let time = new Date($("#date-picker").val());
        time.setHours(hh, mm, ss);
        
        if(typeof data[i].realtime !== 'undefined') {
            nb_of_realtime_points++;
            formatted_data.push({date: time, realtime: data[i].realtime});
        }
        if(typeof data[i].predicted !== 'undefined') {
            nb_of_predicted_points++;
            if(nb_of_realtime_points > 0 && nb_of_predicted_points === 1) {
                formatted_data.push({date: formatted_data[i-1].date, predicted: formatted_data[i-1].realtime});
            }
            formatted_data.push({date: time, predicted: data[i].predicted});
        }
    }
    
    am4core.ready(function() {
        am4core.useTheme(am4themes_animated);
        let chart = am4core.create("chartdiv", am4charts.XYChart);
        chart.data = formatted_data;
        chart.dateFormatter.dateFormat = "HH:mm:ss";

        let date_axis = chart.xAxes.push(new am4charts.DateAxis());
        date_axis.renderer.minGridDistance = 60;
        date_axis.dateFormatter.dateFormat = "HH:mm:ss";
        date_axis.baseInterval = {   
            "timeUnit": "second",
            "count": 10
        };

        let value_axis = chart.yAxes.push(new am4charts.ValueAxis());
        value_axis.title.text = "Temps d'attente";
        value_axis.renderer.minLabelPosition = 0.01;

        chart.scrollbarX = new am4charts.XYChartScrollbar();
        chart.cursor = new am4charts.XYCursor();
        chart.cursor.xAxis = date_axis;
        chart.legend = new am4charts.Legend();

        if(nb_of_realtime_points > 0) {
            let series_realtime = chart.series.push(new am4charts.LineSeries());
            series_realtime.dataFields.valueY = "realtime";
            series_realtime.dataFields.dateX = "date";
            series_realtime.name = "Attente réelle";
            series_realtime.strokeWidth = 2;
            let bullet_realtime = series_realtime.bullets.push(new am4charts.Bullet());
            let square_realtime = bullet_realtime.createChild(am4core.Rectangle);
            square_realtime.width = 3;
            square_realtime.height = 3;
            square_realtime.horizontalCenter = "middle";
            square_realtime.verticalCenter = "middle";
            series_realtime.tooltipText = "Attente actuelle : {valueY}";
            series_realtime.legendSettings.valueText = "{valueY}";
            series_realtime.visible  = false;
            chart.scrollbarX.series.push(series_realtime);
        }

        if(nb_of_predicted_points > 0) {
            let series_predicted = chart.series.push(new am4charts.LineSeries());
            series_predicted.dataFields.valueY = "predicted";
            series_predicted.dataFields.dateX = "date";
            series_predicted.name = "Attente estimée";
            series_predicted.strokeWidth = 2;
            let bullet_predicted = series_predicted.bullets.push(new am4charts.Bullet());
            let square_predicted = bullet_predicted.createChild(am4core.Rectangle);
            square_predicted.width = 3;
            square_predicted.height = 3;
            square_predicted.horizontalCenter = "middle";
            square_predicted.verticalCenter = "middle";
            series_predicted.tooltipText = "Attente estimée : {valueY}";
            series_predicted.legendSettings.valueText = "{valueY}";
            series_predicted.visible  = false;
            chart.scrollbarX.series.push(series_predicted);
        }
    });
}

function calendar_handler(event) {
    update_page($("#date-picker").val());
}





function create_random_data() {
    let data = [];
    let realtime = 0;
    let predicted = 0;
    for(let i=10; i<60; i+=1) {
        for(let j=10; j<60; j+=30) {
            realtime += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 10);
            data.push({date: "12:" + i + ":" + j, realtime: realtime});
        }
    }
    for(let i=10; i<60; i+=5) {
        predicted += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 10);
        data.push({date: "13:" + i + ":00", predicted: predicted});
    }
    return data;
}

