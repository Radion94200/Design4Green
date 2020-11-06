<template>
    <div class="card">
        <div class="card-header">
            <h3>Carte</h3>
        </div>
        <div id="map" class="card-body">
            <div class="container">
            <p>Veuillez sélectionner votre commune pour afficher les informations sur la carte.</p>
                <l-map
                        ref="mapCtrl"
                        :zoom="zoom"
                        :center="center"
                        style="height: 500px; width: 100%"
                >
                    <l-tile-layer
                            :url="url"
                            :attribution="attribution"
                    />
                    <l-geo-json
                            ref="mapJson"
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
        props: {
            commune: Object
        },
        data() {
            return {
                show: true,
                service: null,
                enableTooltip: true,
                zoom: 5,
                colors: null,
                center: [47, 2],
                geojson: null,
                url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                attribution:
                    '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            };
        },
        methods: {
            findQuartier (feature) {
                for (let el of this.commune["quartiers"]) {
                    if (feature["properties"]["code_iris"] === el["code_iris"]) {
                        return el
                    }
                }
            }
        },
        watch: {
            commune: function () {
                if (this.commune['nom'] !== "") {
                    const JSON5 = require('json5')
                    let geojson = {
                        "type": "FeatureCollection",
                        "features": []
                    }
                    for (let q of this.commune['quartiers'])
                    {
                        geojson['features'].push(JSON5.parse(q['geojson']))
                    }
                    this.geojson = geojson
                    const self = this
                    setTimeout(function () {
                        self.$refs.mapCtrl.mapObject.fitBounds(self.$refs.mapJson.getBounds())
                    }, 200)
                }
            }
        },
        mounted() {
            let colormap = require('colormap')
             this.colors = colormap({
                colormap: 'YIGnBu',
                nshades: 276,
                format: 'rgbaString',
                alpha: [0.7, 0.9]
            })
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
                    const score = this.findQuartier(feature).score;
                    return {
                        weight: 2,
                        color: "rgba(29,28,28,0.74)",
                        opacity: 1,
                        fillColor: this.colors[275 - score],
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
                        "<div><b>Code Iris: </b>" +
                        feature.properties.code_iris +
                        "</div><div><b>Nom: </b>" +
                        feature.properties.nom_iris +
                        "</div><div><b>Score: </b>" +
                        this.findQuartier(feature).score +
                        "</div><div><b>Score Departement: </b>" +
                        this.findQuartier(feature).score_global_dep +
                        "</div><div><b>Score Region: </b>" +
                        this.findQuartier(feature).score_global_region +
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
