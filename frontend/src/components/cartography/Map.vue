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
        width: 90%;
        margin-top: 15px;
    }

    #map-content {
        padding: 20px;
        border: solid 5px black;
        border-radius: 10px;

        display: grid;
        align-items: center;

        background-color: lightgrey;
    }
</style>