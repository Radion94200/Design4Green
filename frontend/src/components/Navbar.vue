<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" @click="sendExtend('app-home')">
            <img id="navbar-logo" src="../assets/tree_standalone.png" alt="logo">
            Home
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <a class="nav-link" @click="sendExtend('app-cartography')">Map</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" @click="sendExtend('app-about')">About</a>
                </li>
            </ul>
            <div class="my-2 my-lg-0">
                <span class="text-muted">made by <code>Team 49</code></span>
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

    .nav-link {
        cursor: pointer;
    }

</style>