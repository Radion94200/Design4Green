<template>
    <div class="card">
        <div class="card-header">
            <h3>Résultats détaillés - {{this.commune.nom}}</h3>
        </div>
        <div class="card-body">
            <div class="table-responsive-sm">
                <table class="table">
                    <thead>
                    <tr>
                        <th scope="col">Code IRIS</th>
                        <th scope="col">Population</th>
                        <th scope="col">Score</th>
                        <th scope="col">Score Département</th>
                        <th scope="col">Score Région</th>
                        <th scope="col">Score Accès</th>
                        <th scope="col">Score Compétences</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr :key="val.code_iris" v-for="val in this.commune['quartiers']">
                        <th scope="row">{{val.code_iris}}</th>
                        <td>{{val.population}}</td>
                        <td>{{val.score}}</td>
                        <td>{{val.score_global_dep}}</td>
                        <td>{{val.score_global_region}}</td>
                        <td>{{val.score_acces}}</td>
                        <td>{{val.score_comp}}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "QuartiersTable",
        props: {
            commune: Object
        }
    }
</script>

<style scoped>
    td {
        text-align: center;
    }
</style>
