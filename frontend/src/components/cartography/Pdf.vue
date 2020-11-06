<template>
    <div class="card">
        <div class="card-header">
            <h3>Export PDF</h3>
        </div>
        <div class="card-body">
            <p>
                Ce site internet vous permet de récupérer des résultats détaillés sur votre commune au format PDF.<br>
                Pour cela, veuillez dans un premier temps sélectionner votre ville. Lorsque la ville sera sélectionnée,
                les boutons seront accessibles.<br><br>

                Ce document contient la description des différents indicateurs utilisés pour les calculs des scores
                ainsi que des propositions d'axes d'amélioration.<br><br>

                Nous vous conseillons de télécharger votre rapport ci-dessous.

            </p>
            <div v-if="this.commune === ''">
                <button class="btn btn-warning" disabled>Voir les résultats</button>
                <button class="btn btn-warning" disabled>Télécharger les résultats</button>
            </div>
            <div v-else>
                <a
                        class="btn btn-warning"
                        :href="this.url + '/pdf_view?commune=' + this.commune"
                        target="_blank"
                >
                    Voir les résultats
                </a>

                <a
                        class="btn btn-warning"
                        :href="this.url + '/pdf_download?commune=' + this.commune"
                        target="_blank"
                >
                    Télécharger les résultats
                </a>
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
                url: "http://vps-2ea52359.vps.ovh.net:8000"
            }
        }
    }
</script>

<style scoped>
a {
    margin-left: 10px;
    margin-right: 10px;
}
button {
    margin-left: 10px;
    margin-right: 10px;
}
.card {
    width: 100%
}
</style>
