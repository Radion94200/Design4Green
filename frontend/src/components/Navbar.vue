<template>
    <nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand">
            <img id="navbar-logo" src="../assets/tree_standalone.png" alt="logo">
        </a>
        <h3>INDICE NATIONAL DE FRAGILITÉ NUMÉRIQUE</h3>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
            </ul>
            <div class="my-2 my-lg-0">
                <span class="text-muted">made by <b>Team 49</b></span>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: "Navbar",
        methods: {
            sendExtend(id) {
                this.$emit('onExtend', id)
            }
        }
    }
</script>

<style scoped>
    #navbar-logo {
        border: solid 1px black;
        border-radius: 4px;
        height: 50px;
        padding: 3px;
    }

    .navbar-brand {
        cursor: pointer;
    }
</style>
