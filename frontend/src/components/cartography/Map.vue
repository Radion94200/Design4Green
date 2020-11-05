<template>
    <div class="card">
        <div class="card-header">
            <h3>Carte</h3>
        </div>
        <div id="map" class="card-body">
            <div class="container">
            <p>Veuillez sélectionner votre commune pour afficher les informations sur la carte.</p>
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
                commune: null,
                zoom: 6,
                center: [48, -1.219482],
                geojson: null,
                url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                attribution:
                    '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            };
        },
        methods: {
            goto (commune) {
              this.geojson = this.service.getGeojson(commune)
            },
            findQuartier (feature) {
                for (let el of this.commune["quartiers"]) {
                    if (feature["properties"]["code_iris"] === el["code_iris"]) {
                        return el
                    }
                }
            }
        },
        mounted() {
            this.service = new ApiService();
            setTimeout(function() { window.dispatchEvent(new Event('resize')) }, 250);
        },
        computed: {
            options() {
                return {
                    onEachFeature: this.onEachFeatureFunction
                };
            },
            styleFunction() {
                return (feature) => {
                    const score = this.findQuartier(feature);
                    let fillColor = "";
                    if (score < 100)
                        fillColor = "#d2d2d2";
                    else
                        fillColor = "#d01515"; // todo : add a map
                    return {
                        weight: 2,
                        color: "#131111",
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
        display: grid;
    }
</style>
