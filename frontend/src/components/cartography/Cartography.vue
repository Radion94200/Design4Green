<template>
    <div id="cartography" class="container-fluid">
        <div class="row">
            <div class="col-sm-3">
                <div class="row">
                    <Filters></Filters>
                </div>
<!--                <div class="row">-->
<!--                    <CitySearch></CitySearch>-->
<!--                </div>-->
            </div>
            <div class="col">
                <div class="row">
                    <Map></Map>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Filters from "@/components/cartography/Filters";
    import Map from "@/components/cartography/Map";
    export default {
        name: "Cartographie",
        components: {Map, Filters}
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

        border-bottom: solid 3px black;
    }
</style>