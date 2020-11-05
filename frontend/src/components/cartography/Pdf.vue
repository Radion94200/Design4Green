<template>
    <div class="card">
        <div class="card-header">
            <h3>Export PDF</h3>
        </div>
        <div class="card-body">
            <p>
                Ce site internet vous permet de récupérer des résultats détaillés sur votre commune au format PDF.<br>
                Pour cela, veuillez dans un premier temps sélectionner votre ville. Lorsque la ville sera sélectionnée, un bouton apparaitra pour récupérer ce document PDF.
            </p>
            <div>
                <a class="btn btn-warning" :href="this.url + '/pdf_view?commune=' + this.commune" target="_blank">Voir les résultats</a> <!--TODO : Add commune event -->
                <a class="btn btn-warning" :href="this.url + '/pdf_download?commune=' + this.commune" target="_blank">Télécharger les résultats</a>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Pdf",
        props: {
            commune: String
        },
        data() {
            return {
                url: "http://vps-2ea52359.vps.ovh.net:8080"
            }
        }
    }
</script>

<style scoped>

</style>
