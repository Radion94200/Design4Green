<template xmlns:width="http://www.w3.org/1999/xhtml">
    <div id="city-search">
        <div id="search-content">
            <span class="panel-title">Search</span>
            <div id="search-form">
                <div class="form-group">
                    <div class="input-group mb-3">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="search-prepend">
                                <img src="../../assets/search.png" style="height: 22px" alt="search_logo">
                            </span>
                        </div>
                        <input type="text" class="form-control" placeholder="Query..." aria-label="Query" aria-describedby="query">
                        <div class="input-group-append">
                            <button class="btn btn-primary" id="search-append">Search</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CitySearch",
        data() {
            return {
                query: ""
            }
        },
    }
</script>

<style scoped>

    #city-search {
        width: 90%;
    }

    #search-content {
        padding: 20px;
        border: solid 5px black;
        border-radius: 10px;

        display: grid;
        align-items: center;

        background-color: lightgrey;
    }

    #search-form {
        margin-top: 10px;
    }

</style>