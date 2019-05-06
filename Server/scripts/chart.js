function update_chart(restaurants, date) {
    am4core.ready(function() {
        let formatted_data = [];
        let nb_of_realtime_points = [];
        let nb_of_predicted_points = [];
        for(let r=0; r<restaurants.length; r++) {
            let realtime_label = "realtime" + r;
            let predicted_label = "predicted" + r;
            nb_of_realtime_points[r] = 0;
            nb_of_predicted_points[r] = 0;
            
            for(let i=0; i<restaurants[r].data.length; i++) {
                let hh = parseInt(restaurants[r].data[i].date.substr(0, 2), 10);
                let mm = parseInt(restaurants[r].data[i].date.substr(3, 2), 10);
                let ss = parseInt(restaurants[r].data[i].date.substr(6, 2), 10);
                let time = new Date(date);
                time.setHours(hh, mm, ss);
                
                if(typeof restaurants[r].data[i].realtime !== 'undefined') {
                    nb_of_realtime_points[r]++;
                    formatted_data.push({date: time, [realtime_label]: restaurants[r].data[i].realtime});
                }
                if(typeof restaurants[r].data[i].predicted !== 'undefined') {
                    nb_of_predicted_points[r]++;
                    if(nb_of_realtime_points[r] > 0 && nb_of_predicted_points[r] === 1) {
                        formatted_data.push({date: formatted_data[formatted_data.length-1].date,
                                            [predicted_label]: formatted_data[formatted_data.length-1][realtime_label]});
                    }
                    formatted_data.push({date: time, [predicted_label]: restaurants[r].data[i].predicted});
                }
            }
        }
        
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
        
        for(let r=0; r<restaurants.length; r++) {
            let realtime_label = "realtime" + r;
            let predicted_label = "predicted" + r;
            if(nb_of_realtime_points[r] > 0) {
                let series_realtime = chart.series.push(new am4charts.LineSeries());
                series_realtime.dataFields.valueY = realtime_label;
                series_realtime.dataFields.dateX = "date";
                series_realtime.name = restaurants[r].name + " (attente mesurée)";
                series_realtime.strokeWidth = 2;
                let bullet_realtime = series_realtime.bullets.push(new am4charts.Bullet());
                let square_realtime = bullet_realtime.createChild(am4core.Rectangle);
                square_realtime.width = 3;
                square_realtime.height = 3;
                square_realtime.horizontalCenter = "middle";
                square_realtime.verticalCenter = "middle";
                series_realtime.tooltipText = "Attente : {valueY} min";
                series_realtime.legendSettings.valueText = "{valueY}";
                series_realtime.visible = false;
                chart.scrollbarX.series.push(series_realtime);
            }

            if(nb_of_predicted_points[r] > 0) {
                let series_predicted = chart.series.push(new am4charts.LineSeries());
                series_predicted.dataFields.valueY = predicted_label;
                series_predicted.dataFields.dateX = "date";
                series_predicted.name = restaurants[r].name + " (attente estimée)";
                series_predicted.strokeWidth = 2;
                let bullet_predicted = series_predicted.bullets.push(new am4charts.Bullet());
                let square_predicted = bullet_predicted.createChild(am4core.Rectangle);
                square_predicted.width = 3;
                square_predicted.height = 3;
                square_predicted.horizontalCenter = "middle";
                square_predicted.verticalCenter = "middle";
                series_predicted.tooltipText = "Attente : {valueY} min";
                series_predicted.legendSettings.valueText = "{valueY}";
                series_predicted.visible = false;
                chart.scrollbarX.series.push(series_predicted);
            }
        }
    });
}

