<template>
    <div id="cartography" class="container-fluid">
        <div class="row">
            <div class="col-sm-2">
                <div class="row">
                    <Recherche @recherche="recherche"></Recherche>
                </div>
                <br>
                <div class="row">
                    <Legend></Legend>
                </div>
            </div>
            <div class="col-sm-4">
                <Map></Map>
            </div>
            <div class="col-sm-6">
                <div class="row">
                    <QuartiersTable :commune="this.commune"></QuartiersTable>
                </div>
                <br>
                <div class="row">
                    <Pdf :commune="this.commune.nom"></Pdf>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Recherche from "@/components/cartography/Recherche";
    import Map from "@/components/cartography/Map";
    import Legend from "@/components/cartography/Legend";
    import Pdf from "@/components/cartography/Pdf";
    import QuartiersTable from "@/components/cartography/QuartiersTable";

    export default {
        name: "Cartographie",
        components: {Legend, Map, Recherche, Pdf, QuartiersTable},
        data () {
            return {
                commune: {
                    nom: "",
                    quartiers: []
                }
            }
        },
        methods: {
            recherche (commune) {
                this.commune = commune
            }
        }
    }
</script>

<style>
    #cartography {
        margin-top: 10px
    }
</style>
