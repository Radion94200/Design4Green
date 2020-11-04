<template>
    <div>
        <Filters></Filters>
        <CitySearch></CitySearch>
        <Map></Map>
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

<style scoped>

</style>