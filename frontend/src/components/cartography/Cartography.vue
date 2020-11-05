<template>
    <div id="cartography" class="container-fluid">
        <div class="row">
            <div class="col-sm-3">
                <Filters></Filters>
            </div>
            <div class="col">
                <div class="row">
                    <CitySearch></CitySearch>
                </div>
                <div class="row">
                    <Map></Map>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Filters from "@/components/cartography/Filters";
    import CitySearch from "@/components/cartography/CitySearch";
    import Map from "@/components/cartography/Map";
    export default {
        name: "Cartographie",
        components: {Map, CitySearch, Filters}
    }
</script>

<style>
    #cartography {
        margin-top: 10px
    }

    .panel-title {
        font-size: 32px;
        font-family: monospace;
        text-align: center;

        border-bottom: solid 3px darkgreen;
    }
</style>