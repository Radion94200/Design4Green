<template>
    <div id="filters">
        <div id="filters-content">
                        <div class="custom-control custom-checkbox input-group-menu">
                            <input type="checkbox" class="custom-control-input" id="is-dom-tom-input">
                            <label class="custom-control-label" for="is-dom-tom-input">In DOM-TOM</label>
                        </div>

                        <div class="input-group-menu">
                            <label for="region-input">Region</label>
                            <input type="text" class="form-control" id="region-input">
                        </div>

                        <div class="input-group-menu">
                            <label for="dep-input">Department</label>
                            <input type="text" class="form-control" id="dep-input">
                        </div>

                        <div class="input-group-menu">
                            <label for="city-input">City</label>
                            <input type="text" class="form-control" id="city-input">
                        </div>

                        <div class="input-group-menu">
                            <label for="neigh-input">Neighbourhood</label>
                            <input type="text" class="form-control" id="neigh-input">
                        </div>

                        <div class="input-group-menu">
                            <button class="btn btn-primary" style="width: 100%">Submit</button>
                        </div>

                    </div>
    </div>
</template>

<script>
    export default {
        name: "Filters",
        data() {
            return {
            };
        },

    }
</script>

<style scoped>
    #filters {

    }

    #filters-content {
        padding: 20px;
        display: grid;
        align-items: center;

        border-radius: 10px;
        border: solid 5px darkgreen;

        background-color: lightgreen;
    }

    .input-group-menu {
        margin-top: 20px;
        margin-bottom: 20px;
        width: 100%;
    }
</style>
