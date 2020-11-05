<template>
    <div id="map">
        <div id="map-content">
            <span class="panel-title">Map</span>
            <div>
                map
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Map"
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