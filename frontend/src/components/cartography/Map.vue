<template>
    <div id="map">
        <div id="map-content">
            <span class="panel-title">Carte</span>
            <div class="row">
                <l-map
                        :zoom="zoom"
                        :center="center"
                        style="height: 500px; width: 100%"
                >
                    <l-tile-layer
                            :url="url"
                            :attribution="attribution"
                    />
                    <l-geo-json
                            v-if="show"
                            :geojson="geojson"
                            :options="options"
                            :options-style="styleFunction"
                    />
                </l-map>
            </div>
        </div>
    </div>
</template>

<script>
    import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet";
    import ApiService from "../../services/api-service";

    export default {
        name: "Map",
        components: {
            LMap,
            LTileLayer,
            LGeoJson
        },
        data() {
            return {
                show: true,
                service: null,
                enableTooltip: true,
                zoom: 6,
                center: [48, -1.219482],
                geojson: null,
                fillColor: "#e4ce7f",
                url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                attribution:
                    '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            };
        },
        methods: {
            goto (commune) {
              this.geojson = this.service.getGeojson(commune)
          }
        },
        mounted() {
            this.service = new ApiService();
        },
        computed: {
            options() {
                return {
                    onEachFeature: this.onEachFeatureFunction
                };
            },
            styleFunction() {
                const fillColor = this.fillColor;
                return () => {
                    return {
                        weight: 2,
                        color: "#ECEFF1",
                        opacity: 1,
                        fillColor: fillColor,
                        fillOpacity: 1
                    };
                };
            },
            onEachFeatureFunction() {
                if (!this.enableTooltip) {
                    return () => {};
                }
                return (feature, layer) => {
                    layer.bindTooltip(
                        "<div>code:" +
                        feature.properties.code +
                        "</div><div>nom: " +
                        feature.properties.nom +
                        "</div>",
                        { permanent: false, sticky: true }
                    );
                };
            }
        }
    }
</script>

<style scoped>
    #map {
        width: 100%;
    }

    #map-content {
        margin: 10px;
        padding: 20px;
        border: solid 5px black;
        border-radius: 10px;

        display: grid;
        align-items: center;

        background-color: lightgrey;
    }
</style>
