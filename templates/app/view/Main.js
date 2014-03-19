// Global variable to store 10 coldest cities
var mydata;
var data;

// Non-asynchronous function that fetches data

$.ajax({
    url: './scraper/sencha_data.json',
    dataType: 'json',
    async: false,
    data: mydata,
    success: function(result) {
        data = result
    }
});

Ext.define('ColdSpots.view.Main', {
    extend: 'Ext.tab.Panel',
    xtype: 'main',
    requires: [
        'Ext.TitleBar',
        'Ext.Carousel',
        'Ext.Map'
    ],
    config: {
        tabBarPosition: 'bottom',
        scrollable: 'vertical', 
        items: [
            {
                docked: 'top',
                xtype: 'titlebar',
                title: 'ColdSpots'
            },
            {
                title: 'Map',
                id :'geomap',
                iconCls: 'locate',
                xtype: 'map',
                mapOptions : {
                    mapTypeId: google.maps.MapTypeId.ROADMAP,
                    zoom: 10
                },

                // Populate the Google Map once it has been rendered
                listeners: {
                    maprender: function() {
                        var gMap = this.getMap();
                        var bounds = new google.maps.LatLngBounds();

                        var i=0;
                        while (i<10) {
                            var latLng = new google.maps.LatLng(data["lat"][i], data["lon"][i]);
                            gMap.fitBounds(bounds);
                            new google.maps.Marker({
                                map: gMap,
                                title: data["city names"][i],
                                animation: google.maps.Animation.DROP,
                                position: latLng,
                                icon: "http://i.imgur.com/Zm6CeVZ.png"
                            })
                            bounds.extend(latLng);
                            i++;  
                        }
                        gMap.panToBounds(bounds);
                        var weatherLayer = new google.maps.weather.WeatherLayer({
                            map: gMap,
                            temperatureUnits: google.maps.weather.TemperatureUnit.CELSIUS
                        });
                        var cloudLayer = new google.maps.weather.CloudLayer({
                            map: gMap
                        });
                    }
                }
            },
            {
                xtype: 'carousel',
                iconCls: 'info',
                title: 'Cities',
                direction: 'horizontal',
                items: [
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][0]
                        }]
                    },
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][1]
                        }]
                    },
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][1]
                        }]
                    },
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][2]
                        }]
                    },
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][3]
                        }]
                    },
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][4]
                        }]
                    },
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][5]
                        }]
                    },
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][6]
                        }]
                    },
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][7]
                        }]
                    },
                    {
                        layout: {
                            type: 'hbox',
                            align: 'center',
                            pack: 'center'
                        },
                        items: [{
                            html: data["city names"][8]
                        }]
                    },
                ]
            }
        ]
    }
});
