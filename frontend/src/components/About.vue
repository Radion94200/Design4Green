<template>
    <div id="about">
        <div class="row align-items-center">
            <div class="col">
                <div class="p">
                    <div>
                        <a href="https://twitter.com/GreenSociety9" rel="noopener noreferrer" target="_blank">
                            <img class="logo-link" src="../assets/icons8-twitter-48.png" alt="twitter">
                        </a>

                        <a href="https://gitlab.com/dadard/Design4Green" rel="noopener noreferrer" target="_blank">
                            <img class="logo-link" src="../assets/icons8-gitlab-48.png" alt="gitlab">
                        </a>

                        <a href="https://github.com/Radion94200/Design4Green" rel="noopener noreferrer" target="_blank">
                            <img class="logo-link" src="../assets/icons8-github-48.png" alt="github">
                        </a>
                    </div>
                    <div>
                        Nous utilisons Gitlab pour l'integration continue de notre solution.<br>
                        La compilation et de le déploiement du projet sont gérés automatiquement par des pipelines dediées.
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="p">
                    <div>
                        <a href="http://vps-2ea52359.vps.ovh.net:9000/" rel="noopener noreferrer" target="_blank">
                            <img class="logo-link" src="../assets/Sonarqube-48x200.png" alt="sonarqube">
                        </a>
                    </div>
                    <div>
                        Nous utilisons SonarQube pour nous assurer que la qualité de notre code est la meilleure possible.<br>
                        Un compte public est disponible avec le login/password suivant: <code>guest/guest</code>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="p">
                    <div>
                        <a href="http://vps-2ea52359.vps.ovh.net/" rel="noopener noreferrer" target="_blank">
                            <img class="logo-link" src="../assets/logo_sanstexte.png" alt="logo">
                        </a>
                    </div>
                    <div>
                        Ce site utilise des données officielles concernant la fragilité numérique en France.<br>
                        A partir de ces données nous calculons des indicateurs pour caractériser cette fragilité numérique selon les territoires.<br>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "About"
    }
</script>

<style scoped>
    #about {
        text-align: center;
    }

    .logo-link:hover {
        border-bottom: solid 5px black;
    }

    .p {
        margin: 30px;
    }
</style>
