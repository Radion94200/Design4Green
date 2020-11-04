<template>
    <div id="about">
        <div class="logo">
            <img src="../assets/logo.png" alt="logo">
        </div>
        <div class="p about-content">
            <div>
                Detailed stuff about how it works
            </div>
            <div>
                links to github/gitlab/sonarqube...
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

    .logo {
        margin: 15px;
    }

    .about-content {
        margin-top: 20px;
    }


</style>