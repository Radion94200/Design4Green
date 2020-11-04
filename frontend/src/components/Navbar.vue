<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">
            <router-link class="nav-link" to="/">
                <img id="navbar-logo" src="../assets/tree_standalone.png">
                Design4Green
            </router-link>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <router-link class="nav-link" to="/map">Map</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/about">About</router-link>
                </li>
            </ul>
            <div class="my-2 my-lg-0">
                <span class="text-muted">made by <code>GreenSociety</code></span>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: "Navbar"
    }
</script>

<style scoped>
    #navbar-logo {
        border: solid 1px black;
        border-radius: 4px;
        height: 50px;
        padding: 3px;
    }

</style>